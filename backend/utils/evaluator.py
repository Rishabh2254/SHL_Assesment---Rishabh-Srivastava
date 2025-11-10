"""
Evaluation Module for Computing Recall@10
"""

import pandas as pd
import numpy as np
import os
import sys
import faiss
import pickle

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.embedding_model import EmbeddingModel
from utils.preprocess import DataPreprocessor

class Evaluator:
    """Evaluates recommendation system using Recall@10 metric"""
    
    def __init__(self):
        self.embedding_model = EmbeddingModel()
        self.data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
        self.vectorstore_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "vectorstore")
    
    def load_index_and_data(self):
        """Load FAISS index and assessment data"""
        index_path = os.path.join(self.vectorstore_dir, "faiss_index.bin")
        data_path = os.path.join(self.vectorstore_dir, "assessment_data.pkl")
        
        if not os.path.exists(index_path) or not os.path.exists(data_path):
            print("Index not found. Building index...")
            preprocessor = DataPreprocessor()
            preprocessor.build_index()
        
        index = faiss.read_index(index_path)
        with open(data_path, 'rb') as f:
            assessment_data = pickle.load(f)
        
        return index, assessment_data
    
    def compute_recall_at_k(self, predicted_urls: list, true_urls: list, k: int = 10) -> float:
        """
        Compute Recall@K
        
        Args:
            predicted_urls: List of predicted assessment URLs
            true_urls: List of true/relevant assessment URLs
            k: Number of top predictions to consider
            
        Returns:
            Recall@K score (0.0 to 1.0)
        """
        if len(true_urls) == 0:
            return 0.0
        
        # Take top k predictions
        top_k_predicted = predicted_urls[:k]
        
        # Count how many true URLs are in top k predictions
        relevant_retrieved = len(set(top_k_predicted) & set(true_urls))
        
        # Recall = relevant_retrieved / total_relevant
        recall = relevant_retrieved / len(true_urls) if len(true_urls) > 0 else 0.0
        
        return recall
    
    def evaluate(self, k: int = 10) -> dict:
        """
        Evaluate the recommendation system on labeled test data
        
        Returns:
            Dictionary with evaluation metrics
        """
        print("Starting evaluation...")
        
        # Load labeled training data
        train_path = os.path.join(self.data_dir, "labeled_train.csv")
        
        if not os.path.exists(train_path):
            print(f"Warning: {train_path} not found. Skipping evaluation.")
            return {"mean_recall_at_10": 0.0, "total_queries": 0}
        
        train_df = pd.read_csv(train_path)
        
        # Group by query to get all relevant URLs for each query
        query_to_urls = {}
        for _, row in train_df.iterrows():
            query = str(row.get('Query', '')).strip()
            url = str(row.get('Assessment_url', '')).strip()
            
            if query and url and url != 'nan':
                if query not in query_to_urls:
                    query_to_urls[query] = []
                query_to_urls[query].append(url)
        
        if len(query_to_urls) == 0:
            print("No labeled queries found. Skipping evaluation.")
            return {"mean_recall_at_10": 0.0, "total_queries": 0}
        
        # Load index and data
        index, assessment_data = self.load_index_and_data()
        
        # Evaluate each query
        recalls = []
        results = []
        
        for query, true_urls in query_to_urls.items():
            # Generate recommendations
            query_embedding = self.embedding_model.encode([query])
            query_embedding = np.array(query_embedding, dtype='float32')
            faiss.normalize_L2(query_embedding)
            
            # Search in index
            search_k = min(k, index.ntotal)
            distances, indices = index.search(query_embedding, search_k)
            
            # Get predicted URLs
            predicted_urls = []
            for idx in indices[0]:
                if idx < len(assessment_data):
                    predicted_urls.append(assessment_data[idx]['url'])
            
            # Compute recall
            recall = self.compute_recall_at_k(predicted_urls, true_urls, k)
            recalls.append(recall)
            
            results.append({
                'query': query,
                'recall_at_10': recall,
                'num_relevant': len(true_urls),
                'num_retrieved': len(set(predicted_urls) & set(true_urls))
            })
        
        # Compute mean recall
        mean_recall = np.mean(recalls) if len(recalls) > 0 else 0.0
        
        # Save results
        results_df = pd.DataFrame(results)
        results_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "docs", "results.csv")
        os.makedirs(os.path.dirname(results_path), exist_ok=True)
        results_df.to_csv(results_path, index=False)
        
        print(f"\nEvaluation Results:")
        print(f"Mean Recall@{k}: {mean_recall:.4f}")
        print(f"Total Queries: {len(recalls)}")
        print(f"Results saved to {results_path}")
        
        return {
            "mean_recall_at_10": mean_recall,
            "total_queries": len(recalls),
            "individual_recalls": recalls,
            "results": results
        }
    
    def generate_submission_csv(self):
        """Generate submission CSV for unlabeled test queries"""
        print("Generating submission CSV...")
        
        # Load unlabeled test data
        test_path = os.path.join(self.data_dir, "unlabeled_test.csv")
        
        if not os.path.exists(test_path):
            print(f"Warning: {test_path} not found.")
            return
        
        test_df = pd.read_csv(test_path)
        
        # Load index and data
        index, assessment_data = self.load_index_and_data()
        
        # Generate recommendations for each query
        submission_data = []
        
        for _, row in test_df.iterrows():
            query = str(row.get('Query', '')).strip()
            
            if not query:
                continue
            
            # Generate recommendations
            query_embedding = self.embedding_model.encode([query])
            query_embedding = np.array(query_embedding, dtype='float32')
            faiss.normalize_L2(query_embedding)
            
            # Search in index (top 10)
            k = min(10, index.ntotal)
            distances, indices = index.search(query_embedding, k)
            
            # Get predicted URLs
            seen_urls = set()
            for idx in indices[0]:
                if idx < len(assessment_data):
                    url = assessment_data[idx]['url']
                    if url not in seen_urls:
                        seen_urls.add(url)
                        submission_data.append({
                            'Query': query,
                            'Assessment_url': url
                        })
                        if len(seen_urls) >= 10:
                            break
        
        # Save submission CSV
        submission_df = pd.DataFrame(submission_data)
        submission_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "docs", "submission.csv")
        os.makedirs(os.path.dirname(submission_path), exist_ok=True)
        submission_df.to_csv(submission_path, index=False)
        
        print(f"Submission CSV saved to {submission_path}")
        print(f"Total recommendations: {len(submission_df)}")

