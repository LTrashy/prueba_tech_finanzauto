import requests
from jsonschema import validate

BASE = "https://reqres.in/api"

def test_login_success(login_payload_ok, headers):
    r = requests.post(f"{BASE}/login", json=login_payload_ok, headers=headers)
    assert r.status_code == 200
    assert "token" in r.json()

def test_login_fail(login_payload_fail, headers):
    r = requests.post(f"{BASE}/login", json=login_payload_fail, headers=headers)
    assert r.status_code == 400

def test_register_success(login_payload_ok, headers):
    r = requests.post(f"{BASE}/register", json=login_payload_ok, headers=headers)
    assert r.status_code == 200
    assert "token" in r.json()
    assert "id" in r.json()

def test_register_fail(login_payload_fail, headers):
    r = requests.post(f"{BASE}/register", json=login_payload_fail, headers=headers)
    assert r.status_code == 400
    assert "error" in r.json()

