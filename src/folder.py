# Defines the Folder class and its methods

from message import Message

class Folder:
    # Initializes the folder with a name and a list of messages
    def __init__(self, name, messages=None):
        self.name = name
        self.messages = messages or []

    # Adds a message to the folder
    def add_message(self, message):
        self.messages.append(message)

    # Removes a message from the folder
    def remove_message(self, message_id):
        new_messages = []
        for msg in self.messages:
            if msg.id != message_id:
                new_messages.append(msg)
        self.messages = new_messages

    # Lists all the messages in the folder
    def list_messages(self):
        summaries = []
        for msg in self.messages:
            summaries.append(msg.display_summary())
        return summaries