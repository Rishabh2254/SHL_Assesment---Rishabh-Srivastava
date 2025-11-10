# What to Do Next - Step by Step

## ✅ Current Status
- Backend server is **RUNNING** on http://localhost:8000
- FAISS index is built
- Dataset is processed
- API endpoints are working

---

## Step 1: Start the Frontend (5 minutes)

### Open a NEW Terminal Window
**Important**: Keep your backend terminal running! Open a **new terminal** for the frontend.

### In the New Terminal:

```powershell
# Navigate to frontend
cd "D:\SHL Assesment\frontend"

# Install dependencies (if not already done)
npm install

# Start the frontend server
npm run dev
```

**Expected Output**:
```
  ▲ Next.js 14.0.4
  - Local:        http://localhost:3000
  - Ready in 2.3s
```

### If you get errors:
- **"npm not found"**: Install Node.js from https://nodejs.org/
- **Port 3000 in use**: Change port: `npm run dev -- -p 3001`
- **Module errors**: Run `npm install` again

---

## Step 2: Test the Full System (2 minutes)

1. **Open your browser**: http://localhost:3000

2. **You should see**: 
   - SHL Assessment Recommender interface
   - Search input field
   - "Get Recommendations" button

3. **Test with a query**:
   - Enter: `"Hiring for a Python developer with strong communication skills"`
   - Click "Get Recommendations"
   - Wait a few seconds
   - You should see a table with 5-10 recommended assessments

4. **Verify**:
   - ✅ Recommendations appear
   - ✅ Assessment names are shown
   - ✅ URLs are clickable
   - ✅ Dark mode toggle works

---

## Step 3: Generate Submission Files (5 minutes)

### In your backend terminal (where server is running):

**Press `Ctrl+C` to stop the server temporarily**

Then run:

```powershell
cd "D:\SHL Assesment\backend"

# Generate submission CSV
python -m utils.evaluator
```

**This will**:
- Compute Mean Recall@10 on labeled data
- Generate `docs/results.csv` (evaluation results)
- Generate `docs/submission.csv` (for submission)

**Expected Output**:
```
Starting evaluation...
Evaluation Results:
Mean Recall@10: 0.XXXX
Total Queries: 10
Results saved to D:\SHL Assesment\docs\results.csv
Submission CSV saved to D:\SHL Assesment\docs\submission.csv
```

### Restart the server:
```powershell
python app.py
```

---

## Step 4: Verify Submission Files (2 minutes)

Check that files were created:

```powershell
# From project root
dir docs\*.csv
```

You should see:
- `results.csv` - Evaluation results
- `submission.csv` - Submission file

Open `docs/submission.csv` and verify:
- Format: `Query,Assessment_url`
- Each query has 5-10 assessment URLs
- URLs are valid

---

## Step 5: Complete Approach Report (10 minutes)

1. **Open**: `docs/approach_report.md`

2. **Fill in**:
   - Your name
   - Date
   - Mean Recall@10 score (from Step 3)
   - Any customizations you made
   - Results summary

3. **Export as PDF**:
   - Open in a Markdown editor (VS Code, Typora, etc.)
   - Export as PDF
   - Or use online converter: https://www.markdowntopdf.com/
   - **Keep it to 2 pages maximum**

---

## Step 6: Prepare for Deployment (Optional - 30-45 minutes)

### 6.1: Push to GitHub

```powershell
# From project root
cd "D:\SHL Assesment"

# Initialize git (if not done)
git init
git add .
git commit -m "SHL Assessment Recommendation System"

# Create repo on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/shl-assessment-recommender.git
git branch -M main
git push -u origin main
```

### 6.2: Deploy Backend (Render)

1. Go to https://render.com
2. Sign up/Login
3. New → Web Service
4. Connect GitHub repo
5. Configure:
   - **Root Directory**: `backend`
   - **Build Command**: `pip install -r requirements.txt && python -m utils.preprocess`
   - **Start Command**: `uvicorn app:app --host 0.0.0.0 --port $PORT`
6. Deploy and note the URL

### 6.3: Deploy Frontend (Vercel)

1. Go to https://vercel.com
2. Sign up/Login
3. Import GitHub repo
4. Configure:
   - **Root Directory**: `frontend`
   - **Environment Variable**: `NEXT_PUBLIC_API_URL` = your Render backend URL
5. Deploy and note the URL

**See `docs/submission_instructions.md` for detailed deployment steps**

---

## Step 7: Final Checklist

Before submitting, verify:

- [ ] Backend running locally: http://localhost:8000/health works
- [ ] Frontend running locally: http://localhost:3000 works
- [ ] Recommendations appear when searching
- [ ] `docs/submission.csv` is generated
- [ ] `docs/approach_report.md` is completed (2 pages, PDF)
- [ ] (Optional) Backend deployed and accessible
- [ ] (Optional) Frontend deployed and accessible
- [ ] (Optional) GitHub repo is public

---

## Quick Command Reference

### Backend (Terminal 1):
```powershell
cd "D:\SHL Assesment\backend"
python app.py
```

### Frontend (Terminal 2 - NEW):
```powershell
cd "D:\SHL Assesment\frontend"
npm install
npm run dev
```

### Generate Submission:
```powershell
cd "D:\SHL Assesment\backend"
python -m utils.evaluator
```

---

## What You'll Submit

1. **API Endpoint URL**: `http://localhost:8000` (or deployed URL)
2. **Frontend URL**: `http://localhost:3000` (or deployed URL)
3. **GitHub Repository**: (if you pushed to GitHub)
4. **CSV File**: `docs/submission.csv`
5. **Approach Report**: `docs/approach_report.pdf` (2 pages)

---

## Need Help?

- **Frontend won't start**: Check Node.js is installed (`node --version`)
- **No recommendations**: Check backend is running
- **CORS errors**: Backend CORS is already configured
- **Port conflicts**: Change ports in commands

---

## Current Status Summary

✅ Backend: **RUNNING** (http://localhost:8000)
⏳ Frontend: **Need to start** (next step)
⏳ Submission CSV: **Need to generate** (Step 3)
⏳ Approach Report: **Need to complete** (Step 5)
⏳ Deployment: **Optional** (Step 6)

---

**Start with Step 1: Open a new terminal and run the frontend!**

