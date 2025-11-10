# Quick Checklist - SHL Assessment Recommendation System

Use this checklist to track your progress. Check off each item as you complete it.

## Phase 1: Setup & Installation

### Prerequisites
- [ ] Python 3.10+ installed (`python --version`)
- [ ] Node.js 18+ installed (`node --version`)
- [ ] npm installed (`npm --version`)
- [ ] `Gen_AI Dataset.xlsx` file located

### Initial Setup
- [ ] Navigated to project directory
- [ ] Verified project structure (backend, frontend, docs folders exist)
- [ ] Copied `Gen_AI Dataset.xlsx` to `backend/data/` folder

## Phase 2: Backend Setup

### Installation
- [ ] Navigated to `backend` directory
- [ ] Created virtual environment (optional but recommended)
- [ ] Activated virtual environment
- [ ] Installed dependencies (`pip install -r requirements.txt`)
- [ ] All packages installed successfully

### Initialization
- [ ] Ran initialization script (`python scripts/initialize.py`)
- [ ] FAISS index built successfully
- [ ] Evaluation completed (Mean Recall@10 computed)
- [ ] Submission CSV generated
- [ ] Verified `vectorstore/` folder has `faiss_index.bin` and `assessment_data.pkl`

### Server
- [ ] Started backend server (`python app.py`)
- [ ] Server running on http://localhost:8000
- [ ] Health endpoint works (`curl http://localhost:8000/health`)

## Phase 3: Frontend Setup

### Installation
- [ ] Opened new terminal window
- [ ] Navigated to `frontend` directory
- [ ] Installed dependencies (`npm install`)
- [ ] All packages installed successfully

### Configuration
- [ ] Created `.env.local` file (optional)
- [ ] Set `NEXT_PUBLIC_API_URL=http://localhost:8000`

### Server
- [ ] Started frontend server (`npm run dev`)
- [ ] Server running on http://localhost:3000
- [ ] Frontend loads in browser

## Phase 4: Local Testing

### Backend Testing
- [ ] Health endpoint returns `{"status": "running"}`
- [ ] Recommendation endpoint accepts queries
- [ ] Recommendations are returned correctly
- [ ] Test script passes (`python test_api.py`)

### Frontend Testing
- [ ] Frontend page loads correctly
- [ ] Search input field works
- [ ] "Get Recommendations" button works
- [ ] Recommendations table displays
- [ ] Assessment URLs are clickable
- [ ] Dark mode toggle works
- [ ] Loading animations appear
- [ ] Error messages display correctly

### End-to-End Testing
- [ ] Entered test query: "Hiring for a Python developer"
- [ ] Received 5-10 recommendations
- [ ] Recommendations are relevant
- [ ] URLs open correctly

## Phase 5: Evaluation

### Files Generated
- [ ] `docs/results.csv` exists
- [ ] `docs/submission.csv` exists
- [ ] Submission CSV has correct format (Query, Assessment_url)
- [ ] Each query has 5-10 assessment URLs
- [ ] Mean Recall@10 score recorded

## Phase 6: GitHub Setup

### Repository
- [ ] Created GitHub account (if needed)
- [ ] Created new repository: `shl-assessment-recommender`
- [ ] Repository is public (or private with sharing enabled)

### Code Push
- [ ] Initialized git (`git init`)
- [ ] Added all files (`git add .`)
- [ ] Committed changes (`git commit -m "..."`)
- [ ] Added remote origin
- [ ] Pushed to GitHub (`git push -u origin main`)
- [ ] Verified code is on GitHub

## Phase 7: Backend Deployment (Render)

### Render Setup
- [ ] Created Render account (or logged in)
- [ ] Connected GitHub account to Render

### Service Configuration
- [ ] Created new Web Service
- [ ] Selected repository: `shl-assessment-recommender`
- [ ] Set Environment: Python 3
- [ ] Set Root Directory: `backend`
- [ ] Set Build Command: `pip install -r requirements.txt && python -m utils.preprocess`
- [ ] Set Start Command: `uvicorn app:app --host 0.0.0.0 --port $PORT`
- [ ] Configured environment variables (if needed)

### Deployment
- [ ] Clicked "Create Web Service"
- [ ] Deployment started
- [ ] Build completed successfully
- [ ] Service is live
- [ ] Noted backend URL: `https://your-api.onrender.com`

### Testing Deployed Backend
- [ ] Health endpoint works: `https://your-api.onrender.com/health`
- [ ] Recommendation endpoint works
- [ ] CORS is configured correctly

## Phase 8: Frontend Deployment (Vercel)

### Vercel Setup
- [ ] Created Vercel account (or logged in)
- [ ] Connected GitHub account to Vercel

### Project Configuration
- [ ] Imported repository: `shl-assessment-recommender`
- [ ] Set Framework Preset: Next.js
- [ ] Set Root Directory: `frontend`
- [ ] Build settings auto-detected correctly

### Environment Variables
- [ ] Added `NEXT_PUBLIC_API_URL`
- [ ] Set value to backend URL: `https://your-api.onrender.com`
- [ ] Applied to all environments (Production, Preview, Development)

### Deployment
- [ ] Clicked "Deploy"
- [ ] Build completed successfully
- [ ] Deployment is live
- [ ] Noted frontend URL: `https://your-project.vercel.app`

### Testing Deployed Frontend
- [ ] Frontend loads correctly
- [ ] Can enter queries
- [ ] Recommendations load from deployed backend
- [ ] All features work correctly

## Phase 9: Final Verification

### URLs Working
- [ ] Backend URL accessible
- [ ] Frontend URL accessible
- [ ] GitHub repository accessible
- [ ] All links work correctly

### Functionality
- [ ] End-to-end flow works on deployed version
- [ ] Recommendations are returned
- [ ] No console errors
- [ ] Performance is acceptable

### Files Ready
- [ ] `docs/submission.csv` is correct
- [ ] `docs/approach_report.md` is completed
- [ ] Approach report exported as PDF (2 pages)
- [ ] All files are in correct format

## Phase 10: Submission Preparation

### Documentation
- [ ] Approach report completed with:
  - [ ] Overview
  - [ ] Data preprocessing
  - [ ] Embedding generation
  - [ ] Evaluation results
  - [ ] Technology stack
  - [ ] Results summary
- [ ] Report is 2 pages maximum
- [ ] Report exported as PDF

### Submission Package
- [ ] API Endpoint URL noted
- [ ] Frontend URL noted
- [ ] GitHub Repository URL noted
- [ ] Submission CSV file ready
- [ ] Approach report PDF ready

### Final Check
- [ ] All URLs are working
- [ ] Code is on GitHub
- [ ] CSV file is formatted correctly
- [ ] Report is complete
- [ ] Ready to submit!

---

## Quick Command Reference

### Backend
```bash
cd backend
pip install -r requirements.txt
python scripts/initialize.py
python app.py
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Testing
```bash
# Backend health check
curl http://localhost:8000/health

# Backend recommendation
curl -X POST http://localhost:8000/recommend -H "Content-Type: application/json" -d "{\"query\": \"test\"}"

# Run test script
cd backend
python test_api.py
```

### Evaluation
```bash
cd backend
python -m utils.evaluator
```

---

## Important URLs to Note

- **Local Backend**: http://localhost:8000
- **Local Frontend**: http://localhost:3000
- **Deployed Backend**: https://____________________
- **Deployed Frontend**: https://____________________
- **GitHub Repo**: https://github.com/____________________

---

**Progress**: ___ / 100+ items completed

**Status**: ⬜ Not Started | 🟡 In Progress | ✅ Complete

---

*Keep this checklist open while working through the steps!*

