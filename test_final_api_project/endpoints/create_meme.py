import requests
import allure

from test_final_api_project.endpoints.endpoint import Endpoint


class CreateMeme(Endpoint):

    @allure.step('Create new meme')
    def create_new_meme(self, payload, headers):
        self.response = requests.post(
            f"{self.url}/meme",
            headers=headers,
            json=payload
        )
