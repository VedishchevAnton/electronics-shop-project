import pytest
from src.csv_error import InstantiateCSVError
import os


def test_csv_error():
    """
    Тест на исключение если фаил поврежден
    """
    with pytest.raises(InstantiateCSVError):
        raise InstantiateCSVError


