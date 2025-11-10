# Deployment Checklist - Tick Off as You Go ✅

## Pre-Deployment

- [ ] Backend works locally (http://localhost:8000)
- [ ] Frontend works locally (http://localhost:3000)
- [ ] All code is committed to Git
- [ ] GitHub account created
- [ ] Render account created
- [ ] Vercel account created

---

## Step 1: GitHub Setup

- [ ] Git repository initialized
- [ ] All files added and committed
- [ ] GitHub repository created
- [ ] Code pushed to GitHub
- [ ] Verified files are on GitHub

**GitHub URL**: `https://github.com/____________________/shl-assessment-recommender`

---

## Step 2: Backend Deployment (Render)

### Configuration
- [ ] Logged into Render
- [ ] Created new Web Service
- [ ] Connected GitHub repository
- [ ] Set **Root Directory**: `backend` ⚠️
- [ ] Set **Build Command**: `pip install -r requirements.txt && python -m utils.preprocess`
- [ ] Set **Start Command**: `uvicorn app:app --host 0.0.0.0 --port $PORT`
- [ ] Selected Free tier
- [ ] Clicked "Create Web Service"

### Deployment
- [ ] Build started
- [ ] Build completed successfully
- [ ] Service is live
- [ ] Copied backend URL

**Backend URL**: `https://____________________.onrender.com`

### Testing
- [ ] Health endpoint works: `/health`
- [ ] Recommendation endpoint works: `/recommend`
- [ ] No errors in logs

---

## Step 3: Frontend Deployment (Vercel)

### Configuration
- [ ] Logged into Vercel
- [ ] Imported GitHub repository
- [ ] Set **Root Directory**: `frontend` ⚠️
- [ ] Framework auto-detected: Next.js
- [ ] Build settings verified

### Environment Variables
- [ ] Added `NEXT_PUBLIC_API_URL`
- [ ] Set value to backend URL: `https://____________________.onrender.com`
- [ ] Applied to all environments

### Deployment
- [ ] Clicked "Deploy"
- [ ] Build started
- [ ] Build completed successfully
- [ ] Frontend is live
- [ ] Copied frontend URL

**Frontend URL**: `https://____________________.vercel.app`

---

## Step 4: Link Frontend to Backend

- [ ] Environment variable set correctly
- [ ] Frontend redeployed (if needed)
- [ ] Frontend can connect to backend
- [ ] No CORS errors
- [ ] No connection errors

---

## Step 5: Final Testing

### Backend Tests
- [ ] `https://YOUR-BACKEND.onrender.com/health` → `{"status":"running"}`
- [ ] Backend responds to POST requests
- [ ] Recommendations are returned

### Frontend Tests
- [ ] Frontend page loads
- [ ] Search input works
- [ ] "Get Recommendations" button works
- [ ] Recommendations appear (5-10 items)
- [ ] Assessment URLs are clickable
- [ ] Dark mode toggle works
- [ ] No console errors (F12)

### End-to-End Test
- [ ] Entered test query
- [ ] Got recommendations
- [ ] All features working

---

## Final Verification

- [ ] Both URLs are accessible
- [ ] System works end-to-end
- [ ] No errors in browser console
- [ ] No errors in deployment logs
- [ ] Ready for submission!

---

## Your Deployment URLs

**Backend**: `https://____________________.onrender.com`  
**Frontend**: `https://____________________.vercel.app`  
**GitHub**: `https://github.com/____________________/shl-assessment-recommender`

---

## Common Issues Checklist

If something doesn't work, check:

- [ ] Root directory is correct (`backend` for backend, `frontend` for frontend)
- [ ] Environment variable is set in Vercel
- [ ] Backend URL uses `https://` (not `http://`)
- [ ] Backend is not sleeping (first request may be slow)
- [ ] No typos in URLs
- [ ] CORS is enabled in backend (already done)

---

**Status**: ⬜ Not Started | 🟡 In Progress | ✅ Complete

---

*Print this page or keep it open while deploying!*

