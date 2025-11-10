"""
API Routes for SHL Assessment Recommendation System
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import os
import sys

# Add parent directory to path
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, backend_dir)

from models.embedding_model import EmbeddingModel
from utils.preprocess import DataPreprocessor
import faiss
import numpy as np
import pandas as pd
import pickle

router = APIRouter()

# Global variables for model and index
embedding_model = None
faiss_index = None
assessment_data = None

class QueryRequest(BaseModel):
    query: str

class RecommendationResponse(BaseModel):
    assessment_name: str
    assessment_url: str

class RecommendationsResponse(BaseModel):
    recommendations: List[RecommendationResponse]

def load_model_and_index():
    """Load the embedding model and FAISS index"""
    global embedding_model, faiss_index, assessment_data
    
    if embedding_model is None:
        embedding_model = EmbeddingModel()
    
    # Load FAISS index
    index_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "vectorstore", "faiss_index.bin")
    data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "vectorstore", "assessment_data.pkl")
    
    if os.path.exists(index_path) and os.path.exists(data_path):
        faiss_index = faiss.read_index(index_path)
        with open(data_path, 'rb') as f:
            assessment_data = pickle.load(f)
    else:
        # Initialize if index doesn't exist
        preprocessor = DataPreprocessor()
        preprocessor.build_index()
        faiss_index = faiss.read_index(index_path)
        with open(data_path, 'rb') as f:
            assessment_data = pickle.load(f)

@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "running"}

@router.post("/recommend", response_model=RecommendationsResponse)
async def get_recommendations(request: QueryRequest):
    """
    Get assessment recommendations based on query
    """
    global embedding_model, faiss_index, assessment_data
    
    try:
        # Load model and index if not already loaded
        if faiss_index is None or assessment_data is None:
            load_model_and_index()
        
        if not request.query or not request.query.strip():
            raise HTTPException(status_code=400, detail="Query cannot be empty")
        
        # Generate embedding for query
        query_embedding = embedding_model.encode([request.query.strip()])
        query_embedding = np.array(query_embedding, dtype='float32')
        
        # Normalize for cosine similarity
        faiss.normalize_L2(query_embedding)
        
        # Search in FAISS index (top 10)
        k = min(10, faiss_index.ntotal)
        distances, indices = faiss_index.search(query_embedding, k)
        
        # Get recommendations
        recommendations = []
        for idx in indices[0]:
            if idx < len(assessment_data):
                assessment = assessment_data[idx]
                recommendations.append(
                    RecommendationResponse(
                        assessment_name=assessment['name'],
                        assessment_url=assessment['url']
                    )
                )
        
        # Filter out duplicates and ensure we have 5-10 results
        seen_urls = set()
        unique_recommendations = []
        for rec in recommendations:
            if rec.assessment_url not in seen_urls:
                seen_urls.add(rec.assessment_url)
                unique_recommendations.append(rec)
                if len(unique_recommendations) >= 10:
                    break
        
        # Ensure at least 5 recommendations
        if len(unique_recommendations) < 5 and len(recommendations) >= 5:
            # Add more if available
            for rec in recommendations:
                if rec.assessment_url not in seen_urls:
                    unique_recommendations.append(rec)
                    if len(unique_recommendations) >= 5:
                        break
        
        return RecommendationsResponse(recommendations=unique_recommendations)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating recommendations: {str(e)}")

