from data_store.destination.file_storage_destination import FileStorage
from data_store.format.json_format import JsonDataFormat
from data_store.data_store import DataStore
from os import unlink

def example_run():
    ds.put("key", "val")
    ds.put_batch([("key_1", "val_1"), ("key_2", "val_2")])

    print("All Items :", ds.query())
    
    limit = 1
    offset = 5
    print(f"Get {limit} number of Items after skipping {offset} items", ds.query(limit=limit, offset=offset))


    print("key :", ds.get("key"))
    ds.update("key", "val_0")
    print("updated 'key' value into val_0")
    print("key :", ds.get("key"))

    try:
        ds.update("non_existing_key", "value")
    except Exception :
        print ("no key named 'non_existing_key'. nothing to update.")

    print("deleting 'key'")
    ds.delete("key")
    print("deleted 'key'")
    print("key :", ds.get("key"))

def clean_up(file_path):
    unlink(file_path)


if __name__ == "__main__":
    format = JsonDataFormat()
    destination = FileStorage(format, "store.json")
    ds = DataStore(destination)
    print(f"DataStore started with Destination {ds.destination()} and Format {ds.format()}")
    
    example_run()
    clean_up("store.json")
    

