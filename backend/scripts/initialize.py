"""
Initialization script to build FAISS index and prepare data
Run this script before starting the API server
"""

import os
import sys

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.preprocess import DataPreprocessor
from utils.evaluator import Evaluator

def main():
    print("=" * 60)
    print("SHL Assessment Recommendation System - Initialization")
    print("=" * 60)
    
    # Step 1: Build FAISS index
    print("\n[Step 1/3] Building FAISS index...")
    preprocessor = DataPreprocessor()
    preprocessor.build_index()
    print("✓ FAISS index built successfully")
    
    # Step 2: Evaluate on labeled data
    print("\n[Step 2/3] Evaluating on labeled data...")
    evaluator = Evaluator()
    results = evaluator.evaluate(k=10)
    print(f"✓ Evaluation complete. Mean Recall@10: {results['mean_recall_at_10']:.4f}")
    
    # Step 3: Generate submission CSV
    print("\n[Step 3/3] Generating submission CSV...")
    evaluator.generate_submission_csv()
    print("✓ Submission CSV generated")
    
    print("\n" + "=" * 60)
    print("Initialization complete! You can now start the API server.")
    print("=" * 60)
    print("\nTo start the server, run:")
    print("  python app.py")
    print("  or")
    print("  uvicorn app:app --reload")

if __name__ == "__main__":
    main()

