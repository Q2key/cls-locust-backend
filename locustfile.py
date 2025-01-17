from locust import TaskSet, HttpUser, task, between
import uuid
import random
import time


class UserBehavior(TaskSet):
    def authenticate(self):
        login = uuid.uuid4().__str__()
        with self.client.post('/users/authenticate',
                              json={"login": login},
                              headers={"content-type": "application/json"}, catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Not authorized")
                exit(-1)

        response_obj = response.json()
        return {
            'Content-Type': 'application/json',
            "Authorization": f'Bearer {response_obj["token"]}'
        }

    def on_start(self):
        pass

    @task
    def perform_actions(self):
        sleep_timer = 1  # Adjust this as needed
        # In-App Purchase request
        in_app_request_dto = {
            "TransactionId": "test",
            "DefinitionId": "test",
            "CurrencyCode": "USD",
            "Price": 10
        }

        headers = self.authenticate()

        in_app_response = self.client.post(f"/iaps/ios-purchase", json=in_app_request_dto, headers=headers)
        print(f"inAppHttpResponse: {in_app_response.status_code}")
        time.sleep(sleep_timer)
        # Update user data
        user_dto = {"LevelProgress": random.randint(16, 50)}
        player_update_response = self.client.put(f"/users/update", json=user_dto, headers=headers)
        print(f"playerUpdateResponse: {player_update_response.status_code}")
        time.sleep(sleep_timer)

        # Fetch offers
        offers_response = self.client.get(f"/Configurations/offers/V2", headers=headers)
        print(f"offersResponse: {offers_response.status_code}")
        time.sleep(sleep_timer)

        # Repeat In-App Purchase request
        in_app_response_2 = self.client.post(f"/iaps/ios-purchase", json=in_app_request_dto,
                                             headers=headers)
        print(f"inAppHttpResponse2: {in_app_response_2.status_code}")
        time.sleep(sleep_timer)

        # Repeat update user data
        user_dto_2 = {"LevelProgress": random.randint(16, 50)}
        player_update_response_2 = self.client.put(f"/users/update", json=user_dto_2, headers=headers)
        print(f"playerUpdateResponse2: {player_update_response_2.status_code}")
        time.sleep(sleep_timer)

        # Repeat fetch offers
        offers_response_2 = self.client.get(f"/Configurations/offers/V2", headers=headers)
        print(f"offersResponse2: {offers_response_2.status_code}")
        time.sleep(sleep_timer)

        print("Sequence finished")


class LoadTestUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 2)  # Adjust as needed
