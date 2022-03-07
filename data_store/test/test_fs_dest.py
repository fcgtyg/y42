import pytest
import json
from os import unlink
from os.path import exists
from data_store.destination.file_storage_destination import FileStorage
from data_store.format.json_format import JsonDataFormat

file_ = "testing_file.json"

@pytest.fixture
def file_storage():
    if exists(file_):
        unlink(file_)
    return FileStorage(JsonDataFormat(), file_)

@pytest.fixture
def mock_data_list():
    return [ ("key_1", 1), ("key_2", 2), ("key_3", 3) ]

@pytest.fixture
def mock_data_dump():
    return '{"key_1": "val_1", "key_2": 2, "key_3": "val_3", "key_4": 4}'


def test_write_batch(file_storage, mock_data_list):
    fs = file_storage
    fs.write_batch(mock_data_list)

    saved_data = {}
    with open(file_) as f:
        saved_data = json.load(f)
    
    for key, val in mock_data_list:
        assert saved_data[key] == val

def test_write(file_storage, mock_data_list):
    fs = file_storage
    mock_data = mock_data_list[0]
    fs.write(*mock_data)

    with open(file_) as f:
        assert json.load(f)[mock_data[0]] == mock_data[1]

def test_read(file_storage, mock_data_dump):
    fs = file_storage
    with open(file_, "w") as f:
        f.write(mock_data_dump)
    
    data_dict = fs.read()
    assert data_dict == json.loads(mock_data_dump)

def test_delete(file_storage, mock_data_dump):
    fs = file_storage
    with open(file_, "w") as f:
        f.write(mock_data_dump)
    
    fs.delete("key_1")
    expected = json.loads(mock_data_dump)
    expected.pop("key_1")

    assert fs.read() == expected

def teardown_module():
    unlink(file_)