import pytest

from .tag_creator_validator import tag_creator_validator
from src.errors.errors_types.http_unprocessable_entity import HttpUnprocessableEntityError


class MockRequest:
    def __init__(self, json) -> None:
        self.json = json


def test_tag_creator_validator():
    req = MockRequest(json={"product_code": "0090009.0800.6000100"})
    tag_creator_validator(req)


def test_tag_creator_validator_with_error():
    req = MockRequest(json={"product_code": 123})

    with pytest.raises(HttpUnprocessableEntityError):
        tag_creator_validator(req)


def test_tag_creator_validator_ckeck_if_no_pass_request_format_error():
    req = MockRequest(json={"product_code": 123})
    try:
        tag_creator_validator(req)
        assert False
    except Exception as e:
        assert isinstance(e, HttpUnprocessableEntityError)

