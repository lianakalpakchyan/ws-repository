import pytest

from exceptions import DuplicateEmailError
from repos.sqlite import SQLiteRepository
from schemas.users import User


@pytest.fixture
def repo():
    return SQLiteRepository(db_name=":memory:")


def test_save_and_find(repo):
    repo.save(User("Alice", "alice@example.com", 30))
    result = repo.find_by_email("alice@example.com")
    assert result == User("Alice", "alice@example.com", 30, id=1)


def test_find_returns_none_when_not_found(repo):
    result = repo.find_by_email("ghost@example.com")
    assert result is None


def test_save_raises_on_duplicate_email(repo):
    repo.save(User("Alice", "alice@example.com", 30))
    with pytest.raises(DuplicateEmailError):
        repo.save(User("Alice", "alice@example.com", 30))