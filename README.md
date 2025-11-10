# SHL Assessment Recommendation System

AI-powered recommendation system for SHL assessments that recommends relevant individual test solutions based on job descriptions or natural language queries.

## 🚀 Features

- **Semantic Search**: Uses Sentence-BERT embeddings for intelligent matching
- **Fast Retrieval**: FAISS vector database for efficient similarity search
- **Modern UI**: Beautiful, responsive web interface with dark mode
- **RESTful API**: FastAPI backend with clean endpoints
- **Evaluation**: Built-in Recall@10 metric computation

## 📁 Project Structure

```
shl-assessment-recommender/
├── backend/              # FastAPI backend
│   ├── app.py           # Main application
│   ├── api/             # API routes
│   ├── models/          # Embedding models
│   ├── utils/           # Utilities (crawler, preprocess, evaluator)
│   ├── data/            # Dataset files
│   └── vectorstore/     # FAISS index storage
├── frontend/            # Next.js frontend
│   ├── pages/           # Next.js pages
│   ├── components/      # React components
│   └── utils/           # Frontend utilities
└── docs/                # Documentation
    ├── approach_report.md
    └── submission_instructions.md
```

## 🛠️ Setup

### Prerequisites

- Python 3.10+
- Node.js 18+
- `Gen_AI Dataset.xlsx` file (place in `backend/data/`)

### Backend Setup

1. Navigate to backend directory:
   ```bash
   cd backend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Place your dataset:
   - Copy `Gen_AI Dataset.xlsx` to `backend/data/`

4. Initialize the system (build index):
   ```bash
   python scripts/initialize.py
   ```
   Or manually:
   ```bash
   python -m utils.preprocess
   ```

5. Start the server:
   ```bash
   python app.py
   ```
   Or using uvicorn:
   ```bash
   uvicorn app:app --reload --host 0.0.0.0 --port 8000
   ```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Create `.env.local` (optional):
   ```env
   NEXT_PUBLIC_API_URL=http://localhost:8000
   ```

4. Run development server:
   ```bash
   npm run dev
   ```

The frontend will be available at `http://localhost:3000`

## 📡 API Endpoints

### Health Check
```bash
GET /health
```
Response:
```json
{"status": "running"}
```

### Get Recommendations
```bash
POST /recommend
Content-Type: application/json

{
  "query": "Hiring for a Python developer with strong communication skills"
}
```

Response:
```json
{
  "recommendations": [
    {
      "assessment_name": "SHL Verify Coding Test",
      "assessment_url": "https://www.shl.com/..."
    },
    ...
  ]
}
```

## 🧪 Evaluation

Run evaluation on labeled data:

```bash
cd backend
python -m utils.evaluator
```

This will:
- Compute Mean Recall@10 on labeled queries
- Generate `docs/results.csv` with evaluation results
- Generate `docs/submission.csv` for unlabeled test queries

## 🚢 Deployment

See `docs/submission_instructions.md` for detailed deployment instructions:

1. **Backend**: Deploy to Render/Railway/Hugging Face
2. **Frontend**: Deploy to Vercel
3. **Generate Submission CSV**: Run evaluation script
4. **Create Report**: Complete `docs/approach_report.md`

## 📊 Technology Stack

### Backend
- FastAPI
- Sentence-BERT (all-MiniLM-L6-v2)
- FAISS
- BeautifulSoup4
- pandas, numpy

### Frontend
- Next.js 14+
- TailwindCSS
- Framer Motion
- Axios

## 📝 Documentation

- **Approach Report**: `docs/approach_report.md`
- **Deployment Guide**: `docs/submission_instructions.md`
- **Backend README**: `backend/README.md`
- **Frontend README**: `frontend/README.md`

## 🎯 Usage Example

1. Start backend: `cd backend && python app.py`
2. Start frontend: `cd frontend && npm run dev`
3. Open browser: `http://localhost:3000`
4. Enter query: "Hiring for a data analyst with SQL skills"
5. Get recommendations!

## 🔧 Troubleshooting

### Index not found
Run initialization script:
```bash
cd backend
python scripts/initialize.py
```

### CORS errors
Ensure CORS middleware is enabled in `backend/app.py`

### Dataset not found
Place `Gen_AI Dataset.xlsx` in `backend/data/` directory

## 📄 License

This project is created for SHL AI Research Intern assignment.

## 👤 Author

Created for SHL AI Research Intern Assessment

---

For detailed information, see the documentation in the `docs/` directory.

