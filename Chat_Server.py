import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 12345        # Port to listen on

# List to keep track of connected clients
clients = []
client_threads = []

# Flag to indicate if the server is running
running = True

def broadcast(message, client_socket=None):
    """Send a message to all clients except the sender."""
    for client in clients:
        if client['socket'] != client_socket:
            try:
                client['socket'].send(message)
            except:
                client['socket'].close()
                clients.remove(client)

def handle_client(client_socket, username):
    """Handle communication with a connected client."""
    print(f"Thread started for {username}.")
    while running:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            broadcast(message, client_socket)
        except:
            break
    client_socket.close()
    clients.remove({'socket': client_socket, 'username': username})
    broadcast(f"{username} has left the chat.".encode('utf-8'), client_socket)
    print(f"Thread exiting for {username}.")

def start_server():
    """Start the chat server."""
    global running
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server started on {HOST}:{PORT}")

    while running:
        try:
            server_socket.settimeout(1)
            client_socket, client_address = server_socket.accept()
        except socket.timeout:
            continue
        except OSError:
            break

        print(f"New connection from {client_address}")
        
        # Receive the username from the client
        username = client_socket.recv(1024).decode('utf-8')
        clients.append({'socket': client_socket, 'username': username})
        
        # Notify all clients about the new user
        broadcast(f"{username} has joined the chat.".encode('utf-8'))
        
        client_thread = threading.Thread(target=handle_client, args=(client_socket, username))
        client_threads.append(client_thread)
        client_thread.start()

    # Close all client connections
    for client in clients:
        client['socket'].close()

    # Wait for all client threads to finish
    for thread in client_threads:
        thread.join()

    server_socket.close()
    print("Server has shut down.")

def stop_server():
    """Stop the chat server."""
    global running
    running = False

if __name__ == "__main__":
    try:
        server_thread = threading.Thread(target=start_server)
        server_thread.start()
        input("Press Enter to stop the server...\n")
        stop_server()
        server_thread.join()
    except KeyboardInterrupt:
        stop_server()
        server_thread.join()