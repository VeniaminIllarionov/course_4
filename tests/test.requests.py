import pytest

from src.requests_hh import Request_HH


@pytest.fixture
def requests():
    api_list = Request_HH('Разработчик')
    return api_list


def test_init(requests):
    assert requests.name == 'Разработчик'
