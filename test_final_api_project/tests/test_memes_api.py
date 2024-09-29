import allure
import pytest


TEST_DATA = [
    {"title": "test product 2", "price": 222, "description": "the best product 2"},
    {"title": "test product 3", "price": 333, "description": "the best product 3"},
    {"title": "test product 4", "price": 444, "description": "the best product 4"}
]

TEST_DATA_NEGATIVE = [
    {"title": "I can't recieve 400 status code (always - 200). So it's just example"}
]


@allure.feature('Feature 1')
@allure.story('Story 1')
@allure.title('Test for Feature 1 and Story 1')
@pytest.mark.parametrize('data', TEST_DATA)
def test_meme_create(create_meme_endpoint, data, start_complete, before_after_every_test):
    create_meme_endpoint.create_new_meme(payload=data)
    create_meme_endpoint.check_that_status_is_200()
    create_meme_endpoint.check_response_title_is_correct(data['title'])


@allure.feature('Feature 2')
@allure.story('Story 2')
@allure.title('Test for Feature 2 and Story 2')
@pytest.mark.parametrize('data', TEST_DATA_NEGATIVE)
def test_meme_create_negative(create_meme_endpoint, data, start_complete, before_after_every_test):
    create_meme_endpoint.create_new_meme(payload=data)
    create_meme_endpoint.check_bad_request()


@allure.feature('Feature 3')
@allure.story('Story 3')
@allure.title('Test for Feature 3 and Story 3')
@pytest.mark.critical
def test_meme_update(update_meme_endpoint, meme_id, start_complete, before_after_every_test):
    payload = {"title": "test product UPD", "price": 555, "description": "the best product UPD"}
    update_meme_endpoint.update_created_meme(meme_id, payload)
    update_meme_endpoint.check_that_status_is_200()
    update_meme_endpoint.check_response_title_is_correct(payload['title'])


@allure.feature('Feature 4')
@allure.story('Story 4')
@allure.title('Test for Feature 4 and Story 4')
@pytest.mark.medium
def test_meme_delete(delete_meme_endpoint, meme_id, start_complete, before_after_every_test):
    delete_meme_endpoint.delete_created_meme(meme_id)
    delete_meme_endpoint.check_that_status_is_200()
