import requests
import allure

from test_final_api_project.endpoints.endpoint import Endpoint


class CreateMeme(Endpoint):
    meme_id = None

    @allure.step('Create new meme')
    def create_new_meme(self, payload, headers=None):
        headers = headers if headers else {}
        combined_headers = {**self.headers, **headers}
        self.response = requests.post(
            f'{self.url}/meme',
            json=payload,
            headers=combined_headers
        )
        self.json = self.response.json()
        self.meme_id = self.json['id']
        return self.response
