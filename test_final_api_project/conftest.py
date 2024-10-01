import pytest
from endpoints.get_token import GetToken
from endpoints.get_meme import GetMemes
from endpoints.create_meme import CreateMeme
from endpoints.update_meme import UpdateMeme
from endpoints.delete_meme import DeleteMeme


@pytest.fixture
def meme_id(create_meme_endpoint, authorization_token):
    payload = {'text': 'Test Meme', 'url': 'http://example.com/meme.jpg', 'tags': ['test', 'meme'],
               'info': {'author': 'user123', 'date': '2024-01-01'}}
    create_meme_endpoint.create_new_meme(payload, headers=authorization_token)
    return create_meme_endpoint.response.json().get('id')


@pytest.fixture(scope='session')
def authorization_token():
    token = GetToken().get_token()
    return {'Authorization': token, 'Content-type': 'application/json'}


@pytest.fixture
def invalid_authorization_endpoint():
    return GetToken()


@pytest.fixture
def get_memes_endpoint():
    return GetMemes()


@pytest.fixture
def create_meme_endpoint():
    return CreateMeme()


@pytest.fixture
def update_meme_endpoint():
    return UpdateMeme()


@pytest.fixture
def delete_meme_endpoint():
    return DeleteMeme()
