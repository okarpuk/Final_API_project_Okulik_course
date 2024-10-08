import allure


class Endpoint:
    url = 'http://167.172.172.115:52355'
    response = None
    headers = {'Content-type': 'application/json'}


    @allure.step('Check that text is the same as sent')
    def check_response_data_is_correct(self, expected_data):
        response_json = self.response.json()
        assert response_json['text'] == expected_data['text'], "Text does not match"
        assert response_json['url'] == expected_data['url'], "URL does not match"
        assert response_json['info'] == expected_data['info'], "Info does not match"
        assert response_json['tags'] == expected_data['tags'], "Tags do not match"

    @allure.step('Check that returned meme ID is correct')
    def check_response_meme_id_is_correct(self, expected_meme_id):
        response_json = self.response.json()
        assert response_json.get('id') == expected_meme_id, f"Expected meme ID '{expected_meme_id}', got {response_json.get('id')}"

    @allure.step('Check that JSON keys are correct')
    def check_response_json_keys_are_correct(self, expected_json_keys):
        response_json = self.response.json()
        for key in expected_json_keys:
            assert key in response_json, f"Key '{key}' is missing in the JSON response"

    @allure.step('Check that response contains the expected text')
    def check_response_contains_text(self, expected_text):
        response_text = self.response.text
        assert expected_text in response_text, f"Expected text '{expected_text}' not found in the response"

    @allure.step('Check that response is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200, f"Expected status code 200, got {self.response.status_code}"

    @allure.step('Check that 400 error received')
    def check_400_bad_request(self):
        assert self.response.status_code == 400, f"Need status code - 400 but got {self.response.status_code}"

    @allure.step('Check that 401 error received')
    def check_401_bad_request(self):
        assert self.response.status_code == 401, f"Need status code - 401 but got {self.response.status_code}"

    @allure.step('Check that 404 error received')
    def check_404_bad_request(self):
        assert self.response.status_code == 404, f"Need status code - 404 but got {self.response.status_code}"
