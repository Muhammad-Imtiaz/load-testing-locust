import json
from locust import (HttpUser, task, between, TaskSet)

BASE_URL = 'https://api.fankave.com'
HEADERS = {'Content-Type': 'application/json', 'clientapikey': 'K5MeJJ3eQmZWt52K'}

@task
def polling_rainfocus_api(self):
    
    response = self.client.get(f'https://events.rainfocus.com/api/jwt?clientId=28f702ad-ba8a-4bbe-9df4-ac0292d68ec5&rfApiProfileId=VovKmNb0KMqSUc1tYgRLZIrGijssV7iuclglobal2021')
    jwt_token = json.loads(response.content)
    token = jwt_token['jwt']

    # headers = {"Authorization": "Bearer " + token}
    # headers.update(HEADERS)
    # print(HEADERS)
    with self.client.post(f'{BASE_URL}/ids/verifyRainfocus', headers=headers, data={"token": f'{token}'}, catch_response=True) as response:
        if response.text != "Success":
            return response.failure(f"Unable to communicate to rainfocus")

class IdsApp(HttpUser):
    tasks = [polling_rainfocus_api]

    