# Complete Step-by-Step Guide for SHL Assessment Recommendation System

This guide will walk you through every step needed to set up, test, evaluate, and deploy your system.

---

## 📋 Table of Contents

1. [Prerequisites Check](#1-prerequisites-check)
2. [Initial Setup](#2-initial-setup)
3. [Dataset Preparation](#3-dataset-preparation)
4. [Backend Setup & Initialization](#4-backend-setup--initialization)
5. [Frontend Setup](#5-frontend-setup)
6. [Local Testing](#6-local-testing)
7. [Evaluation & Submission Files](#7-evaluation--submission-files)
8. [Deployment - Backend](#8-deployment---backend)
9. [Deployment - Frontend](#9-deployment---frontend)
10. [Final Verification](#10-final-verification)
11. [Submission Preparation](#11-submission-preparation)

---

## 1. Prerequisites Check

### Check Python Installation

Open your terminal/command prompt and run:

```bash
python --version
```

**Expected Output**: Python 3.10 or higher (e.g., `Python 3.10.8`)

**If Python is not installed**:
- Download from: https://www.python.org/downloads/
- During installation, check "Add Python to PATH"
- Restart terminal after installation

### Check Node.js Installation

```bash
node --version
```

**Expected Output**: Node.js 18 or higher (e.g., `v18.17.0`)

**If Node.js is not installed**:
- Download from: https://nodejs.org/
- Install the LTS version
- Restart terminal after installation

### Check npm (comes with Node.js)

```bash
npm --version
```

**Expected Output**: npm version number (e.g., `9.6.7`)

### Verify You Have the Dataset

- Locate `Gen_AI Dataset.xlsx` file
- Note its location (you'll need to copy it later)

---

## 2. Initial Setup

### Step 2.1: Navigate to Project Directory

```bash
# Open terminal/command prompt
# Navigate to your project folder
cd "D:\SHL Assesment"
```

**Verify you're in the right place**:
```bash
# You should see these folders:
dir
# Should show: backend, frontend, docs folders
```

### Step 2.2: Verify Project Structure

You should have this structure:
```
SHL Assesment/
├── backend/
├── frontend/
├── docs/
├── README.md
└── ...
```

If anything is missing, check that all files were created properly.

---

## 3. Dataset Preparation

### Step 3.1: Locate Your Dataset File

Find your `Gen_AI Dataset.xlsx` file on your computer.

### Step 3.2: Copy Dataset to Backend

**Option A: Using File Explorer (Windows)**
1. Open File Explorer
2. Navigate to: `D:\SHL Assesment\backend\data\`
3. Copy `Gen_AI Dataset.xlsx` into this folder

**Option B: Using Command Line**
```bash
# Replace "C:\path\to\your\file.xlsx" with actual path
copy "C:\path\to\your\Gen_AI Dataset.xlsx" "backend\data\Gen_AI Dataset.xlsx"
```

### Step 3.3: Verify Dataset is in Place

```bash
dir backend\data
```

You should see `Gen_AI Dataset.xlsx` listed.

**Note**: If you don't have the dataset, the system will use fallback data, but results may not be optimal.

---

## 4. Backend Setup & Initialization

### Step 4.1: Navigate to Backend Directory

```bash
cd backend
```

### Step 4.2: Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**You should see `(venv)` in your terminal prompt**

### Step 4.3: Install Python Dependencies

```bash
pip install -r requirements.txt
```

**This will take 3-5 minutes**. You'll see packages being downloaded and installed.

**Expected output**: 
```
Successfully installed fastapi-0.104.1 uvicorn-0.24.0 ...
```

**If you get errors**:
- Make sure you're in the `backend` directory
- Make sure virtual environment is activated
- Try: `pip install --upgrade pip` first

### Step 4.4: Initialize the System

This step builds the FAISS index and prepares the system. **This will take 5-10 minutes** (downloads the embedding model).

```bash
python scripts/initialize.py
```

**What this does**:
1. Downloads Sentence-BERT model (first time only)
2. Crawls/scrapes SHL catalog (or uses fallback data)
3. Generates embeddings for all assessments
4. Builds FAISS vector index
5. Runs evaluation on labeled data
6. Generates submission CSV

**Expected output**:
```
============================================================
SHL Assessment Recommendation System - Initialization
============================================================

[Step 1/3] Building FAISS index...
Building FAISS index...
Generating embeddings...
FAISS index saved to ...
✓ FAISS index built successfully

[Step 2/3] Evaluating on labeled data...
Starting evaluation...
✓ Evaluation complete. Mean Recall@10: 0.XXXX

[Step 3/3] Generating submission CSV...
Generating submission CSV...
✓ Submission CSV generated

============================================================
Initialization complete! You can now start the API server.
============================================================
```

**If you see errors**:
- Check that dataset is in `backend/data/` folder
- Make sure all dependencies are installed
- Check error messages for specific issues

### Step 4.5: Verify Index Files Created

```bash
dir vectorstore
```

You should see:
- `faiss_index.bin` (the vector index)
- `assessment_data.pkl` (assessment metadata)

### Step 4.6: Start the Backend Server

**Keep this terminal window open!**

```bash
python app.py
```

**Expected output**:
```
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**The server is now running!** Don't close this terminal.

**If port 8000 is busy**:
- Change port in `app.py` or use: `uvicorn app:app --port 8001`

---

## 5. Frontend Setup

### Step 5.1: Open a NEW Terminal Window

**Important**: Keep the backend server running in the first terminal, open a new terminal for frontend.

### Step 5.2: Navigate to Frontend Directory

```bash
cd "D:\SHL Assesment\frontend"
```

### Step 5.3: Install Node Dependencies

```bash
npm install
```

**This will take 2-3 minutes**. You'll see packages being downloaded.

**Expected output**:
```
added 500+ packages, and audited 501 packages in 30s
```

**If you get errors**:
- Make sure Node.js is installed
- Try: `npm cache clean --force` then `npm install` again
- Check you're in the `frontend` directory

### Step 5.4: Create Environment File (Optional)

Create a file named `.env.local` in the `frontend` directory:

**Windows (Command Prompt)**:
```bash
echo NEXT_PUBLIC_API_URL=http://localhost:8000 > .env.local
```

**Windows (PowerShell)**:
```powershell
Set-Content -Path .env.local -Value "NEXT_PUBLIC_API_URL=http://localhost:8000"
```

**macOS/Linux**:
```bash
echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local
```

**Or manually create**:
1. Create new file: `.env.local`
2. Add this line: `NEXT_PUBLIC_API_URL=http://localhost:8000`
3. Save the file

### Step 5.5: Start Frontend Development Server

```bash
npm run dev
```

**Expected output**:
```
  ▲ Next.js 14.0.4
  - Local:        http://localhost:3000
  - Ready in 2.3s
```

**The frontend is now running!**

---

## 6. Local Testing

### Step 6.1: Test Backend API

**Open a third terminal** (or use browser/Postman)

**Test Health Endpoint**:
```bash
curl http://localhost:8000/health
```

**Expected response**:
```json
{"status":"running"}
```

**Or test in browser**: Open http://localhost:8000/health

**Test Recommendation Endpoint**:
```bash
curl -X POST http://localhost:8000/recommend -H "Content-Type: application/json" -d "{\"query\": \"Hiring for a Python developer\"}"
```

**Or use the test script**:
```bash
cd backend
python test_api.py
```

### Step 6.2: Test Frontend

1. **Open browser**: http://localhost:3000
2. **You should see**: The SHL Assessment Recommender interface
3. **Try a test query**: 
   - Enter: "Hiring for a Python developer with strong communication skills"
   - Click "Get Recommendations"
4. **Expected result**: Table showing 5-10 recommended assessments

### Step 6.3: Verify Everything Works

✅ Backend server running (terminal 1)
✅ Frontend server running (terminal 2)
✅ Health endpoint returns `{"status": "running"}`
✅ Frontend loads at http://localhost:3000
✅ Recommendations appear when you search

**If something doesn't work**:
- Check both terminals for error messages
- Verify backend is running on port 8000
- Verify frontend is running on port 3000
- Check browser console (F12) for errors

---

## 7. Evaluation & Submission Files

### Step 7.1: Run Evaluation (If Not Already Done)

If you already ran `python scripts/initialize.py`, this was done automatically. Otherwise:

**In backend terminal** (stop server with Ctrl+C first):
```bash
python -m utils.evaluator
```

**This will**:
- Compute Mean Recall@10 on labeled queries
- Generate `docs/results.csv` with evaluation results
- Generate `docs/submission.csv` for unlabeled test queries

### Step 7.2: Check Generated Files

```bash
# From project root
dir docs
```

You should see:
- `results.csv` - Evaluation results
- `submission.csv` - Submission file (this is what you'll submit)

### Step 7.3: Verify Submission CSV Format

Open `docs/submission.csv` in Excel or text editor. It should look like:

```csv
Query,Assessment_url
Query1,https://www.shl.com/...
Query1,https://www.shl.com/...
Query2,https://www.shl.com/...
```

**Each query should have 5-10 assessment URLs**

---

## 8. Deployment - Backend

### Step 8.1: Create GitHub Repository

1. **Go to GitHub**: https://github.com
2. **Sign in** (or create account)
3. **Click "New"** (green button) or go to: https://github.com/new
4. **Repository name**: `shl-assessment-recommender`
5. **Visibility**: Public (or Private with sharing enabled)
6. **Don't initialize** with README (you already have one)
7. **Click "Create repository"**

### Step 8.2: Push Code to GitHub

**In your project root directory** (new terminal):

```bash
cd "D:\SHL Assesment"

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: SHL Assessment Recommendation System"

# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/shl-assessment-recommender.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**If you get authentication errors**:
- Use GitHub Personal Access Token instead of password
- Or use GitHub Desktop app

### Step 8.3: Deploy to Render

1. **Go to Render**: https://render.com
2. **Sign up/Login** (can use GitHub account)
3. **Click "New +"** → **"Web Service"**
4. **Connect GitHub** (if not connected)
5. **Select repository**: `shl-assessment-recommender`
6. **Configure service**:
   - **Name**: `shl-recommender-api`
   - **Environment**: `Python 3`
   - **Region**: Choose closest to you
   - **Branch**: `main`
   - **Root Directory**: `backend` (important!)
   - **Build Command**: 
     ```bash
     pip install -r requirements.txt && python -m utils.preprocess
     ```
   - **Start Command**: 
     ```bash
     uvicorn app:app --host 0.0.0.0 --port $PORT
     ```
   - **Instance Type**: Free (or paid if needed)

7. **Environment Variables** (if needed):
   - `PORT`: Auto-set by Render
   - Add any others if required

8. **Click "Create Web Service"**

9. **Wait for deployment** (5-10 minutes):
   - Watch the logs
   - Wait for "Your service is live" message

10. **Note your URL**: `https://shl-recommender-api.onrender.com` (or similar)

### Step 8.4: Test Deployed Backend

```bash
curl https://YOUR_SERVICE_URL.onrender.com/health
```

**Expected**: `{"status":"running"}`

**Test recommendation**:
```bash
curl -X POST https://YOUR_SERVICE_URL.onrender.com/recommend \
  -H "Content-Type: application/json" \
  -d "{\"query\": \"Hiring for a Python developer\"}"
```

**Note**: First request may be slow (cold start on free tier)

---

## 9. Deployment - Frontend

### Step 9.1: Deploy to Vercel

1. **Go to Vercel**: https://vercel.com
2. **Sign up/Login** (can use GitHub account)
3. **Click "Add New..."** → **"Project"**
4. **Import Git Repository**:
   - Select `shl-assessment-recommender`
   - Click "Import"

5. **Configure Project**:
   - **Framework Preset**: Next.js (auto-detected)
   - **Root Directory**: `frontend` (change from default!)
   - **Build Command**: `npm run build` (auto-detected)
   - **Output Directory**: `.next` (auto-detected)
   - **Install Command**: `npm install` (auto-detected)

6. **Environment Variables**:
   - Click "Environment Variables"
   - Add new variable:
     - **Name**: `NEXT_PUBLIC_API_URL`
     - **Value**: `https://YOUR_BACKEND_URL.onrender.com` (from Step 8.3)
     - **Environment**: Production, Preview, Development (check all)

7. **Click "Deploy"**

8. **Wait for deployment** (2-5 minutes):
   - Watch build logs
   - Wait for "Ready" status

9. **Note your URL**: `https://your-project.vercel.app` (or custom domain)

### Step 9.2: Test Deployed Frontend

1. **Open your Vercel URL** in browser
2. **Test the interface**:
   - Enter a query
   - Click "Get Recommendations"
   - Verify recommendations appear

**If recommendations don't load**:
- Check browser console (F12) for errors
- Verify `NEXT_PUBLIC_API_URL` is set correctly in Vercel
- Check backend is accessible

---

## 10. Final Verification

### Step 10.1: Verify All Endpoints

✅ **Backend Health**: `https://your-api.onrender.com/health`
✅ **Backend Recommend**: Test with a query
✅ **Frontend**: Loads correctly
✅ **Frontend Search**: Returns recommendations
✅ **GitHub Repo**: Code is pushed and accessible

### Step 10.2: Test End-to-End Flow

1. Open deployed frontend URL
2. Enter query: "Hiring for a data analyst with SQL skills"
3. Click "Get Recommendations"
4. Verify 5-10 recommendations appear
5. Click on assessment URLs (should open in new tab)

### Step 10.3: Check Submission Files

```bash
# Verify files exist
dir docs\submission.csv
dir docs\results.csv
```

Open `docs/submission.csv` and verify:
- Has correct format (Query, Assessment_url)
- Each query has 5-10 URLs
- URLs are valid SHL assessment URLs

---

## 11. Submission Preparation

### Step 11.1: Complete Approach Report

1. **Open**: `docs/approach_report.md`
2. **Fill in**:
   - Your name
   - Date
   - Mean Recall@10 score (from evaluation)
   - Any customizations you made
   - Results summary

3. **Export as PDF**:
   - Open in Markdown editor or convert online
   - Export as PDF (2 pages maximum)
   - Save as: `approach_report.pdf`

### Step 11.2: Prepare Submission Package

You need to submit:

1. ✅ **API Endpoint URL**: `https://your-api.onrender.com`
2. ✅ **Frontend URL**: `https://your-project.vercel.app`
3. ✅ **GitHub Repository**: `https://github.com/YOUR_USERNAME/shl-assessment-recommender`
4. ✅ **CSV File**: `docs/submission.csv`
5. ✅ **Approach Report**: `docs/approach_report.pdf` (2 pages)

### Step 11.3: Final Checklist

Before submitting, verify:

- [ ] Backend API is deployed and accessible
- [ ] Frontend is deployed and accessible
- [ ] Both URLs work correctly
- [ ] GitHub repository is public (or shareable)
- [ ] `submission.csv` is generated and formatted correctly
- [ ] Approach report is completed (2 pages, PDF format)
- [ ] All code is pushed to GitHub
- [ ] Tested end-to-end flow works

### Step 11.4: Submission Format

Prepare your submission with:

```
Submission for SHL AI Research Intern Assessment

1. API Endpoint: https://your-api.onrender.com
2. Frontend URL: https://your-project.vercel.app
3. GitHub Repository: https://github.com/YOUR_USERNAME/shl-assessment-recommender
4. CSV File: [Attach submission.csv]
5. Approach Report: [Attach approach_report.pdf]
```

---

## 🆘 Troubleshooting Common Issues

### Issue: "Module not found" errors

**Solution**:
```bash
cd backend
pip install -r requirements.txt
```

### Issue: "Port already in use"

**Solution**: 
- Change port: `uvicorn app:app --port 8001`
- Or kill process using port 8000

### Issue: Frontend can't connect to backend

**Solution**:
- Check backend is running
- Verify `NEXT_PUBLIC_API_URL` in `.env.local`
- Check CORS settings in `backend/app.py`

### Issue: "Index not found" error

**Solution**:
```bash
cd backend
python scripts/initialize.py
```

### Issue: Deployment fails on Render

**Solution**:
- Check build logs for specific errors
- Verify `Root Directory` is set to `backend`
- Check build command is correct
- Ensure all dependencies in `requirements.txt`

### Issue: Deployment fails on Vercel

**Solution**:
- Check build logs
- Verify `Root Directory` is set to `frontend`
- Check environment variables are set
- Ensure `package.json` is correct

---

## 📞 Need Help?

1. **Check error messages** in terminal/logs
2. **Review documentation**:
   - `README.md` - Overview
   - `QUICKSTART.md` - Quick setup
   - `SETUP.md` - Detailed setup
3. **Verify all prerequisites** are installed
4. **Check file paths** are correct

---

## ✅ Success Criteria

You're ready to submit when:

✅ Backend API returns recommendations correctly
✅ Frontend displays recommendations in a table
✅ Both are deployed and accessible via URLs
✅ GitHub repository contains all code
✅ Submission CSV is generated with correct format
✅ Approach report is completed (2 pages)

---

**Good luck with your submission! 🚀**

If you encounter any issues at any step, refer back to the troubleshooting section or check the specific error messages for guidance.

