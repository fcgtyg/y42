import pytest
import json
from os import unlink
from os.path import exists
from data_store.data_store import DataStore
from data_store.destination.file_storage_destination import FileStorage
from data_store.format.json_format import JsonDataFormat

file_ = "testing_file.json"

@pytest.fixture
def data_store():
    if exists(file_):
        unlink(file_)
    return DataStore(FileStorage(JsonDataFormat(), file_))

@pytest.fixture
def mock_data_list():
    return [ ("key_1", 1), ("key_2", 2), ("key_3", 3) ]

@pytest.fixture
def mock_data_dump():
    return '{"key_1": "val_1", "key_2": "val_2", "key_3": "val_3", "key_4": "val_4"}'

def test_put(data_store, mock_data_list):
    ds = data_store
    mock_key, mock_val = mock_data_list[0]
    ds.put(mock_key, mock_val)

    with open(file_) as f:
        actual_data = json.load(f)
        assert actual_data[mock_key] == mock_val

def test_put_batch(data_store, mock_data_list):
    ds = data_store
    ds.put_batch(mock_data_list)
    with open(file_) as f:
        actual_data = json.load(f)
        for key, val in mock_data_list:
            assert actual_data[key] == val

def test_get(data_store, mock_data_dump):
    ds = data_store
    test_data = {}
    with open(file_, "w") as f:
        f.write(mock_data_dump)
    
    with open(file_) as f:
        test_data = json.load(f)
    
    for key, val in test_data.items():
        assert ds.get(key) == val

def test_query_limit_offset(data_store, mock_data_dump):
    ds = data_store
    test_data = {}
    with open(file_, "w") as f:
        f.write(mock_data_dump)
    
    with open(file_) as f:
        test_data = json.load(f)

    actual = ds.query(limit=1, offset=1) 
    
    assert actual == list(test_data.items())[1:2]

def test_query_value(data_store, mock_data_dump):
    ds = data_store
    test_data = {}
    with open(file_, "w") as f:
        f.write(mock_data_dump)
    
    with open(file_) as f:
        test_data = json.load(f)

    for key,value in test_data.items():
        actual = ds.query(value=value) 
        assert actual[0] == (key, value)

def test_update(data_store, mock_data_dump):
    ds = data_store
    test_data = {}
    with open(file_, "w") as f:
        f.write(mock_data_dump)
    
    with open(file_) as f:
        test_data = json.load(f)

    for key, val in test_data.items():
        ds.update(key, str(val) + "_updated")

    with open(file_) as f:
        for key,val in json.load(f).items():
            assert val.endswith("_updated")
    
    with pytest.raises(Exception) as expected_exception:
        ds.update("NOT_EXISTED_KEY", "value")


def teardown_module():
    unlink(file_)