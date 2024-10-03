import allure
import pytest


TEST_DATA = [
    {"text": "Created Meme", "url": "http://example.com/created_meme.jpg", "tags": ["created", "created_meme"], "info": {"author": "user123", "date": "2024-01-02"}},
    {"text": "12345", "url": "http://example.com/created_meme_111.jpg", "tags": [1, "created_meme", True], "info": {"author": 123, "date": False}},
    {"text": "@#$^&*", "url": "http://example.com/created_meme_222.jpg", "tags": ["@#$%", "$%^&"], "info": {"111": "@@##$", "date": "2024.01.02"}}
]

UPDATE_DATA = [
    {"text": "Updated Meme", "url": "http://example.com/updated_meme.jpg", "tags": ["updated", "meme"], "info": {"author": "user456", "date": "2024-01-02"}},
    {"text": "12345", "url": "http://example.com/updated_meme_111.jpg", "tags": [1, 5], "info": {"author": 123, "date": "2024/01/02"}},
    {"text": "@#$^&*", "url": "http://example.com/updated_meme_222.jpg", "tags": ["@#$%", True], "info": {"111": "@@##$", "date": "2024.01.02"}}
]

TEST_DATA_NEGATIVE = [
    {"text": (1, 2, 3), "url": "http://example.com/updated_meme_222.jpg", "tags": [111, "meme"], "info": {"tag_1": "tag 1 description"}},
    {"text": "Updated Meme", "url": False, "tags": [111, "meme"], "info": {"tag_1": "tag 1 description"}},
    {"text": "Updated Meme", "url": "http://example.com/updated_meme_222.jpg", "tags": False, "info": {"tag_1": "tag 1 description"}},
    {"text": "Updated Meme", "url": "http://example.com/updated_meme_222.jpg", "tags": [111, "meme"], "info": True},

]


@allure.feature('Invalid Authorization')
@allure.story('Requesting token with invalid credentials')
@allure.title('Test invalid authorization')
def test_invalid_authorization(invalid_authorization_endpoint):
    invalid_authorization_endpoint.invalid_authorization()
    invalid_authorization_endpoint.check_400_bad_request()

@allure.feature('Request without authorization')
@allure.story('Requesting info without authorization')
@allure.title('Test request info without authorization')
def test_get_all_memes_without_authorization(get_memes_endpoint):
    headers_without_authorization = {'Content-type': 'application/json'}
    get_memes_endpoint.get_memes(headers=headers_without_authorization)
    get_memes_endpoint.check_401_bad_request()

@allure.feature('Get all memes')
@allure.story('Getting all memes')
@allure.title('Test getting all memes')
def test_get_all_memes(authorization_token, get_memes_endpoint):
    get_memes_endpoint.get_memes(headers=authorization_token)
    get_memes_endpoint.check_that_status_is_200()

@allure.feature('Get memes by ID')
@allure.story('Getting meme by ID')
@allure.title('Test getting meme by ID')
@pytest.mark.parametrize('meme_id', [1, 5, 7])
def test_get_meme_by_id(authorization_token, get_memes_endpoint, meme_id):
    get_memes_endpoint.get_meme_by_id(meme_id=meme_id, headers=authorization_token)
    get_memes_endpoint.check_that_status_is_200()

@allure.feature('Get memes by ID - negative')
@allure.story('Getting meme by ID - negative')
@allure.title('Test getting meme by ID - negative')
@pytest.mark.parametrize('meme_id', [-2, 0, 'abc'])
def test_get_meme_by_id_negative(authorization_token, get_memes_endpoint, meme_id):
    get_memes_endpoint.get_meme_by_id(meme_id=meme_id, headers=authorization_token)
    get_memes_endpoint.check_404_bad_request()

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
    create_meme_endpoint.check_400_bad_request()

@allure.feature('Update Meme')
@allure.story('Updating an existing meme')
@allure.title('Test updating a meme with different data')
@pytest.mark.parametrize('update_data', UPDATE_DATA)
def test_meme_update(authorization_token, update_meme_endpoint, meme_id, update_data):
    payload = {'id': meme_id, 'text': update_data['text'], 'url': update_data['url'], 'tags': update_data['tags'], 'info': update_data['info']}
    update_meme_endpoint.update_existing_meme(meme_id=meme_id, payload=payload, headers=authorization_token)
    update_meme_endpoint.check_that_status_is_200()
    update_meme_endpoint.check_response_text_is_correct(update_data['text'])

@allure.feature('Update Meme - invalid data')
@allure.story('Updating an existing meme - invalid data')
@allure.title('Test updating a meme with invalid data')
@pytest.mark.parametrize('update_data', TEST_DATA_NEGATIVE)
def test_meme_update_invalid_data(authorization_token, update_meme_endpoint, meme_id, update_data):
    payload = {'id': meme_id, 'text': update_data['text'], 'url': update_data['url'], 'tags': update_data['tags'], 'info': update_data['info']}
    update_meme_endpoint.update_existing_meme(meme_id=meme_id, payload=payload, headers=authorization_token)
    update_meme_endpoint.check_400_bad_request()

@allure.feature('Update Meme - not all data')
@allure.story('Updating an existing meme - not all data')
@allure.title('Test updating a meme with not all data')
@pytest.mark.parametrize('update_data', TEST_DATA_NEGATIVE)
def test_meme_update_not_all_data(authorization_token, update_meme_endpoint, meme_id, update_data):
    payload = {'id': meme_id, 'text': update_data['text'], 'url': update_data['url'], 'tags': update_data['tags']}
    update_meme_endpoint.update_existing_meme(meme_id=meme_id, payload=payload, headers=authorization_token)
    update_meme_endpoint.check_400_bad_request()

@allure.feature('Delete Meme')
@allure.story('Deleting an existing meme')
@allure.title('Test deleting a meme')
def test_meme_delete(authorization_token, delete_meme_endpoint, meme_id):
    delete_meme_endpoint.delete_meme(meme_id=meme_id, headers=authorization_token)
    delete_meme_endpoint.check_that_status_is_200()

@allure.feature('Delete Meme - invalid ID')
@allure.story('Deleting an meme - invalid ID')
@allure.title('Test deleting a meme - invalid ID')
@pytest.mark.parametrize('meme_id', [-2, 0, 'abc'])
def test_meme_delete(authorization_token, delete_meme_endpoint, meme_id):
    delete_meme_endpoint.delete_meme(meme_id=meme_id, headers=authorization_token)
    delete_meme_endpoint.check_404_bad_request()
