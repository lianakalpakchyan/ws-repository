import pytest
from unittest.mock import MagicMock

from exceptions import DuplicateEmailError
from repos.sqlite import SQLiteRepository
from schemas.users import User
from services.users import UserService


@pytest.fixture
def mock_repo():
    return MagicMock(spec=SQLiteRepository)


@pytest.fixture
def service(mock_repo):
    return UserService(mock_repo)


def test_register_user(service, mock_repo):
    user = User("Alice", "alice@example.com", 30)
    service.register(user)


def test_find_by_email(service, mock_repo):
    mock_repo.find_by_email.return_value = {
        "name": "Alice", "email": "alice@example.com", "age": 30, "id": 1
    }
    result = service.find_by_email("alice@example.com")
    assert result == User("Alice", "alice@example.com", 30, id=1)

    mock_repo.find_by_email.return_value = None
    result = service.find_by_email("ghost@example.com")
    assert result is None


def test_register_propagates_duplicate_email_error(service, mock_repo):
    mock_repo.save.side_effect = DuplicateEmailError("Duplicate email")
    with pytest.raises(DuplicateEmailError):
        service.register(User("Alice", "alice@example.com", 30))