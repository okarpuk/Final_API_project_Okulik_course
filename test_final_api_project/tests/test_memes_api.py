import allure
import pytest


TEST_DATA = [
    {"text": "meme_1", "url": "http://example.com/meme1.jpg", "tags": [1, "one", 5, True], "info": {"author": "author1", "date": "2024-01-01"}},
    {"text": "meme_2", "url": "http://example.com/meme2.jpg", "tags": [2, "two", 7, False], "info": {"author": "author1", "date": "2024-01-01"}},
    {"text": "meme_2", "url": "http://example.com/meme3.jpg", "tags": [1, "three", 9, True], "info": {"author": "author1", "date": "2024-01-01"}}
]

TEST_DATA_NEGATIVE = [
    {"text": (1, 2, 3), "url": 1, "tags": (1, "a", 5, True), "info": {"tag_1": "tag 1 description"}},
]

UPDATE_DATA = [
    {"text": "Updated Meme", "url": "http://example.com/updated_meme.jpg", "tags": ["updated", "meme"], "info": {"author": "user456", "date": "2024-01-02"}}
]


@allure.feature('Create new meme')
@allure.story('Creating new meme')
@allure.title('Test creating meme')
@pytest.mark.parametrize('data', TEST_DATA)
def test_meme_create(authorization_token, create_meme_endpoint, data):
    create_meme_endpoint.create_new_meme(payload=data, headers=authorization_token)
    create_meme_endpoint.check_that_status_is_200()
    create_meme_endpoint.check_response_text_is_correct(data['text'])


@allure.feature('Create meme - negative')
@allure.story('Creating meme - negative')
@allure.title('Test creating meme - negative')
@pytest.mark.parametrize('data', TEST_DATA_NEGATIVE)
def test_meme_create_negative(authorization_token, create_meme_endpoint, data):
    create_meme_endpoint.create_new_meme(payload=data, headers=authorization_token)
    create_meme_endpoint.check_bad_request()


@allure.feature('Update Meme')
@allure.story('Updating an existing meme')
@allure.title('Test updating a meme with different data')
@pytest.mark.parametrize('update_data', UPDATE_DATA)
def test_meme_update(authorization_token, update_meme_endpoint, meme_id, update_data):
    payload = {'id': meme_id, 'text': update_data['text'], 'url': update_data['url'], 'tags': update_data['tags'], 'info': update_data['info']}
    update_meme_endpoint.update_existing_meme(meme_id=meme_id, payload=payload, headers=authorization_token)
    update_meme_endpoint.check_that_status_is_200()
    update_meme_endpoint.check_response_text_is_correct(update_data['text'])


@allure.feature('Delete Meme')
@allure.story('Deleting an existing meme')
@allure.title('Test deleting a meme')
def test_meme_delete(authorization_token, delete_meme_endpoint, meme_id):
    delete_meme_endpoint.delete_meme(meme_id=meme_id, headers=authorization_token)
    delete_meme_endpoint.check_that_status_is_200()
