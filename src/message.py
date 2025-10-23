# Defines the Message class and its methods

from utils import generate_id

class Message:
    def __init__(self, from_addr, to_addr, subject, body, timestamp, read=False, labels=None, id=None):
        self.id = id or generate_id()
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.subject = subject
        self.body = body
        self.timestamp = timestamp
        self.read = read
        self.labels = labels or []

    # Marks the message as read
    def mark_read(self):
        self.read = True

    # Marks the message as unread
    def mark_unread(self):
        self.read = False

    # Displays the summary of the message
    def display_summary(self):
        return (
            f"Subject: {self.subject} " 
            f"Sender: {self.from_addr} "
            f"Time: {self.timestamp} "
            f"Read: {self.read} "
        )
    
    # Converts the message to dictionary format to be saved in a folder
    def to_dict(self):
        return {
            "id": self.id,
            "from_addr": self.from_addr,
            "to_addr": self.to_addr,
            "subject": self.subject,
            "body": self.body,
            "timestamp": self.timestamp,
            "read": self.read,
            "labels": self.labels,
        }
    
    # Converts the dictionary format data from the storage to a message object for displaying. 
    @classmethod 
    def from_dict(cls, data):
        return cls(
            from_addr=data.get("from_addr"),
            to_addr=data.get("to_addr"),
            subject=data.get("subject"),
            body=data.get("body"),
            timestamp=data.get("timestamp"),
            read=data.get("read", False),
            labels=data.get("labels", []),
            id=data.get("id"),
        )