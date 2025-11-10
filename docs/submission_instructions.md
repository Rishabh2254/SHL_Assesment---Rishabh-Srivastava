# Submission Instructions

This document provides step-by-step instructions for deploying the SHL Assessment Recommendation System and preparing your submission.

## Prerequisites

- GitHub account
- Render account (for backend) - [https://render.com](https://render.com)
- Vercel account (for frontend) - [https://vercel.com](https://vercel.com)
- Python 3.10+ installed locally
- Node.js 18+ installed locally

---

## Step 1: Prepare Your Repository

1. **Initialize Git Repository** (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit: SHL Assessment Recommendation System"
   ```

2. **Create GitHub Repository**:
   - Go to [GitHub](https://github.com) and create a new repository
   - Name it: `shl-assessment-recommender`
   - Make it public (or private with sharing enabled)

3. **Push to GitHub**:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/shl-assessment-recommender.git
   git branch -M main
   git push -u origin main
   ```

---

## Step 2: Deploy Backend API (Render)

### Option A: Render (Recommended - Free Tier Available)

1. **Sign up/Login** to [Render](https://render.com)

2. **Create New Web Service**:
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select the repository: `shl-assessment-recommender`

3. **Configure Service**:
   - **Name**: `shl-recommender-api`
   - **Environment**: `Python 3`
   - **Build Command**: 
     ```bash
     cd backend && pip install -r requirements.txt && python -m utils.preprocess
     ```
   - **Start Command**: 
     ```bash
     cd backend && uvicorn app:app --host 0.0.0.0 --port $PORT
     ```
   - **Root Directory**: Leave empty (or set to `backend` if needed)

4. **Environment Variables** (if needed):
   - `PORT`: Will be set automatically by Render
   - Add any other required variables

5. **Deploy**:
   - Click "Create Web Service"
   - Wait for deployment to complete (5-10 minutes)
   - Note your service URL: `https://shl-recommender-api.onrender.com`

6. **Test the API**:
   ```bash
   curl https://YOUR_SERVICE_URL.onrender.com/health
   ```

### Option B: Railway

1. Sign up at [Railway](https://railway.app)
2. Create new project from GitHub repo
3. Add Python service
4. Set root directory to `backend`
5. Railway will auto-detect and deploy

### Option C: Hugging Face Spaces

1. Create a new Space at [Hugging Face Spaces](https://huggingface.co/spaces)
2. Select "Docker" SDK
3. Upload backend files
4. Configure Dockerfile (see below)

---

## Step 3: Deploy Frontend (Vercel)

1. **Sign up/Login** to [Vercel](https://vercel.com)

2. **Import Project**:
   - Click "Add New..." → "Project"
   - Import your GitHub repository
   - Select the repository: `shl-assessment-recommender`

3. **Configure Project**:
   - **Framework Preset**: Next.js
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build` (auto-detected)
   - **Output Directory**: `.next` (auto-detected)

4. **Environment Variables**:
   - Add: `NEXT_PUBLIC_API_URL` = `https://YOUR_BACKEND_URL.onrender.com`
   - Replace `YOUR_BACKEND_URL` with your actual backend URL from Step 2

5. **Deploy**:
   - Click "Deploy"
   - Wait for deployment (2-5 minutes)
   - Note your frontend URL: `https://your-project.vercel.app`

6. **Test the Frontend**:
   - Visit your Vercel URL
   - Try a sample query: "Hiring for a Python developer"

---

## Step 4: Generate Submission CSV

1. **Prepare Dataset**:
   - Place `Gen_AI Dataset.xlsx` in `backend/data/` directory

2. **Run Evaluation Script**:
   ```bash
   cd backend
   python -m utils.evaluator
   ```

3. **Generate Submission CSV**:
   The script will automatically:
   - Build the FAISS index (if not already built)
   - Evaluate on labeled data (compute Recall@10)
   - Generate `docs/submission.csv` for unlabeled test queries

4. **Verify CSV Format**:
   ```csv
   Query,Assessment_url
   Query1,https://www.shl.com/...
   Query1,https://www.shl.com/...
   Query2,https://www.shl.com/...
   ```

---

## Step 5: Create Approach Report

1. **Open** `docs/approach_report.md`
2. **Fill in** the details based on your implementation
3. **Export** as PDF (2 pages maximum)

The report should include:
- Overview of the system
- Data preprocessing approach
- Embedding generation method
- Vector search implementation
- Evaluation metrics and results
- Technology stack
- Future improvements

---

## Step 6: Final Checklist

Before submission, verify:

- [ ] Backend API is deployed and accessible
- [ ] `/health` endpoint returns `{"status": "running"}`
- [ ] `/recommend` endpoint accepts queries and returns recommendations
- [ ] Frontend is deployed and accessible
- [ ] Frontend can connect to backend API
- [ ] GitHub repository is public or shareable
- [ ] `submission.csv` is generated with correct format
- [ ] `approach_report.md` is completed (2 pages)
- [ ] All URLs are working

---

## Step 7: Submission

Submit the following:

1. **API Endpoint URL**: `https://your-api.onrender.com`
2. **Frontend URL**: `https://your-project.vercel.app`
3. **GitHub Repository**: `https://github.com/YOUR_USERNAME/shl-assessment-recommender`
4. **CSV File**: `docs/submission.csv`
5. **Approach Report**: `docs/approach_report.md` (as PDF)

---

## Troubleshooting

### Backend Issues

- **Build fails**: Check that all dependencies are in `requirements.txt`
- **Index not found**: Run `python -m utils.preprocess` locally first
- **CORS errors**: Ensure CORS middleware is configured in `app.py`

### Frontend Issues

- **API connection fails**: Check `NEXT_PUBLIC_API_URL` environment variable
- **Build fails**: Ensure all dependencies are in `package.json`
- **Styling issues**: Verify TailwindCSS is properly configured

### General Issues

- **Dataset not found**: Ensure `Gen_AI Dataset.xlsx` is in `backend/data/`
- **Low recall scores**: Try different embedding models or fine-tuning
- **Slow responses**: Consider caching or optimizing FAISS index

---

## Support

For issues or questions:
1. Check the README files in `backend/` and `frontend/`
2. Review error logs in Render/Vercel dashboards
3. Test locally first before deploying

---

## Additional Notes

- **Free Tier Limits**: Render free tier may spin down after inactivity. Consider upgrading for production use.
- **API Rate Limits**: Implement rate limiting if needed
- **Security**: Add authentication for production deployments
- **Monitoring**: Set up logging and monitoring for production

Good luck with your submission! 🚀

