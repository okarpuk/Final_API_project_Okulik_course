import allure


class Endpoint:
    url = 'http://167.172.172.115:52355'
    response = None
    json = None
    headers = {'Content-type': 'application/json'}





    @allure.step('Check that text is the same as sent')
    def check_response_text_is_correct(self, text):
        assert self.json['text'] == text, f"Need title {text} but get {self.json['text']}"

    @allure.step('Check that response is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200, f"Need status code - 200 but get {self.response.status_code}"

    @allure.step('Check that 400 error received')
    def check_bad_request(self):
        assert self.response.status_code == 400, f"Need status code - 400 but get {self.response.status_code}"
