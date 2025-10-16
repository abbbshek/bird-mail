Bird Mail initial build

Files and their functioning (plain text)

src/message.py
Purpose: Represents a single email/message object.
Current contents: Message class skeleton with fields for sender, recipient, subject, body, timestamp, read flag and labels; placeholder methods for mark_read(), mark_unread(), and display_summary().
How it will function later: Instances will encapsulate message data + behavior (marking read/unread, serialization to/from dict for storage). This is the canonical unit used throughout the app.

src/folder.py
Purpose: Represents a mail folder (Inbox, Sent, Trash).
Current contents: Folder class skeleton with name and messages attributes and placeholder methods add_message(), remove_message(), and list_messages().
How it will function later: Each Folder will own and manage a list of Message objects, handle ordering and folder-specific behavior, and call the storage layer to persist changes.

src/storage.py
Purpose: Abstracts file-based persistence (local JSON storage).
Current contents: FileStorage class skeleton with data_path attribute and placeholder load(folder_name) and save(folder_name, messages) methods.
How it will function later: FileStorage will read from and write to data/<folder_name>.json, converting between Message objects and serializable dicts. This abstraction allows swapping JSON for a DB later.

src/email_client.py
Purpose: High-level orchestrator (the app interface).
Current contents: EmailClient class skeleton that holds references to storage and three folder instances (inbox, sent, trash). Placeholder methods include compose_email(), read_inbox(), delete_email(), and mark_as_read().
How it will function later: EmailClient will implement user-facing operations (compose, read, delete, mark) by coordinating Message, Folder, and FileStorage. This is the class CLI/UI will call.

src/utils.py
Purpose: Small helper utilities used across the codebase.
Current contents: Implemented helpers: generate_id() (UUID generation), get_timestamp() (standard timestamp string), and message_summary() (compact summary string).
How it will function later: Utility functions will standardize ID/timestamp generation and common lightweight formatting so other modules remain clean.

data/inbox.json, data/sent.json, data/trash.json
Purpose: Local JSON files that simulate message storage (one file per folder).
Current contents: Each file contains a valid empty JSON array: [].
How they will function later: These files will persist serialized messages for each folder. FileStorage will read from and write to these files during program runs. (Note: when migrating to a DB, these files will be migrated or deprecated.)