# Simple CLI interface to demonstrate BirdMail functionality
from src.storage import FileStorage
from src.folder import Folder
from src.email_client import EmailClient

def main():
    # Initialize the email system
    storage = FileStorage("data")
    inbox = Folder("inbox")
    sent = Folder("sent")
    trash = Folder("trash")
    client = EmailClient(storage, inbox, sent, trash)
    
    print("Welcome to Bird Mail!")
    
    while True:
        print("Choose an option:")
        print("1. Compose Email")
        print("2. Read Inbox")
        print("3. Delete Email")
        print("4. Mark Email as Read")
        print("5. View Sent Messages")
        print("6. View Trash")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == "1":
            compose_email(client)
        elif choice == "2":
            read_inbox(client)
        elif choice == "3":
            delete_email(client)
        elif choice == "4":
            mark_as_read(client)
        elif choice == "5":
            view_sent_messages(client)
        elif choice == "6":
            view_trash(client)
        elif choice == "7":
            print("Thank you for using BirdMail! Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-7.")

def compose_email(client):
    print("\nCompose Email:")
    
    from_addr = input("From: ").strip()
    if not from_addr:
        print("Error: From address is required!")
        return
    
    to_addr = input("To: ").strip()
    if not to_addr:
        print("Error: To address is required!")
        return
    
    subject = input("Subject: ").strip()
    if not subject:
        print("Error: Subject is required!")
        return
    
    body = input("Body: ").strip()
    if not body:
        print("Error: Body is required!")
        return
    
    try:
        message = client.compose_email(from_addr, to_addr, subject, body)
        print(f"Email sent successfully! Message ID: {message.id}")
    except Exception as e:
        print(f"Error sending email: {e}")

def read_inbox(client):
    print("\nInbox")
    try:
        messages = client.read_inbox()
        if not messages:
            print("Inbox is empty")
    except Exception as e:
        print(f"Error reading inbox: {e}")

def delete_email(client):
    print("\nDelete Email:")
    
    folder = input("Folder (inbox/sent/trash): ").strip().lower()
    if folder not in ["inbox", "sent", "trash"]:
        print("Error: Invalid folder! Use 'inbox', 'sent', or 'trash'")
        return
    
    message_id = input("Message ID: ").strip()
    if not message_id:
        print("Error: Message ID is required!")
        return
    
    try:
        client.delete_email(folder, message_id)
    except Exception as e:
        print(f"Error deleting email: {e}")

def mark_as_read(client):
    print("\nMark as Read:")
    
    folder = input("Folder (inbox/sent/trash): ").strip().lower()
    if folder not in ["inbox", "sent", "trash"]:
        print("Error: Invalid folder! Use 'inbox', 'sent', or 'trash'")
        return
    
    message_id = input("Message ID: ").strip()
    if not message_id:
        print("Error: Message ID is required!")
        return
    
    try:
        client.mark_as_read(folder, message_id)
    except Exception as e:
        print(f"Error marking email as read: {e}")

def view_sent_messages(client):
    print("\nSent Messages:")
    try:
        sent_messages = client.storage.load("sent")
        if not sent_messages:
            print("No sent messages")
        else:
            for message in sent_messages:
                print(f"{message.display_summary()}")
    except Exception as e:
        print(f"Error loading sent messages: {e}")

def view_trash(client):
    print("\nTrash:")
    try:
        trash_messages = client.storage.load("trash")
        if not trash_messages:
            print("Trash is empty")
        else:
            for message in trash_messages:
                print(f"{message.display_summary()}")
    except Exception as e:
        print(f"Error loading trash: {e}")

if __name__ == "__main__":
    main()
