import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # Server's IP address
PORT = 12345        # Server's port

# Flag to indicate when the client is exiting
exiting = False

def receive_messages(client_socket):
    """Receive messages from the server."""
    global exiting
    print("Receive thread started.")
    while not exiting:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print("Connection closed by the server.")
                break
            print(message)
        except:
            if not exiting:
                print("An error occurred while receiving a message.")
            break
    print("Receive thread exiting.")

def send_messages(client_socket, username):
    """Send messages to the server."""
    global exiting
    print("Send thread started.")
    while not exiting:
        try:
            message = input()
            if message.lower() == 'exit':
                print("Exiting chat...")
                exiting = True
                client_socket.close()
                break
            full_message = f"{username}: {message}"
            client_socket.send(full_message.encode('utf-8'))
        except:
            if not exiting:
                print("An error occurred while sending a message.")
            break
    print("Send thread exiting.")

def start_client():
    """Start the chat client."""
    print("Welcome to the chat client!")
    username = input("Enter your username: ")
    print(f"Hello, {username}! Type 'exit' to leave the chat.")

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        
        # Send the username to the server
        client_socket.send(username.encode('utf-8'))
    except:
        print("Unable to connect to the server. Please try again later.")
        return

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    send_thread = threading.Thread(target=send_messages, args=(client_socket, username))

    receive_thread.start()
    send_thread.start()

    print("Threads started. You can now start chatting.")
    receive_thread.join()
    send_thread.join()
    print("Threads have finished. Exiting client.")

if __name__ == "__main__":
    start_client()