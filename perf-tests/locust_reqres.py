from locust import HttpUser, task, between

class ReqResUser(HttpUser):
    wait_time = between(0.1, 0.5)
    host = "https://reqres.in"

    @task
    def get_users(self):
        self.client.get("/api/users?page=2")
