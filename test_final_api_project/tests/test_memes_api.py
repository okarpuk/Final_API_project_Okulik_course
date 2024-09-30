import allure
import pytest


TEST_DATA = [
    {"text": "meme_1", "url": "https//:1", "tags": (1, "one", 5, True), "info": {"tag_1": "tag 1 description"}},
    {"text": "meme_2", "url": "https//:2", "tags": (2, "two", 7, False), "info": {"tag_2": "tag 2 description"}},
    {"text": "meme_2", "url": "https//:3", "tags": (1, "three", 9, True), "info": {"tag_3": "tag 3 description"}}
]

TEST_DATA_NEGATIVE = [
    {"text": (1, 2, 3), "url": "https//", "tags": (1, "a", 5, True), "info": {"tag_1": "tag 1 description"}},
]


@allure.feature('Feature 1')
@allure.story('Story 1')
@allure.title('Test for Feature 1 and Story 1')
@pytest.mark.parametrize('data', TEST_DATA)
def test_meme_create(authorization_token, create_meme_endpoint, data, start_complete, before_after_every_test):
    create_meme_endpoint.create_new_meme(payload=data, headers=authorization_token)
    create_meme_endpoint.check_that_status_is_200()
    create_meme_endpoint.check_response_text_is_correct(data['text'])
    print(create_meme_endpoint.json)


@allure.feature('Feature 2')
@allure.story('Story 2')
@allure.title('Test for Feature 2 and Story 2')
@pytest.mark.parametrize('data', TEST_DATA_NEGATIVE)
def test_meme_create_negative(authorization_token, create_meme_endpoint, data, start_complete, before_after_every_test):
    create_meme_endpoint.create_new_meme(payload=data, headers=authorization_token)
    create_meme_endpoint.check_bad_request()
    print(create_meme_endpoint.response)


@allure.feature('Feature 3')
@allure.story('Story 3')
@allure.title('Test for Feature 3 and Story 3')
@pytest.mark.critical
def test_meme_update(update_meme_endpoint, meme_id, start_complete, before_after_every_test):
    payload = {"text": "meme_1", "url": "https//:1", "tags": (1, "one", 5, True), "info": {"tag_1": "tag 1 description"}}
    update_meme_endpoint.update_created_meme(meme_id, payload)
    update_meme_endpoint.check_that_status_is_200()
    # update_meme_endpoint.check_response_title_is_correct(payload['title'])


@allure.feature('Feature 4')
@allure.story('Story 4')
@allure.title('Test for Feature 4 and Story 4')
@pytest.mark.medium
def test_meme_delete(delete_meme_endpoint, meme_id, start_complete, before_after_every_test):
    delete_meme_endpoint.delete_created_meme(meme_id)
    delete_meme_endpoint.check_that_status_is_200()
