import pytest
from data_store.format.json_format import JsonDataFormat
import json


@pytest.fixture
def json_formatter():
    return JsonDataFormat()

@pytest.fixture
def data_dict():
    d = {}
    d["key_1"] = "val_1"
    d["key_2"] = 2
    d["key_3"] = "val_3"
    d["key_4"] = 4
    return d

@pytest.fixture
def data_dump():
    return '{"key_1": "val_1", "key_2": 2, "key_3": "val_3", "key_4": 4}'

def test_dump(data_dict, data_dump, json_formatter):
    actual = json_formatter.dump(data_dict)
    expected = data_dump
    assert actual == expected

def test_load(data_dict, data_dump, json_formatter):
    actual = json_formatter.load(data_dump)
    expected = data_dict
    assert actual == expected