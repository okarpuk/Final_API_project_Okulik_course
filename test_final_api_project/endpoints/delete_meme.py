import requests
import allure

from test_final_api_project.endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):

    @allure.step('Delete meme')
    def delete_created_meme(self, meme_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(
            f'{self.url}/meme/{meme_id}',
            headers=headers
        )
        self.json = self.response.json()
        return self.response
