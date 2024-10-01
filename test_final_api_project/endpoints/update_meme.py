import requests
import allure

from test_final_api_project.endpoints.endpoint import Endpoint


class UpdateMeme(Endpoint):

    @allure.step('Update a meme')
    def update_existing_meme(self, meme_id, payload, headers):
        self.response = requests.put(
            f"{self.url}/meme/{meme_id}",
            headers=headers,
            json=payload
        )
