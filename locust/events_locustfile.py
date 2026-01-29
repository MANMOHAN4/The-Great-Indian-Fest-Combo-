from locust import HttpUser, task, between

class EventsUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        # Common headers for all requests
        self.headers = {
            "Accept": "application/json",
            "User-Agent": "LocustLoadTest"
        }

    @task
    def view_events(self):
        with self.client.get(
            "/events",
            params={"user": "locust_user"},
            headers=self.headers,
            name="/events",
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(f"Failed with status {response.status_code}")
            else:
                response.success()
