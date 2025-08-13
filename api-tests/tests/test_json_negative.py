import requests
from jsonschema import validate
import time

BASE = "https://jsonplaceholder.typicode.com"
def assert_response_time(r, max_seconds=2):
    assert r.elapsed.total_seconds() < max_seconds, f"Tiempo de respuesta {r.elapsed.total_seconds()} > {max_seconds}"

def test_get_non_existing_posts():
    r = requests.get(f"{BASE}/posts/999")
    assert_response_time(r)
    assert r.status_code == 404 or r.json() == {}

def test_invalid_payload_posts():
    invalid_payload = {"title":123, "body":123, "userId":"test", "id":"test"}
    r = requests.post(f"{BASE}/posts", json=invalid_payload)
    assert_response_time(r)
    assert r.status_code in (400, 200, 201)

def test_method_not_allowed():
    r = requests.patch(f"{BASE}/posts")
    assert_response_time(r)
    assert r.status_code in (405, 404)