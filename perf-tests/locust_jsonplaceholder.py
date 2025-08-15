from locust import HttpUser, task, between

class JSONPlaceholderUser(HttpUser):
    wait_time = between(0.1, 0.5)
    host = "https://jsonplaceholder.typicode.com"

    @task
    def get_posts(self):
        self.client.get("/posts")
