import socket
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 9999))
    while True:
        response = client.recv(4096).decode()
        print(response)
        if "Disconnecting" in response:
            break
        command = input("Enter command: ")
        client.send(command.encode())
start_client()