# Deployment Quick Start - 5 Minute Guide

## 🚀 Fast Deployment Steps

### Step 1: Push to GitHub (2 min)

```powershell
cd "D:\SHL Assesment"
git init
git add .
git commit -m "Deploy SHL Assessment System"
git remote add origin https://github.com/YOUR_USERNAME/shl-assessment-recommender.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy Backend - Render (3 min)

1. Go to: https://render.com → Sign up with GitHub
2. Click "New +" → "Web Service"
3. Connect your GitHub repo: `shl-assessment-recommender`
4. Configure:
   - **Name**: `shl-api`
   - **Root Directory**: `backend` ⚠️
   - **Build Command**: `pip install -r requirements.txt && python -m utils.preprocess`
   - **Start Command**: `uvicorn app:app --host 0.0.0.0 --port $PORT`
5. Click "Create Web Service"
6. **Wait 5-10 min**, then **copy your URL**: `https://YOUR-API.onrender.com`

### Step 3: Deploy Frontend - Vercel (2 min)

1. Go to: https://vercel.com → Sign up with GitHub
2. Click "Add New..." → "Project"
3. Import your repo: `shl-assessment-recommender`
4. Configure:
   - **Root Directory**: `frontend` ⚠️
   - **Environment Variable**: 
     - Name: `NEXT_PUBLIC_API_URL`
     - Value: `https://YOUR-API.onrender.com` (from Step 2)
5. Click "Deploy"
6. **Wait 2-5 min**, then **copy your URL**: `https://YOUR-APP.vercel.app`

### Step 4: Test (1 min)

1. Open: `https://YOUR-APP.vercel.app`
2. Enter a query
3. Get recommendations! ✅

---

## 📝 Important Notes

- **Backend Root**: Must be `backend` (not root)
- **Frontend Root**: Must be `frontend` (not root)
- **Environment Variable**: Must be set in Vercel
- **First Request**: May be slow (30-60 sec) on free tier

---

## 🔗 Your Deployment URLs

- **Backend**: `https://____________________.onrender.com`
- **Frontend**: `https://____________________.vercel.app`
- **GitHub**: `https://github.com/YOUR_USERNAME/shl-assessment-recommender`

---

**Done! Your system is live! 🎉**

For detailed instructions, see `DEPLOYMENT_GUIDE.md`

