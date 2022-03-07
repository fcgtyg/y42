from data_store.format.format_interface import BaseDataFormat


"""
    This file is a mock.
    Please do not run.
"""
class XMLDataFormat(BaseDataFormat):
    def dump(self, data_dict:dict):
        # Take a python dictionary object (depth 1)
        '''
            {
                key_1: value_1,
                key_2: value_2
            }
        '''

        # Convert it into xml format:
        '''
            <key_1> value_1 </key_1>
            <key_2> valeu_2 </key_2>
        '''

        # Return XML string
        raise NotImplementedError("This is a MOCK")

    def load(self, serialized_data):
        # Take an XML formatted string
        '''
            <key_1> value_1 </key_1>
            <key_2> valeu_2 </key_2>
        '''

        # Convert it into Python Dictionary
        '''
            {
                key_1: value_1,
                key_2: value_2
            }
        '''
        raise NotImplementedError("This is a MOCK")


    def name(self):
        return "XML Data Format"