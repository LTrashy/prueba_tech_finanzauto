import pytest

@pytest.fixture()
def post_schema():
    return {
        "type": "object",
        "properties": {
            "userId": {"type": "integer"},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "body": {"type": "string"}
        },
        "required": ["userId","id","title","body"]
    }
@pytest.fixture()
def comment_schema():
    return {
        "type": "object",
        "properties": {
            "postId": {"type": "integer"},
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "email": {"type": "string"},
            "body": {"type": "string"}
        },
        "required": ["postId","id","name","email","body"]
    }
@pytest.fixture()
def payload():
    return {
        "title":"title_test",
        "body":"body_test",
        "userId":1,
        "id":100
    }

@pytest.fixture()
def user_payload():
    return {
        "name":"name_test",
        "job":"job_test"
    }

@pytest.fixture()
def login_payload_ok():
    return {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

@pytest.fixture()
def login_payload_fail():
    return {
        "email": "peter@klaven"
    }

@pytest.fixture()
def headers():
    return{"X-Api-Key": "reqres-free-v1"}