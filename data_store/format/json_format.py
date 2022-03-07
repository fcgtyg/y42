from data_store.format.format_interface import BaseDataFormat
import json

class JsonDataFormat(BaseDataFormat):
    def dump(self, data_dict:dict):
        return json.dumps(data_dict)

    def load(self, serialized_data):
        return json.loads(serialized_data)

    def name(self):
        return "JSON Data Format"