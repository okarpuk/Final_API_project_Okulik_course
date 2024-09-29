import requests
import allure

from test_final_api_project.endpoints.endpoint import Endpoint


class CreateProduct(Endpoint):
    post_id = None

    @allure.step('Create new product')
    def create_new_product(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        self.post_id = self.json['id']
        return self.response
