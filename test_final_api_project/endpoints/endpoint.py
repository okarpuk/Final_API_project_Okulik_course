import allure


class Endpoint:
    url = 'https://fakestoreapi.com/products'
    response = None
    json = None
    headers = {'Content-type': 'application/json'}

    @allure.step('Check that title is the same as sent')
    def check_response_title_is_correct(self, title):
        assert self.json['title'] == title, f"Need title {title} but get {self.json['title']}"

    @allure.step('Check that response is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200, f"Need status code - 200 but get {self.response.status_code}"

    @allure.step('Check that 400 error received')
    def check_bad_request(self):
        assert self.response.status_code == 400, f"Need status code - 400 but get {self.response.status_code}"
