import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # Server's IP address
PORT = 12345        # Server's port

def receive_messages(client_socket):
    """Receive messages from the server."""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print("Connection closed by the server.")
                break
            print(message)
        except:
            print("An error occurred while receiving a message.")
            break

def send_messages(client_socket, username):
    """Send messages to the server."""
    while True:
        try:
            message = input()
            if message.lower() == 'exit':
                print("Exiting chat...")
                client_socket.close()
                break
            full_message = f"{username}: {message}"
            client_socket.send(full_message.encode('utf-8'))
        except:
            print("An error occurred while sending a message.")
            break

def start_client():
    """Start the chat client."""
    print("Welcome to the chat client!")
    username = input("Enter your username: ")
    print(f"Hello, {username}! Type 'exit' to leave the chat.")

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
    except:
        print("Unable to connect to the server. Please try again later.")
        return

    threading.Thread(target=receive_messages, args=(client_socket,)).start()
    threading.Thread(target=send_messages, args=(client_socket, username)).start()

if __name__ == "__main__":
    start_client()