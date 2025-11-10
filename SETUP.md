# Complete Setup Instructions

## Initial Setup

### 1. Clone or Download Project

```bash
# If using git
git clone <your-repo-url>
cd shl-assessment-recommender

# Or extract the project folder
```

### 2. Backend Setup

```bash
cd backend

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Place your dataset
# Copy Gen_AI Dataset.xlsx to backend/data/ directory
# If you don't have it, the system will use fallback data

# Initialize system (builds FAISS index)
python scripts/initialize.py
```

### 3. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Create environment file (optional)
echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local
```

## Running the Application

### Start Backend

```bash
cd backend
python app.py
```

Or with uvicorn:
```bash
cd backend
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

### Start Frontend

Open a new terminal:

```bash
cd frontend
npm run dev
```

### Access the Application

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs (FastAPI auto-generated)

## Verification

### Test Backend

```bash
# Health check
curl http://localhost:8000/health

# Get recommendations
curl -X POST http://localhost:8000/recommend \
  -H "Content-Type: application/json" \
  -d '{"query": "Hiring for a Python developer"}'
```

### Test Frontend

1. Open http://localhost:3000
2. Enter a test query
3. Verify recommendations appear

## Generating Submission Files

```bash
cd backend

# Run evaluation (generates results.csv and submission.csv)
python -m utils.evaluator
```

Output files:
- `docs/results.csv` - Evaluation results
- `docs/submission.csv` - Submission file for unlabeled queries

## Directory Structure After Setup

```
shl-assessment-recommender/
├── backend/
│   ├── data/
│   │   └── Gen_AI Dataset.xlsx  # Your dataset
│   ├── vectorstore/
│   │   ├── faiss_index.bin      # Generated index
│   │   └── assessment_data.pkl  # Generated data
│   └── ...
├── frontend/
│   ├── node_modules/            # After npm install
│   └── ...
└── docs/
    ├── results.csv              # After evaluation
    └── submission.csv           # After evaluation
```

## Common Issues

### Python Import Errors

```bash
# Make sure you're in the backend directory
cd backend
python -m utils.preprocess
```

### Node Module Errors

```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

### Port Conflicts

Change ports in:
- Backend: `app.py` or command line
- Frontend: `package.json` scripts or command line

### Dataset Not Found

The system will work with fallback data, but for best results:
1. Place `Gen_AI Dataset.xlsx` in `backend/data/`
2. Run `python scripts/initialize.py` again

## Production Deployment

See `docs/submission_instructions.md` for:
- Deploying to Render/Railway
- Deploying to Vercel
- Generating final submission files

## Support

For detailed information:
- `README.md` - Project overview
- `QUICKSTART.md` - Quick setup guide
- `docs/submission_instructions.md` - Deployment guide
- `docs/approach_report.md` - Technical approach

