# Data Store Library

This package implements a simple data store (without performance concerns). Users can select where to store data (destination) and how to keep data (format). With the power of inheritence and OOP, new destination and formats can be added into ecosystem. 

## Structure

* `./data_store.py`: This file exposes a basic API for users with a class named `DataStore`.

* `./format/`: This directory holds a format interface class at `format_interface.py` which exposes an abstract class named `BaseDataFormat`. Other files are implementations of that class and each one implements another data format.

* `./destination/`: This directory holds a destination interface class at `destination_interface.py` which exposes an abstract class named `BaseDestination`. Other files are implementations of that class and each one implements another data destination.

* `./test/` : Unit tests for **Data Store Library** challenge solution.
## How to run?

At the project root, a file called `data_store_run.py` holds an example for custom testing and running. 

Also unit tests provided at `data_store_test/` directory located at project root. Refer `data_store_test/README.md`.

----

## Adding New Functionality

### Adding New Format

Create an implementation of `BaseFormat` of `./format/format_interface.py`. 
> Full implementation example is `JSONDataFormat` class located in `./format/json_format.py`.

> Mock implementation is `XMLDataFormat` class located in `./format/xml_format.py`.

### Adding New Destination

Create an implementation of `BaseDestination` of `./destination/destination_interface.py`. 
> Full implementation example is `FileStorage` class located in `./destination/file_storage_destination.py`.

> Mock implementation is `FTPDestination` class located in `./destination/ftp_destination.py`.


----

## Running Tests

Assuming the running directory is project root, run below scripts for testing. 

> `$ pytest data_store/test/test_data_store.py`  
`$ pytest data_store/test/test_fs_dest.py`  
`$ pytest data_store/test/test_json_format.py `