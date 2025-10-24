# this file handles composing, reading, deleting, and marking emails
from src.message import Message
from src.utils import get_timestamp
from src.utils import generate_id

class EmailClient:
    # initializes the email client with the storage, inbox, sent, and trash folders
    def __init__(self, storage, inbox, sent, trash):
        self.storage = storage
        self.inbox = inbox
        self.sent = sent
        self.trash = trash

    def compose_email(self, from_addr, to_addr, subject, body):
        # Validate inputs
        if not from_addr or not from_addr.strip():
            raise ValueError("From address is required")
        if not to_addr or not to_addr.strip():
            raise ValueError("To address is required")
        if not subject or not subject.strip():
            raise ValueError("Subject is required")
        if not body or not body.strip():
            raise ValueError("Body is required")
        
        try:
            new_message = Message(
                from_addr=from_addr.strip(),
                to_addr=to_addr.strip(),
                subject=subject.strip(),
                body=body.strip(),
                timestamp=get_timestamp(),
                read=False,
                labels=[],
                id=generate_id(),
            )
            self.sent.add_message(new_message)
            self.storage.save("sent", self.sent.messages)
            return new_message
        except Exception as e:
            raise Exception(f"Failed to compose email: {e}")

    def read_inbox(self):
        try:
            loaded_messages = self.storage.load("inbox")
            self.inbox.messages = loaded_messages
            
            if not loaded_messages:
                print("📭 Inbox is empty")
                return loaded_messages
                
            for message in loaded_messages:
                print(message.display_summary())
            return loaded_messages
        except Exception as e:
            raise Exception(f"Failed to read inbox: {e}")

    def delete_email(self, folder, message_id):
        # Validate inputs
        if not folder or not folder.strip():
            raise ValueError("Folder name is required")
        if not message_id or not message_id.strip():
            raise ValueError("Message ID is required")
        
        folder = folder.strip().lower()
        message_id = message_id.strip()
        
        if folder not in ["inbox", "sent", "trash"]:
            raise ValueError("Invalid folder. Use 'inbox', 'sent', or 'trash'")
        
        try:
            # Load current messages for the target folder
            target_messages = self.storage.load(folder)
            
            found_message = None
            for message in target_messages:
                if message.id == message_id:
                    found_message = message
                    break
                    
            if found_message:
                # Remove message from target folder
                target_messages = [m for m in target_messages if m.id != message_id]
                
                # If deleting from trash, permanently delete
                if folder == "trash":
                    self.storage.save(folder, target_messages)
                    print(f"Message {message_id} permanently deleted from trash")
                else:
                    # Move to trash
                    trash_messages = self.storage.load("trash")
                    trash_messages.append(found_message)
                    self.storage.save(folder, target_messages)
                    self.storage.save("trash", trash_messages)
                    print(f"Message {message_id} moved to trash")
            else:
                print(f"Message {message_id} not found in {folder}")
        except Exception as e:
            raise Exception(f"Failed to delete email: {e}")

    def mark_as_read(self, folder, message_id):
        # Validate inputs
        if not folder or not folder.strip():
            raise ValueError("Folder name is required")
        if not message_id or not message_id.strip():
            raise ValueError("Message ID is required")
        
        folder = folder.strip().lower()
        message_id = message_id.strip()
        
        if folder not in ["inbox", "sent", "trash"]:
            raise ValueError("Invalid folder. Use 'inbox', 'sent', or 'trash'")
        
        try:
            # Load current messages for the target folder
            target_messages = self.storage.load(folder)
            
            found_message = None
            for message in target_messages:
                if message.id == message_id:
                    found_message = message
                    break
                    
            if found_message:
                found_message.mark_read()
                self.storage.save(folder, target_messages)
                print(f"Message {message_id} marked as read")
            else:
                print(f"Message {message_id} not found in {folder}")
        except Exception as e:
            raise Exception(f"Failed to mark email as read: {e}")