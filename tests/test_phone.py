import pytest
from src.phone import Phone


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)

