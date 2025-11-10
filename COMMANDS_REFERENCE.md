# Quick Commands Reference

Copy-paste these commands as you work through the setup.

## 🚀 Initial Setup

### Navigate to Project
```bash
cd "D:\SHL Assesment"
```

### Copy Dataset (replace path)
```bash
copy "C:\path\to\Gen_AI Dataset.xlsx" "backend\data\Gen_AI Dataset.xlsx"
```

---

## 🔧 Backend Commands

### Navigate to Backend
```bash
cd backend
```

### Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Initialize System (Build Index)
```bash
python scripts/initialize.py
```

### Start Server
```bash
python app.py
```

### Test API
```bash
python test_api.py
```

### Run Evaluation
```bash
python -m utils.evaluator
```

---

## 🎨 Frontend Commands

### Navigate to Frontend
```bash
cd frontend
```

### Install Dependencies
```bash
npm install
```

### Create Environment File
```bash
echo NEXT_PUBLIC_API_URL=http://localhost:8000 > .env.local
```

### Start Development Server
```bash
npm run dev
```

### Build for Production
```bash
npm run build
```

---

## 🧪 Testing Commands

### Test Backend Health
```bash
curl http://localhost:8000/health
```

### Test Backend Recommendations
```bash
curl -X POST http://localhost:8000/recommend -H "Content-Type: application/json" -d "{\"query\": \"Hiring for a Python developer\"}"
```

### Test Deployed Backend
```bash
curl https://your-api.onrender.com/health
```

---

## 📦 Git Commands

### Initialize Git
```bash
git init
git add .
git commit -m "Initial commit: SHL Assessment Recommendation System"
```

### Connect to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/shl-assessment-recommender.git
git branch -M main
git push -u origin main
```

---

## 🔍 Verification Commands

### Check Python Version
```bash
python --version
```

### Check Node Version
```bash
node --version
```

### Check Files Exist
```bash
dir backend\data
dir backend\vectorstore
dir docs
```

### Check Server Status
```bash
# Backend
curl http://localhost:8000/health

# Frontend
# Open http://localhost:3000 in browser
```

---

## 🐛 Troubleshooting Commands

### Reinstall Backend Dependencies
```bash
cd backend
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### Reinstall Frontend Dependencies
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

### Rebuild Index
```bash
cd backend
python scripts/initialize.py
```

### Check What's Using Port 8000
```bash
netstat -ano | findstr :8000
```

---

## 📝 Common Workflows

### Full Backend Setup
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python scripts/initialize.py
python app.py
```

### Full Frontend Setup
```bash
cd frontend
npm install
echo NEXT_PUBLIC_API_URL=http://localhost:8000 > .env.local
npm run dev
```

### Quick Test
```bash
# Terminal 1: Backend
cd backend
python app.py

# Terminal 2: Frontend
cd frontend
npm run dev

# Terminal 3: Test
cd backend
python test_api.py
```

---

## 🌐 Deployment URLs Template

Fill these in as you deploy:

```
Backend URL:  https://____________________.onrender.com
Frontend URL: https://____________________.vercel.app
GitHub Repo:  https://github.com/____________________/shl-assessment-recommender
```

---

## 💡 Pro Tips

1. **Keep terminals open**: Backend and frontend need to run simultaneously
2. **Check ports**: Make sure 8000 and 3000 are not in use
3. **Virtual environment**: Always activate before running Python commands
4. **Environment variables**: Set `NEXT_PUBLIC_API_URL` for frontend
5. **Test locally first**: Always test before deploying

---

**Save this file for quick reference!**

