import requests
from jsonschema import validate
import time

BASE = "https://jsonplaceholder.typicode.com"

def assert_response_time(r, max_seconds=2):
    assert r.elapsed.total_seconds() < max_seconds, f"Tiempo de respuesta {r.elapsed.total_seconds()} > {max_seconds}"

def test_posts_comments_relation(payload, comment_schema):
    r = requests.get(f"{BASE}/posts/{payload['id']}/comments")
    assert_response_time(r)
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    validate(instance=data[0], schema=comment_schema)

def test_users_posts_relation(payload, post_schema):
    r = requests.get(f"{BASE}/users/{payload['userId']}/posts")
    assert_response_time(r)
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    validate(instance=data[0], schema=post_schema)