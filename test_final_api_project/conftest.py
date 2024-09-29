import pytest
from endpoints.create_product import CreateProduct
from endpoints.update_product import UpdateProduct
from endpoints.delete_product import DeleteProduct


@pytest.fixture()
def create_product_endpoint():
    return CreateProduct()


@pytest.fixture()
def update_product_endpoint():
    return UpdateProduct()


@pytest.fixture()
def delete_product_endpoint():
    return DeleteProduct()


@pytest.fixture()
def post_id(create_product_endpoint):
    payload = {"title": "test product 1", "price": 100, "description": "the best product"}
    create_product_endpoint.create_new_product(payload)
    yield create_product_endpoint.post_id


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
