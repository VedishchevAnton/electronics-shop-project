import pytest
from src.phone import Phone


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_phone_init(phone):
    """
    Тест конструктора класса Phone
    """
    assert str(phone) == 'iPhone 14'
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone.number_of_sim == 2
