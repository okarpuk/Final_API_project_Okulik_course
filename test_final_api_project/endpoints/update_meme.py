import requests
import allure

from test_final_api_project.endpoints.endpoint import Endpoint


class UpdateMeme(Endpoint):

    @allure.step('Update a product')
    def update_created_meme(self, meme_id, payload, headers=None):
        headers = headers if headers else {}
        combined_headers = {**self.headers, **headers}
        self.response = requests.put(
            f'{self.url}/meme/{meme_id}',
            json=payload,
            headers=combined_headers
        )
        self.json = self.response.json()
        return self.response
