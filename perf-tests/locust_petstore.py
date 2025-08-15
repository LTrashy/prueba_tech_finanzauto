from locust import HttpUser, task, between

class PetstoreUser(HttpUser):
    wait_time = between(0.1, 0.5)
    host = "https://petstore.swagger.io"

    @task
    def get_pets(self):
        self.client.get("/v2/pet/findByStatus?status=available")
