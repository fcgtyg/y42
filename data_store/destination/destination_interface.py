from abc import ABC as Abstract, abstractmethod
from data_store.format.format_interface import BaseDataFormat

class BaseDestination(Abstract):
    def __init__(self, format:BaseDataFormat):
        """ Create destination setting with preferred data format

        Args:
            format (BaseDataFormat): Preferred Data Format to be used for data serialization.
        """
        self._format = format
        super().__init__()

    @abstractmethod
    def write(self, key, value):
        """ Create a new data node, using key and stored value.

        Args:
            key (str): Key to be used for reaching data
            val (any): Data value to be stored
        """
        pass

    @abstractmethod
    def read(self) -> dict:
        """ Retrieve all data into Python Dictionary

        Returns:
            dict: Python Dictionary representation of existing data
        """
        pass

    @abstractmethod
    def write_batch(self, key_val_list:list):
        """ Create multiple data nodes. 

        Args:
            key_val_list (list[tuple[str, any]]): Key-Value list of data nodes to be created.
        """
        pass

    @abstractmethod
    def delete(self, key):
        """Delete a data node.

        Args:
            key (str): Key to be used for reaching data that would be deleted.
        """
        pass

    @abstractmethod
    def name(self):
        """Returns destination that DataStore uses to write data.

        Returns:
            str: Destination Name.
        """
        pass

    @abstractmethod
    def format(self):
        """Returns format that Destination uses to store data.

        Returns:
            str: Type of Data Format
        """
        pass