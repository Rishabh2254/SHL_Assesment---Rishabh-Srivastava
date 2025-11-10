# SHL Assessment Recommendation System - Backend

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Place your `Gen_AI Dataset.xlsx` file in the `data/` directory

3. Build the FAISS index:
```bash
python -m utils.preprocess
```

Or run the evaluation script which will build the index automatically:
```bash
python -m utils.evaluator
```

4. Run the server:
```bash
python app.py
```

Or using uvicorn directly:
```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

## API Endpoints

- `GET /health` - Health check
- `POST /recommend` - Get recommendations
  - Request body: `{"query": "your query here"}`
  - Response: `{"recommendations": [{"assessment_name": "...", "assessment_url": "..."}]}`

## Directory Structure

- `app.py` - Main FastAPI application
- `api/routes.py` - API route handlers
- `models/embedding_model.py` - Sentence-BERT embedding model
- `utils/crawler.py` - Web crawler for SHL catalog
- `utils/preprocess.py` - Data preprocessing and index building
- `utils/evaluator.py` - Evaluation metrics (Recall@10)
- `data/` - Dataset files
- `vectorstore/` - FAISS index and assessment data

