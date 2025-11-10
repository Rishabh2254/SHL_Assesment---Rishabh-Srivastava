"""
Simple test script to verify API endpoints
Run this after starting the server: python app.py
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def test_health():
    """Test health endpoint"""
    print("Testing /health endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        assert response.status_code == 200
        assert response.json()["status"] == "running"
        print("✅ Health check passed!\n")
        return True
    except Exception as e:
        print(f"❌ Health check failed: {e}\n")
        return False

def test_recommend():
    """Test recommend endpoint"""
    print("Testing /recommend endpoint...")
    test_queries = [
        "Hiring for a Python developer with strong communication skills",
        "Need a data analyst who can work with SQL and Excel",
        "Looking for a software engineer with problem-solving abilities"
    ]
    
    for query in test_queries:
        try:
            print(f"\nQuery: {query}")
            response = requests.post(
                f"{BASE_URL}/recommend",
                json={"query": query},
                headers={"Content-Type": "application/json"}
            )
            print(f"Status Code: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                recommendations = data.get("recommendations", [])
                print(f"Found {len(recommendations)} recommendations:")
                for i, rec in enumerate(recommendations[:3], 1):
                    print(f"  {i}. {rec['assessment_name']}")
                    print(f"     URL: {rec['assessment_url']}")
                print("✅ Recommendation test passed!")
            else:
                print(f"❌ Error: {response.text}")
                return False
        except Exception as e:
            print(f"❌ Recommendation test failed: {e}")
            return False
    
    print("\n✅ All recommendation tests passed!\n")
    return True

if __name__ == "__main__":
    print("=" * 60)
    print("SHL Assessment Recommendation API - Test Suite")
    print("=" * 60)
    print(f"\nTesting API at: {BASE_URL}")
    print("Make sure the server is running: python app.py\n")
    
    health_ok = test_health()
    if health_ok:
        recommend_ok = test_recommend()
        if recommend_ok:
            print("=" * 60)
            print("✅ All tests passed! API is working correctly.")
            print("=" * 60)
        else:
            print("=" * 60)
            print("❌ Recommendation tests failed.")
            print("=" * 60)
    else:
        print("=" * 60)
        print("❌ Health check failed. Is the server running?")
        print("=" * 60)
        print("\nStart the server with: python app.py")

