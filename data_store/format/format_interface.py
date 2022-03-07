
from abc import ABC as Abstract, abstractmethod

class BaseDataFormat(Abstract):
    @abstractmethod
    def dump(self, data_dict:dict):
        """ Converts data to string to prepare it to store.

        Args:
            data_dict (dict): Dictionary representation of data.
        """
        pass

    @abstractmethod
    def load(self, serialized_data) -> dict:
        """ Load serialized string data into Python Dictionary object

        Args:
            serialized_data (str): Serialized data.

        Returns:
            dict: Python Dictionary representation of data
        """
        pass

    @abstractmethod
    def name(self):
        """ Returns name of Data Format

        Returns:
            str: Name of Data Format
        """
        pass