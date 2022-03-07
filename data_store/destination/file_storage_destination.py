from data_store.destination.destination_interface import BaseDestination
from data_store.format.format_interface import BaseDataFormat

class FileStorage(BaseDestination):
    def __init__(self, format:BaseDataFormat, filepath:str):
        """Create File Storage Destination with preferred data format

        Args:
            format (BaseDataFormat): Preferred Data Format to be used for data serialization.
            filepath (str): The filepath to be used for write/read data.
        """
        super().__init__(format)
        self.__path = filepath
        open(filepath, "a")

    def write_batch(self, key_val_list):
        data = self.read()
        for key, value in key_val_list:
            data[key] = value
        self.__save(data)


    def write(self, key, value):
        data = self.read()
        data[key] = value
        self.__save(data)

    def __save(self, data):
        """Writedown data to specified file.

        Args:
            data (dict): Data object
        """
        with open(self.__path, "w") as store:
            store.write(self._format.dump(data))

    def read(self):
        data = {}
        with open(self.__path, "r+") as store:
            serialized_data = store.read()
            if len(serialized_data) > 0:
                data = self._format.load(serialized_data)
        return data

    def delete(self, key):
        data = self.read()
        if key in data:
            data.pop(key)
        self.__save(data)

    def name(self):
        return "Local File Storage"

    def format(self):
        return self._format.name()
 