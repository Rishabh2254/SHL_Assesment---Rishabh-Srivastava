"""
Data Preprocessing and FAISS Index Building
"""

import pandas as pd
import numpy as np
import faiss
import os
import pickle
from typing import List, Dict
from models.embedding_model import EmbeddingModel
from utils.crawler import SHLCatalogCrawler

class DataPreprocessor:
    """Handles data preprocessing and FAISS index creation"""
    
    def __init__(self):
        self.embedding_model = EmbeddingModel()
        self.data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
        self.vectorstore_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "vectorstore")
        
        # Create directories if they don't exist
        os.makedirs(self.data_dir, exist_ok=True)
        os.makedirs(self.vectorstore_dir, exist_ok=True)
    
    def load_catalog(self) -> pd.DataFrame:
        """Load or create SHL catalog data"""
        catalog_path = os.path.join(self.data_dir, "shl_catalog.csv")
        
        if os.path.exists(catalog_path):
            print(f"Loading catalog from {catalog_path}")
            df = pd.read_csv(catalog_path)
        else:
            print("Catalog not found. Crawling SHL website...")
            crawler = SHLCatalogCrawler()
            df = crawler.crawl_catalog()
            df.to_csv(catalog_path, index=False)
            print(f"Catalog saved to {catalog_path}")
        
        return df
    
    def load_dataset(self) -> tuple:
        """Load train and test datasets from Excel file"""
        excel_path = os.path.join(self.data_dir, "Gen_AI Dataset.xlsx")
        
        if not os.path.exists(excel_path):
            print(f"Warning: {excel_path} not found. Creating placeholder datasets...")
            return self._create_placeholder_datasets()
        
        try:
            # Read Excel file
            df = pd.read_excel(excel_path)
            
            # Split into train (labeled) and test (unlabeled)
            # Assuming the Excel has columns: Query, Assessment_url (for labeled) or just Query (for unlabeled)
            train_data = []
            test_data = []
            
            for idx, row in df.iterrows():
                query = str(row.get('Query', '')).strip()
                assessment_url = str(row.get('Assessment_url', '')).strip()
                
                if query:
                    if assessment_url and assessment_url != 'nan' and assessment_url:
                        # Has label - training data
                        train_data.append({
                            'Query': query,
                            'Assessment_url': assessment_url
                        })
                    else:
                        # No label - test data
                        test_data.append({
                            'Query': query
                        })
            
            train_df = pd.DataFrame(train_data)
            test_df = pd.DataFrame(test_data)
            
            # Save as CSV
            train_path = os.path.join(self.data_dir, "labeled_train.csv")
            test_path = os.path.join(self.data_dir, "unlabeled_test.csv")
            
            train_df.to_csv(train_path, index=False)
            test_df.to_csv(test_path, index=False)
            
            print(f"Loaded {len(train_df)} labeled queries and {len(test_df)} unlabeled queries")
            
            return train_df, test_df
        
        except Exception as e:
            print(f"Error loading dataset: {str(e)}")
            return self._create_placeholder_datasets()
    
    def _create_placeholder_datasets(self) -> tuple:
        """Create placeholder datasets if Excel file is not found"""
        train_data = [
            {'Query': 'Hiring for a Python developer with strong communication skills', 'Assessment_url': ''},
            {'Query': 'Need a data analyst who can work with SQL and Excel', 'Assessment_url': ''},
            {'Query': 'Looking for a software engineer with problem-solving abilities', 'Assessment_url': ''},
        ]
        test_data = [
            {'Query': 'Hiring a project manager with leadership skills'},
            {'Query': 'Need a financial analyst with numerical reasoning'},
        ]
        
        train_df = pd.DataFrame(train_data)
        test_df = pd.DataFrame(test_data)
        
        train_path = os.path.join(self.data_dir, "labeled_train.csv")
        test_path = os.path.join(self.data_dir, "unlabeled_test.csv")
        
        train_df.to_csv(train_path, index=False)
        test_df.to_csv(test_path, index=False)
        
        return train_df, test_df
    
    def prepare_assessment_texts(self, df: pd.DataFrame) -> List[str]:
        """Prepare text for embedding from assessment DataFrame"""
        texts = []
        
        for _, row in df.iterrows():
            # Combine name, description, and type for better semantic matching
            name = str(row.get('name', ''))
            description = str(row.get('description', ''))
            assessment_type = str(row.get('type', ''))
            
            # Create a comprehensive text representation
            text = f"{name}. {description}"
            if assessment_type:
                type_label = "Technical/Knowledge Assessment" if assessment_type == 'K' else "Personality/Behavioral Assessment"
                text += f" Type: {type_label}"
            
            texts.append(text)
        
        return texts
    
    def build_index(self):
        """Build FAISS index from catalog data"""
        print("Building FAISS index...")
        
        # Load catalog
        catalog_df = self.load_catalog()
        
        if len(catalog_df) == 0:
            raise ValueError("Catalog is empty. Cannot build index.")
        
        # Prepare texts
        texts = self.prepare_assessment_texts(catalog_df)
        
        # Generate embeddings
        print("Generating embeddings...")
        embeddings = self.embedding_model.encode_batch(texts, batch_size=32)
        
        # Get embedding dimension
        dimension = embeddings.shape[1]
        
        # Create FAISS index (L2 distance)
        index = faiss.IndexFlatL2(dimension)
        
        # Normalize embeddings for cosine similarity (using inner product)
        faiss.normalize_L2(embeddings)
        index = faiss.IndexFlatIP(dimension)  # Inner product for cosine similarity
        
        # Add embeddings to index
        index.add(embeddings.astype('float32'))
        
        # Save index
        index_path = os.path.join(self.vectorstore_dir, "faiss_index.bin")
        faiss.write_index(index, index_path)
        print(f"FAISS index saved to {index_path}")
        
        # Save assessment data (for retrieving names and URLs)
        assessment_data = []
        for idx, row in catalog_df.iterrows():
            assessment_data.append({
                'name': str(row.get('name', '')),
                'url': str(row.get('url', '')),
                'description': str(row.get('description', '')),
                'type': str(row.get('type', ''))
            })
        
        data_path = os.path.join(self.vectorstore_dir, "assessment_data.pkl")
        with open(data_path, 'wb') as f:
            pickle.dump(assessment_data, f)
        print(f"Assessment data saved to {data_path}")
        
        print(f"Index built successfully with {index.ntotal} assessments")

