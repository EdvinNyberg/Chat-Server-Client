### README.md

# Chat Application

This is a simple chat application built using Python's 

socket and threading modules. It consists of a server and a client that allow multiple users to communicate with each other in real-time.

## Requirements

- Python 3.x
- ﻿sockets==1.0.0

## Usage

### Running the Server

1. Open a terminal.
2. Navigate to the directory containing `chat_server.py`.
3. Run the server script:
   ```sh
   python chat_server.py
   ```

### Running the Client

1. Open a terminal.
2. Navigate to the directory containing `chat_client.py`.
3. Run the client script:
   ```sh
   python chat_client.py
   ```
4. Enter your username when prompted.
5. Start chatting! Type 'exit' to leave the chat.

## Code Overview

### Server (`chat_server.py`)

- **Global Variables**:
  - 

clients

: List to keep track of connected clients.
  - 

client_threads

: List to keep track of client threads.
  - 

running

: Flag to indicate if the server is running.

- **Functions**:
  - 

broadcast(message, client_socket=None)

: Sends a message to all clients except the sender.
  - 

handle_client(client_socket, username)

: Handles communication with a connected client.
  - 

start_server()

: Starts the chat server and listens for incoming connections.
  - `stop_server()`: Stops the chat server gracefully.

### Client (`chat_client.py`)

- **Global Variables**:
  - 

exiting

: Flag to indicate when the client is exiting.

- **Functions**:
  - 

receive_messages(client_socket)

: Receives messages from the server.
  - 

send_messages(client_socket, username)

: Sends messages to the server.
  - 

start_client()

: Starts the chat client and connects to the server.

## Example

### Server Output

```
Server started on 127.0.0.1:12345
New connection from ('127.0.0.1', 54321)
Thread started for user1.
user1 has joined the chat.
Thread exiting for user1.
user1 has left the chat.
Server has shut down.
```

### Client Output

```
Welcome to the chat client!
Enter your username: user1
Hello, user1! Type 'exit' to leave the chat.
Threads started. You can now start chatting.
user1: Hello, world!
Exiting chat...
Receive thread exiting.
Send thread exiting.
Threads have finished. Exiting client.
```

## Graceful Shutdown

- **Server**: Press Enter in the terminal where the server is running to stop the server gracefully.
- **Client**: Type 'exit' in the client to close the connection and exit gracefully.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

This README provides an overview of the chat application, including how to run the server and client, a brief description of the code, and examples of the output.
