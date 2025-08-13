import requests
from jsonschema import validate

BASE = "https://reqres.in/api"

def test_users_pagination(headers):
    r = requests.get(f"{BASE}/users?page=2", headers=headers)
    assert r.status_code == 200
    data = r.json()
    assert data["page"] == 2
    assert isinstance(data["data"], list)

def test_rate_timing(headers):
    many_requests = False
    for _ in range(30):
        r = requests.get(f"{BASE}/users?page=2",headers=headers)
        if r.status_code == 429:
            many_requests = True
            break
    
    assert many_requests or r.status_code == 200