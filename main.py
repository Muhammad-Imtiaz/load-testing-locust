import json
from locust import (HttpUser, task, between, TaskSet)

BASE_URL = 'https://api.fankave.com'
HEADERS = {'Content-Type': 'application/json', 'clientapikey': 'K5MeJJ3eQmZWt52K'}

@task()
def polling_rainfocus_api(self):

    # tokens list
    token_list = ['2dbb20df40e54b8189faed7229d2610b']

    for token in token_list:
        headers = {"Authorization": "Bearer " + token}
        headers.update(HEADERS)
        with self.client.post(f'{BASE_URL}/ids/verifyRainfocus', headers=headers, catch_response=True) as response:
            if response.text != "Success":
                return response.failure(f"Unable to communicate to rainfocus")

class IdsApp(HttpUser):
    tasks = [polling_rainfocus_api]


