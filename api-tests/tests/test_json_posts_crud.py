import requests
from jsonschema import validate
import time

BASE = "https://jsonplaceholder.typicode.com"

def assert_response_time(r, max_seconds=2):
    assert r.elapsed.total_seconds() < max_seconds, f"Tiempo de respuesta {r.elapsed.total_seconds()} > {max_seconds}"

def test_get_posts(post_schema):
    r = requests.get(f"{BASE}/posts")
    assert_response_time(r)
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    validate(instance=data[0], schema=post_schema)

def test_post_posts(payload):
    r = requests.post(f"{BASE}/posts", json=payload)
    assert_response_time(r)
    assert r.status_code in (201, 200)
    assert r.json().get("title") == "title_test"
    assert r.json().get("id") == 101
    assert r.json().get("body") == "body_test"
    assert r.json().get("userId") == 1

def test_update_posts(payload):
    r = requests.put(f"{BASE}/posts/{payload['id']}", json={"title":"updated","body":"body_updated","userId":1})
    assert_response_time(r)
    assert r.status_code in (200, 201)
    assert r.json().get("title") == "updated"


def test_delete_post(payload):
    r = requests.delete(f"{BASE}/posts/{payload['id']}")
    assert_response_time(r)
    assert r.status_code in (200, 204)
