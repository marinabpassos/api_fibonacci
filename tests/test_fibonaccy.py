import requests

BASE_URL = "http://localhost:8000"

def test_fibonacci_route():
    response = requests.post(f"{BASE_URL}/api/fibonacci", json={"n": 5})
    assert response.status_code == 200
    data = response.json()
    assert data == [0, 1, 1, 2, 3]