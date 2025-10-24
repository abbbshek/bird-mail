# BirdMail is an email app

The core intention was to apply and practice Python OOP 

## Features

- **Message Management**: Create, read, delete and mark emails as read
- **Folder System**: Inbox, Sent and Trash folders
- **Persistence**: JSON file storage for data persistence
- **Interactive CLI**: User friendly command line interface


## File Descriptions

### **Core Application Files**

#### `main.py`
- **Purpose**: Interactive command line interface for the email client
- **Features**: Menu driven navigation, input validation, user friendly prompts
- **Functions**: Compose emails, read inbox, delete messages, mark as read, view folders

#### `src/message.py`
- **Purpose**: Defines the Message class representing individual emails
- **Methods**: 
  - `mark_read()` / `mark_unread()` - Toggle read status
  - `display_summary()` - Format message for display
  - `to_dict()` / `from_dict()` - JSON serialization
- **Attributes**: ID, sender, recipient, subject, body, timestamp, read status, labels

#### `src/folder.py`
- **Purpose**: Manages collections of messages in memory
- **Methods**:
  - `add_message()` - Add message to folder
  - `remove_message()` - Remove message by ID
  - `list_messages()` - Get message summaries
- **Use Case**: Temporary message storage during application runtime

#### `src/storage.py`
- **Purpose**: Handles persistent storage using JSON files
- **Methods**:
  - `load(folder_name)` - Read messages from JSON file
  - `save(folder_name, messages)` - Write messages to JSON file
- **Features**: Error handling, file creation, data validation

#### `src/email_client.py`
- **Purpose**: Main business logic for email operations
- **Methods**:
  - `compose_email()` - Create and send new emails
  - `read_inbox()` - Display inbox messages
  - `delete_email()` - Move to trash or permanently delete
  - `mark_as_read()` - Mark messages as read
- **Features**: Input validation, error handling, folder management

#### `src/utils.py`
- **Purpose**: Utility functions for the application
- **Functions**:
  - `generate_id()` - Create unique message identifiers
  - `get_timestamp()` - Generate current timestamp
  - `message_summary()` - Format message for display

### **Data Files**

#### `data/inbox.json`
- **Purpose**: Stores received messages
- **Format**: JSON array of message objects
- **Content**: Messages from other users

#### `data/sent.json`
- **Purpose**: Stores sent messages
- **Format**: JSON array of message objects
- **Content**: Messages composed by the user

#### `data/trash.json`
- **Purpose**: Stores deleted messages
- **Format**: JSON array of message objects
- **Content**: Messages moved from inbox/sent


### **Available Operations**
1. **Compose Email** - Create and send new emails
2. **Read Inbox** - View all received messages
3. **Delete Email** - Move messages to trash or permanently delete
4. **Mark as Read** - Mark messages as read/unread
5. **View Sent Messages** - See all sent emails
6. **View Trash** - See deleted messages
7. **Exit** - Close the application

Run with `python main.py`