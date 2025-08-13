import requests
from jsonschema import validate

BASE = "https://reqres.in/api"

def test_get_users(headers):
    r = requests.get(f"{BASE}/users/2", headers=headers)
    assert r.status_code == 200
    assert r.json()["data"]["id"] == 2

def test_create_user(headers, user_payload):
    r = requests.post(f"{BASE}/users", json=user_payload, headers=headers)
    assert r.status_code in (201, 200)
    assert r.json()["name"] == "name_test"
    assert r.json()["job"] == "job_test"

def test_update_user(headers, user_payload):
    r = requests.put(f"{BASE}/users/2", json=user_payload, headers=headers)
    assert r.status_code in (200, 201)
    assert r.json()["name"] == "name_test"
    assert r.json()["job"] == "job_test"

def test_delete_user(headers):
    r = requests.delete(f"{BASE}/users/2", headers=headers)
    assert r.status_code in (200, 204)