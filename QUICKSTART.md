# Quick Start Guide

Get the SHL Assessment Recommendation System up and running in minutes!

## Prerequisites Check

- [ ] Python 3.10+ installed (`python --version`)
- [ ] Node.js 18+ installed (`node --version`)
- [ ] `Gen_AI Dataset.xlsx` file available

## Step 1: Backend Setup (5 minutes)

```bash
# Navigate to backend
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Place your dataset
# Copy Gen_AI Dataset.xlsx to backend/data/

# Initialize the system (builds FAISS index)
python scripts/initialize.py

# Start the API server
python app.py
```

✅ Backend running at `http://localhost:8000`

Test it:
```bash
curl http://localhost:8000/health
```

## Step 2: Frontend Setup (3 minutes)

Open a new terminal:

```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

✅ Frontend running at `http://localhost:3000`

## Step 3: Test the System

1. Open browser: `http://localhost:3000`
2. Enter a query: "Hiring for a Python developer with strong communication skills"
3. Click "Get Recommendations"
4. See the results!

## Troubleshooting

### "Index not found" error
```bash
cd backend
python scripts/initialize.py
```

### "Dataset not found" warning
- Place `Gen_AI Dataset.xlsx` in `backend/data/` directory
- The system will use fallback data if dataset is missing

### Port already in use
- Backend: Change port in `app.py` or use `uvicorn app:app --port 8001`
- Frontend: Use `npm run dev -- -p 3001`

### CORS errors
- Ensure backend is running
- Check `NEXT_PUBLIC_API_URL` in frontend `.env.local`

## Next Steps

1. **Evaluate**: Run `python -m utils.evaluator` in backend
2. **Deploy**: Follow `docs/submission_instructions.md`
3. **Customize**: Modify embedding model or ranking logic

## Need Help?

- Check `README.md` for detailed documentation
- See `docs/` for deployment and approach details
- Review error messages in terminal

Happy coding! 🚀

