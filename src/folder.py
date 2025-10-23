class Folder:
    def __init__(self, name, messages=None):
        self.name = name
        self.messages = messages or []

    def add_message(self, message):
        self.messages.append(message)

    def remove_message(self, message_id):
        new_messages = []
        for msg in self.messages:
            if msg.id != message_id:
                new_messages.append(msg)
        self.messages = new_messages

    def list_messages(self):
        summaries = []
        for msg in self.messages:
            summaries.append(msg.display_summary())
        return summaries