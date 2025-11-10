"""
Embedding Model using Sentence-BERT
"""

from sentence_transformers import SentenceTransformer
import os

class EmbeddingModel:
    """Wrapper for Sentence-BERT embedding model"""
    
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Initialize the embedding model
        
        Args:
            model_name: Name of the Sentence-BERT model to use
        """
        self.model_name = model_name
        self.model = SentenceTransformer(model_name)
    
    def encode(self, texts):
        """
        Encode texts into embeddings
        
        Args:
            texts: List of strings or single string
            
        Returns:
            numpy array of embeddings
        """
        if isinstance(texts, str):
            texts = [texts]
        
        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True,
            show_progress_bar=False
        )
        
        return embeddings
    
    def encode_batch(self, texts, batch_size=32):
        """
        Encode texts in batches
        
        Args:
            texts: List of strings
            batch_size: Batch size for encoding
            
        Returns:
            numpy array of embeddings
        """
        embeddings = self.model.encode(
            texts,
            batch_size=batch_size,
            convert_to_numpy=True,
            normalize_embeddings=True,
            show_progress_bar=True
        )
        
        return embeddings

