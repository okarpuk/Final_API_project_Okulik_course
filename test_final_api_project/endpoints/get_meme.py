import requests
import allure

from test_final_api_project.endpoints.endpoint import Endpoint


class GetMemes(Endpoint):

    @allure.step('Get all memes')
    def get_memes(self, headers):
        self.response = requests.get(
            f"{self.url}/meme",
            headers=headers
        )

    @allure.step('Get meme by ID')
    def get_meme_by_id(self, meme_id, headers):
        self.response = requests.get(
            f"{self.url}/meme/{meme_id}",
            headers=headers
        )
