from data_store.destination.destination_interface import BaseDestination


class DataStore:
    def __init__(self, destination:BaseDestination):
        """Creates a DataStore with given Destination setting.

        Args:
            destination (BaseDestination): The destination of data write with prefered format.
        """
        self.__destination = destination

    def put(self, key, val):
        """ Create a new data node, using key and stored value.

        Args:
            key (str): Key to be used for reaching data
            val (any): Data value to be stored
        """
        self.__destination.write(key, val)

    def put_batch(self, key_val_list):
        """ Create multiple data nodes. 

        Args:
            key_val_list (list[tuple[str, any]]): Key-Value list of data nodes to be created.
        """
        self.__destination.write_batch(key_val_list)

    def get(self, key):
        """ Get data value specified by Key

        Args:
            key (str): Key to be used for reaching data

        Returns:
            any: Retrieved data value
        """
        data = self.__destination.read()
        return data.get(key, None)

    def query(self, value=None, limit=-1, offset=0):
        """ Qeury across data, search a value and fetch data with maximum number of limit after some offset.

        Args:
            value (any, optional): The value to be seached. Defaults to None, brings all data.
            limit (int, optional): Maximum number of data to be retrieved. Defaults to -1 means fetch all matched.
            offset (int, optional): Number of matched node to skipped. Defaults to 0, meaning no ofset. Minus values set to 0.

        Returns:
            list[tuple[str, any]]: List of key-value pairs that matched.
        """
        if offset < 0: offset = 0
        data = self.__destination.read()
        if limit < 0:
            limit = len(data)
        
        if value is not None:
            data_ = {}
            for key, val in data.items():
                if val == value:
                    data_[key] = val
            data = data_

        range_end = offset + limit
        if range_end > len(data): range_end = len(data)

        result = []

        all_items = list(data.items())
        i = offset
        while i < range_end and len(result)<limit:
            result.append(all_items[i])
            i+=1
        return result    
        
    def update(self, key, value):
        """ Update an existing data node with new value.

        Args:
            key (str): Key to be used for reaching data
            value (any): Data value to be stored

        Raises:
            Exception: If Key does not exists at DataStore, Exception raises.
        """
        data = self.__destination.read()
        if key not in data:
            raise Exception("No Data to update")
        else:
            self.__destination.write(key, value)

    def delete(self, key):
        """Delete a data node.

        Args:
            key (str): Key to be used for reaching data that would be deleted.
        """
        self.__destination.delete(key)
    
    def format(self):
        """Returns format that DataStore uses to store data.

        Returns:
            str: Type of Data Format
        """
        return self.__destination.format()

    def destination(self):
        """Returns destination that DataStore uses to write data.

        Returns:
            str: Destination Name.
        """
        return self.__destination.name()