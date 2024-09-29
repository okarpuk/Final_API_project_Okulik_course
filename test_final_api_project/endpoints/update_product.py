import requests
import allure

from test_final_api_project.endpoints.endpoint import Endpoint


class UpdateProduct(Endpoint):

    @allure.step('Update a product')
    def make_changes_in_product(self, post_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{post_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
