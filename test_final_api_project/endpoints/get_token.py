import requests
import allure

from test_final_api_project.endpoints.endpoint import Endpoint


class GetToken(Endpoint):
    token = None

    @allure.step('Get token')
    def get_authorization_token(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            f'{self.url}/meme',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        self.token = self.json['token']
        return {"Authorization": self.token}
