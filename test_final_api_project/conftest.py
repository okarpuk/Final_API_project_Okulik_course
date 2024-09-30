import pytest
from endpoints.get_token import GetToken
from endpoints.create_meme import CreateMeme
from endpoints.update_meme import UpdateMeme
from endpoints.delete_meme import DeleteMeme


@pytest.fixture
def auth_token_endpoint():
    return GetToken()


@pytest.fixture
def authorization_token(auth_token_endpoint):
    token = auth_token_endpoint.get_authorization_token(payload={"name": "Okarpuk"})
    return token


@pytest.fixture()
def create_meme_endpoint():
    return CreateMeme()


@pytest.fixture()
def update_meme_endpoint():
    return UpdateMeme()


@pytest.fixture()
def delete_meme_endpoint():
    return DeleteMeme()


@pytest.fixture()
def meme_id(authorization_token, create_meme_endpoint):
    payload = {"text": "meme_1", "url": "https//:1", "tags": (1, "one", 5, True), "info": {"tag_1": "tag 1 description"}}
    create_meme_endpoint.create_new_meme(payload, headers=authorization_token)
    yield create_meme_endpoint.meme_id


@pytest.fixture(scope='session')
def start_complete():
    print('\nStart testing')
    yield
    print('\nTesting completed')


@pytest.fixture()
def before_after_every_test():
    print('\nBefore test')
    yield
    print('\nAfter test')
