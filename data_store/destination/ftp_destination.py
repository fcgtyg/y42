from data_store.destination.destination_interface import BaseDestination
import ftplib
from os import unlink


"""
    This file is a mock.
    Please do not run.
"""
class FTPDestination(BaseDestination):

    def __init__(self, format, ftp_address, username, password, filename):
        """Create FTP Destination setting with preferred data format. THIS IS MOCK CLASS.S
        Args:
            format (BaseDataFormat): Preferred Data Format to be used for data serialization.
            ftp_address (str): FTP host address to be connect
            username (str): Username for logging in to FTP.
            password (str): Password for logging in to FTP.
            filename (str): The filepath to be used for write/read data.

        Raises:
            NotImplementedError: _description_
        """
        super().__init__(format)
        self.hostname = ftp_address
        self.username = username
        self.password = password
        self.filename = filename

        raise NotImplementedError("This is a MOCK")


    def __connect(self):
        """Connect to FTP

        Returns:
            ftplib.FTP: FTP object
        """
        return ftplib.FTP(self.hostname, self.username, self.password)

    def __save(self, data_dict):
        """ Writedown data to specified file at FTP server .

        Args:
            data_dict (dict): Data object
        """
        data_dump = self._format.dump(data_dict)
        with open("data.tmp", "w") as f:
            f.write(data_dump)
        with open("data.tmp", "r") as f:
            ftp = self.__connect()
            ftp.storlines(f"STOR {self.filename}", f)
        unlink("data.tmp")

    def write(self, key, value):
        data_dict = self.read()
        data_dict[key] = value
        self.__save(data_dict)
        pass

    def read(self):
        ftp = self.__connect()
        file_content = ""
        ftp.retrlines(f"RETR {self.filename}", lambda x: file_content + f"{x}\n")
        ftp.close()
        data = self._format.load(file_content)
        return data

    def write_batch(self, key_val_list:list):
        data_dict = self.read()
        for key, value in key_val_list:
            data_dict[key] = value
        self.__save(data_dict)

    def delete(self, key):
        data_dict = self.read()
        if key in data_dict:
            data_dict.pop(key) 
        self.__save(data_dict)

    def name(self):
        return "FTP"

    def format(self):
        self._format.name()