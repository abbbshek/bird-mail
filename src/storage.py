# this file handles the storage of messages in JSON files

import json
import os
from src.message import Message


# handles the storage of messages in JSON files
class FileStorage:
    def __init__(self, data_path):
        self.data_path = data_path

    # loads the messages from the JSON file
    def load(self, folder_name):
        file_path = os.path.join(self.data_path, f"{folder_name}.json")
        
        try:
            with open(file_path, "r") as file:
                json_data = json.load(file)
        except FileNotFoundError:
            return []

        if not isinstance(json_data, list):
            return []

        message_list = []
        for message_dict in json_data:
            message_object = Message.from_dict(message_dict)
            message_list.append(message_object)
            
        return message_list

    # saves the messages to the JSON file
    def save(self, folder_name, messages):
        os.makedirs(self.data_path, exist_ok=True)
        file_path = os.path.join(self.data_path, f"{folder_name}.json")
        
        json_data = []
        for message in messages:
            message_dict = message.to_dict()
            json_data.append(message_dict)
        
        with open(file_path, "w") as file:
            json.dump(json_data, file, indent=2)