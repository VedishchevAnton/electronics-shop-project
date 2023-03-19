import pytest
from src.phone import Phone


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_phone_init(phone):
    """
    Тест конструктора класса Phone
    """
    assert isinstance(phone, Phone)
    assert phone.name == 'iPhone 14'


def test_number_of_sim(phone):
    assert phone.number_of_sim == 2


