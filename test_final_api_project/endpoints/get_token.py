import requests

from test_final_api_project.endpoints.endpoint import Endpoint


class GetToken(Endpoint):
    token_cache = None


    def get_new_token(self):
        payload = {'name': 'okarpuk'}
        response = requests.post(
            f'{self.url}/authorize',
            json=payload
        )
        if response.status_code == 200:
            token = response.json().get('token')
            self.token_cache = token
            return token
        else:
            raise Exception(f"Failed to get token. Status code: {response.status_code}")

    def check_token_validity(self, token):
        response = requests.get(f'{self.url}/authorize/{token}')
        return response.status_code == 200

    def get_token(self):
        if self.token_cache and self.check_token_validity(self.token_cache):
            return self.token_cache
        else:
            return self.get_new_token()

    def invalid_authorization(self):
        payload = {'name': [1, 3, 5]}
        self.response = requests.post(
            f'{self.url}/authorize',
            json=payload
        )
