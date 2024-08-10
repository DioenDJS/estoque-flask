from src.utils.logger import logger
from .auth_validator import auth_validator
from unittest.mock import Mock
import pytest


class MockRequest:
    def __init__(self, json) -> None:
        self.json = json


def test_auth_validator_success():
    req = Mock(json={"username": "User", "password": "12345"})
    try:
        auth_validator(req)
        assert True
    except Exception as e:
        # logger.error(f"Erro: {e}")
        print(f"Erro: {e}")
        assert AssertionError(str(e))


def test_auth_validator_format_password_invalid():
    req = Mock(json={"username": "User", "password": 12345})
    try:
        auth_validator(req)
        assert False
    except Exception as e:
        # logger.error(f"Erro: {e}")
        print(f"Erro: {e}")
        assert AssertionError(str(e))



def test_auth_validator_format_user_invalid():
    req = Mock(json={"username": 12345, "password": "12345"})
    try:
        auth_validator(req)
        assert False
    except Exception as e:
        # logger.error(f"Erro: {e}")
        print(f"Erro: {e}")
        assert AssertionError(str(e))

def test_auth_validator_format_password_empty():
    req = Mock(json={"username": "user", "password": ""})
    try:
        auth_validator(req)
        assert False
    except Exception as e:
        # logger.error(f"Erro: {e}")
        print(f"Erro: {e}")
        assert AssertionError(str(e))

def test_auth_validator_format_user_empty():
    req = Mock(json={"username": " ", "password": "12345"})
    try:
        auth_validator(req)
        assert False
    except Exception as e:
        # logger.error(f"Erro: {e}")
        print(f"Erro: {e}")
        assert AssertionError(str(e))