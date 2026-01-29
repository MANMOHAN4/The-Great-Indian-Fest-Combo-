from locust import HttpUser, task, between

class MyEventsUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        self.headers = {
            "Accept": "application/json",
            "User-Agent": "LocustLoadTest"
        }

    @task
    def view_my_events(self):
        with self.client.get(
            "/my-events",
            params={"user": "locust_user"},
            headers=self.headers,
            name="/my-events",
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(f"Status code: {response.status_code}")
            else:
                response.success()
