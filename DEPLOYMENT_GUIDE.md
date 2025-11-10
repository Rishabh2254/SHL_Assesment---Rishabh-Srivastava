# Complete Deployment Guide - SHL Assessment Recommendation System

This guide will walk you through deploying both frontend and backend to production.

---

## 📋 Table of Contents

1. [Prerequisites](#1-prerequisites)
2. [Step 1: Prepare GitHub Repository](#2-step-1-prepare-github-repository)
3. [Step 2: Deploy Backend (Render)](#3-step-2-deploy-backend-render)
4. [Step 3: Deploy Frontend (Vercel)](#4-step-3-deploy-frontend-vercel)
5. [Step 4: Link Frontend to Backend](#5-step-4-link-frontend-to-backend)
6. [Step 5: Test Deployed System](#6-step-5-test-deployed-system)
7. [Troubleshooting](#7-troubleshooting)

---

## 1. Prerequisites

Before starting, ensure you have:

- ✅ GitHub account (free) - [Sign up](https://github.com/signup)
- ✅ Render account (free tier available) - [Sign up](https://render.com)
- ✅ Vercel account (free tier available) - [Sign up](https://vercel.com)
- ✅ Your code is working locally (backend + frontend)
- ✅ All files committed to Git

---

## 2. Step 1: Prepare GitHub Repository

### 2.1: Initialize Git (if not done)

```powershell
# Navigate to project root
cd "D:\SHL Assesment"

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: SHL Assessment Recommendation System"
```

### 2.2: Create GitHub Repository

1. **Go to GitHub**: https://github.com
2. **Click** the **"+" icon** (top right) → **"New repository"**
3. **Repository settings**:
   - **Name**: `shl-assessment-recommender`
   - **Description**: "AI-powered recommendation system for SHL assessments"
   - **Visibility**: **Public** (or Private - your choice)
   - **DO NOT** check "Initialize with README" (you already have files)
4. **Click "Create repository"**

### 2.3: Push Code to GitHub

**Option A: Using HTTPS (Recommended for beginners)**

```powershell
# From project root
cd "D:\SHL Assesment"

# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/shl-assessment-recommender.git

# Rename branch to main
git branch -M main

# Push code
git push -u origin main
```

**If you get authentication error:**
- GitHub no longer accepts passwords
- Use **Personal Access Token** instead:
  1. Go to: https://github.com/settings/tokens
  2. Click "Generate new token (classic)"
  3. Name: "Deployment Token"
  4. Select scopes: `repo` (full control)
  5. Generate and **copy the token**
  6. When prompted for password, paste the **token** instead

**Option B: Using GitHub Desktop (Easier)**

1. Download: https://desktop.github.com/
2. Install and sign in
3. File → Add Local Repository
4. Select: `D:\SHL Assesment`
5. Click "Publish repository"
6. Choose name and visibility
7. Click "Publish"

### 2.4: Verify Repository

- Go to: `https://github.com/YOUR_USERNAME/shl-assessment-recommender`
- Verify all files are there (backend/, frontend/, docs/, etc.)

---

## 3. Step 2: Deploy Backend (Render)

### 3.1: Sign Up / Login to Render

1. **Go to**: https://render.com
2. **Click "Get Started for Free"** or **"Sign In"**
3. **Sign up with GitHub** (recommended - easier integration)

### 3.2: Create New Web Service

1. **Click "New +"** (top right)
2. **Select "Web Service"**

### 3.3: Connect GitHub Repository

1. **Click "Connect account"** (if not connected)
2. **Authorize Render** to access your GitHub
3. **Select repository**: `shl-assessment-recommender`
4. **Click "Connect"**

### 3.4: Configure Backend Service

Fill in the following settings:

#### Basic Settings:
- **Name**: `shl-recommender-api` (or any name you like)
- **Region**: Choose closest to you (e.g., "Oregon (US West)")
- **Branch**: `main` (or `master` if that's your branch)
- **Root Directory**: `backend` ⚠️ **IMPORTANT!**

#### Build & Deploy:
- **Environment**: `Python 3`
- **Build Command**: 
  ```bash
  pip install -r requirements.txt && python -m utils.preprocess
  ```
- **Start Command**: 
  ```bash
  uvicorn app:app --host 0.0.0.0 --port $PORT
  ```

#### Instance Type:
- **Free**: Select "Free" tier (512 MB RAM)
- **Note**: Free tier spins down after 15 min inactivity (first request will be slow)

#### Advanced Settings (Optional):
- **Auto-Deploy**: `Yes` (deploys automatically on git push)
- **Health Check Path**: `/health`

### 3.5: Environment Variables (Optional)

Click "Advanced" → "Add Environment Variable" if needed:
- `PORT`: Auto-set by Render (don't add manually)
- Add any other variables if your code requires them

### 3.6: Deploy

1. **Click "Create Web Service"**
2. **Wait for deployment** (5-10 minutes):
   - Watch the build logs
   - First deployment takes longer (installing packages, building index)
   - You'll see: "Your service is live at..."

### 3.7: Get Your Backend URL

Once deployed, you'll see:
- **Service URL**: `https://shl-recommender-api.onrender.com` (or similar)
- **Copy this URL** - you'll need it for frontend!

### 3.8: Test Backend

```powershell
# Test health endpoint
curl https://YOUR_SERVICE_NAME.onrender.com/health

# Should return: {"status":"running"}
```

**Or test in browser**: `https://YOUR_SERVICE_NAME.onrender.com/health`

**Note**: First request may take 30-60 seconds (cold start on free tier)

---

## 4. Step 3: Deploy Frontend (Vercel)

### 4.1: Sign Up / Login to Vercel

1. **Go to**: https://vercel.com
2. **Click "Sign Up"** or **"Log In"**
3. **Sign up with GitHub** (recommended)

### 4.2: Import Project

1. **Click "Add New..."** → **"Project"**
2. **Import Git Repository**:
   - Find `shl-assessment-recommender`
   - Click **"Import"**

### 4.3: Configure Project

#### Project Settings:
- **Project Name**: `shl-recommender-frontend` (or any name)
- **Framework Preset**: `Next.js` (auto-detected)
- **Root Directory**: `frontend` ⚠️ **IMPORTANT!**
  - Click "Edit" next to Root Directory
  - Change from `/` to `/frontend`
  - Click "Continue"

#### Build Settings:
- **Build Command**: `npm run build` (auto-detected)
- **Output Directory**: `.next` (auto-detected)
- **Install Command**: `npm install` (auto-detected)

### 4.4: Environment Variables

**BEFORE clicking Deploy**, add environment variable:

1. **Click "Environment Variables"**
2. **Add new variable**:
   - **Name**: `NEXT_PUBLIC_API_URL`
   - **Value**: `https://YOUR_BACKEND_URL.onrender.com`
     - Replace `YOUR_BACKEND_URL` with your actual Render backend URL from Step 3.7
   - **Environment**: Check all (Production, Preview, Development)
3. **Click "Save"**

**Example**:
```
NEXT_PUBLIC_API_URL = https://shl-recommender-api.onrender.com
```

### 4.5: Deploy

1. **Click "Deploy"**
2. **Wait for deployment** (2-5 minutes):
   - Watch build logs
   - Wait for "Ready" status

### 4.6: Get Your Frontend URL

Once deployed:
- **Production URL**: `https://shl-recommender-frontend.vercel.app` (or similar)
- **Copy this URL**

### 4.7: Test Frontend

1. **Open your Vercel URL** in browser
2. **You should see**: The SHL Assessment Recommender interface
3. **Try a search**: Enter a query and test recommendations

---

## 5. Step 4: Link Frontend to Backend

### 5.1: Verify Environment Variable

The frontend should already be linked (you set `NEXT_PUBLIC_API_URL` in Step 4.4).

**To verify/update**:

1. Go to Vercel dashboard
2. Select your project
3. Go to **Settings** → **Environment Variables**
4. Verify `NEXT_PUBLIC_API_URL` is set correctly
5. If wrong, update it and **redeploy**

### 5.2: Redeploy if Needed

If you changed environment variables:

1. Go to **Deployments** tab
2. Click **"..."** (three dots) on latest deployment
3. Click **"Redeploy"**

### 5.3: Test the Connection

1. **Open your Vercel frontend URL**
2. **Open browser DevTools** (F12)
3. **Go to Console tab**
4. **Enter a query** and click "Get Recommendations"
5. **Check for errors**:
   - ✅ No errors = Working!
   - ❌ CORS errors = Backend CORS needs fixing
   - ❌ Connection errors = Check backend URL

---

## 6. Step 5: Test Deployed System

### 6.1: Test Backend

```powershell
# Health check
curl https://YOUR_BACKEND.onrender.com/health

# Recommendation test
curl -X POST https://YOUR_BACKEND.onrender.com/recommend `
  -H "Content-Type: application/json" `
  -d '{\"query\": \"Hiring for a Python developer\"}'
```

### 6.2: Test Frontend

1. **Open**: `https://YOUR_FRONTEND.vercel.app`
2. **Test features**:
   - ✅ Page loads
   - ✅ Search input works
   - ✅ Recommendations appear
   - ✅ URLs are clickable
   - ✅ Dark mode works

### 6.3: End-to-End Test

1. **Enter query**: "Hiring for a data analyst with SQL skills"
2. **Click "Get Recommendations"**
3. **Verify**: 5-10 recommendations appear
4. **Click on assessment URLs**: Should open in new tab

---

## 7. Troubleshooting

### Issue: Backend Deployment Fails

**Problem**: Build command fails

**Solution**:
1. Check build logs in Render dashboard
2. Common issues:
   - Missing dependencies → Check `requirements.txt`
   - Wrong root directory → Should be `backend`
   - Python version → Render auto-detects, but check logs
3. Fix and redeploy

**Problem**: "Index not found" error

**Solution**:
- The build command should run `python -m utils.preprocess`
- Check build logs to verify it ran
- If not, manually add to build command

### Issue: Frontend Deployment Fails

**Problem**: Build fails

**Solution**:
1. Check build logs in Vercel
2. Common issues:
   - Wrong root directory → Should be `frontend`
   - Missing dependencies → Check `package.json`
   - TypeScript errors → Fix code errors
3. Fix and redeploy

### Issue: Frontend Can't Connect to Backend

**Problem**: CORS errors or connection refused

**Solutions**:

1. **Check Environment Variable**:
   - Vercel → Settings → Environment Variables
   - Verify `NEXT_PUBLIC_API_URL` is correct
   - Must start with `https://` (not `http://`)

2. **Check Backend CORS**:
   - Backend already has CORS configured
   - If still issues, check `backend/app.py`:
   ```python
   allow_origins=["*"]  # Should allow all origins
   ```

3. **Check Backend is Running**:
   - Test: `https://YOUR_BACKEND.onrender.com/health`
   - If not responding, backend may be sleeping (free tier)
   - First request after sleep takes 30-60 seconds

4. **Redeploy Frontend**:
   - After changing environment variables, redeploy

### Issue: Backend Takes Too Long to Respond

**Problem**: First request is very slow (30-60 seconds)

**Solution**:
- This is normal on Render free tier (spins down after inactivity)
- Options:
  1. Wait for first request (wakes up the service)
  2. Upgrade to paid tier (always on)
  3. Use a service that doesn't sleep (Railway, Fly.io)

### Issue: Recommendations Not Appearing

**Problem**: Frontend loads but no recommendations

**Solutions**:

1. **Check Browser Console** (F12):
   - Look for errors
   - Check network tab for API calls

2. **Verify Backend URL**:
   - Check environment variable is correct
   - Test backend directly in browser

3. **Check Backend Logs**:
   - Render dashboard → Logs
   - Look for errors

---

## 8. Quick Reference

### Backend (Render)
- **URL**: `https://YOUR_SERVICE.onrender.com`
- **Root Directory**: `backend`
- **Build Command**: `pip install -r requirements.txt && python -m utils.preprocess`
- **Start Command**: `uvicorn app:app --host 0.0.0.0 --port $PORT`

### Frontend (Vercel)
- **URL**: `https://YOUR_PROJECT.vercel.app`
- **Root Directory**: `frontend`
- **Environment Variable**: `NEXT_PUBLIC_API_URL` = your Render backend URL

### Testing URLs
- **Backend Health**: `https://YOUR_BACKEND.onrender.com/health`
- **Frontend**: `https://YOUR_FRONTEND.vercel.app`

---

## 9. Final Checklist

Before considering deployment complete:

- [ ] Backend deployed and accessible
- [ ] Backend `/health` endpoint works
- [ ] Backend `/recommend` endpoint works
- [ ] Frontend deployed and accessible
- [ ] Frontend loads correctly
- [ ] Environment variable `NEXT_PUBLIC_API_URL` is set
- [ ] Frontend can connect to backend
- [ ] Recommendations appear when searching
- [ ] All features work (dark mode, etc.)
- [ ] No console errors in browser

---

## 10. Alternative Deployment Options

### Backend Alternatives:

1. **Railway** (https://railway.app)
   - Similar to Render
   - Free tier available
   - Auto-detects Python projects

2. **Fly.io** (https://fly.io)
   - Free tier
   - Always-on option

3. **Heroku** (https://heroku.com)
   - Paid (no free tier anymore)
   - Easy deployment

### Frontend Alternatives:

1. **Netlify** (https://netlify.com)
   - Free tier
   - Similar to Vercel
   - Good for Next.js

2. **GitHub Pages**
   - Free
   - Requires static export (not ideal for Next.js)

---

## 11. Summary

**Deployment Flow**:
1. ✅ Push code to GitHub
2. ✅ Deploy backend to Render
3. ✅ Get backend URL
4. ✅ Deploy frontend to Vercel
5. ✅ Set environment variable (backend URL)
6. ✅ Test everything

**Your URLs**:
- **Backend**: `https://____________________.onrender.com`
- **Frontend**: `https://____________________.vercel.app`
- **GitHub**: `https://github.com/YOUR_USERNAME/shl-assessment-recommender`

---

**You're all set! Your system is now deployed and accessible worldwide! 🌍**

If you encounter any issues, refer to the Troubleshooting section or check the deployment logs in Render/Vercel dashboards.

