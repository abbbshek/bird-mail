# this file handles composing, reading, deleting, and marking emails
from message import Message
from utils import get_timestamp
from utils import generate_id

class EmailClient:
    # initializes the email client with the storage, inbox, sent, and trash folders
    def __init__(self, storage, inbox, sent, trash):
        self.storage = storage
        self.inbox = inbox
        self.sent = sent
        self.trash = trash

    def compose_email(self, from_addr, to_addr, subject, body):
        new_message = Message(
            from_addr=from_addr,
            to_addr=to_addr,
            subject=subject,
            body=body,
            timestamp=get_timestamp(),
            read=False,
            labels=[],
            id=generate_id(),
        )
        self.sent.add_message(new_message)
        self.storage.save("sent", self.sent.messages)
        return new_message

    def read_inbox(self):
        loaded_messages = self.storage.load("inbox")
        self.inbox.messages = loaded_messages
        
        if not loaded_messages:
            print("Inbox is empty")
            return loaded_messages
            
        for message in loaded_messages:
            print(message.display_summary())
        return loaded_messages

    def delete_email(self, folder, message_id):
        if folder == "inbox":
            target_folder = self.inbox
        elif folder == "sent":
            target_folder = self.sent
        elif folder == "trash":
            target_folder = self.trash
        else:
            print("Invalid folder")
            return
            
        found_message = None
        for message in target_folder.messages:
            if message.id == message_id:
                found_message = message
                break
                
        if found_message:
            target_folder.remove_message(message_id)
            self.trash.add_message(found_message)
            self.storage.save(folder, target_folder.messages)
            self.storage.save("trash", self.trash.messages)
            print(f"Message {message_id} moved to trash")
        else:
            print("Message not found")

    def mark_as_read(self, folder, message_id):
        if folder == "inbox":
            target_folder = self.inbox
        elif folder == "sent":
            target_folder = self.sent
        elif folder == "trash":
            target_folder = self.trash
        else:
            print("Invalid folder")
            return
            
        found_message = None
        for message in target_folder.messages:
            if message.id == message_id:
                found_message = message
                break
                
        if found_message:
            found_message.mark_read()
            self.storage.save(folder, target_folder.messages)
            print(f"Message {message_id} marked as read")
        else:
            print("Message not found")