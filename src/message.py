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

    def mark_read(self):
        self.read = True

    def mark_unread(self):
        self.read = False

    def display_summary(self):
        return (
            f"Subject: {self.subject}\n"
            f"Sender: {self.from_addr}\n"
            f"Time: {self.timestamp}\n"
            f"Read: {self.read}"
        )
    
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
    
    @classmethod 
    def from_dict(cls, d):
        return cls(
            from_addr=d.get("from_addr"),
            to_addr=d.get("to_addr"),
            subject=d.get("subject"),
            body=d.get("body"),
            timestamp=d.get("timestamp"),
            read=d.get("read", False),
            labels=d.get("labels", []),
            id=d.get("id"),
        )