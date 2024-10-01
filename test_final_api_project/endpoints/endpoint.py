import allure


class Endpoint:
    url = 'http://167.172.172.115:52355'
    response = None
    headers = {'Content-type': 'application/json'}


    @allure.step('Check that response is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200, f"Expected status code 200, got {self.response.status_code}"


    @allure.step('Check that 400 error received')
    def check_bad_request(self):
        assert self.response.status_code == 400, f"Need status code - 400 but got {self.response.status_code}"


    @allure.step('Check that 404 error received')
    def check_404_bad_request(self):
        assert self.response.status_code == 404, f"Need status code - 404 but got {self.response.status_code}"


    @allure.step('Check that text is the same as sent')
    def check_response_text_is_correct(self, expected_text):
        response_json = self.response.json()
        assert response_json.get('text') == expected_text, f"Expected text '{expected_text}', got {response_json.get('text')}"


    @allure.step('Check that returned meme ID is correct')
    def check_response_meme_id_is_correct(self, expected_meme_id):
        response_json = self.response.json()
        assert response_json.get('id') == expected_meme_id, f"Expected meme ID '{expected_meme_id}', got {response_json.get('id')}"
