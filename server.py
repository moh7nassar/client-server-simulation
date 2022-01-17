import socket
from layers import *

HOST = '192.168.1.13'
# alt: HOST = 'localhost'

PORT = 9091
# should be unique (never been used before).

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

# "bind" is used for connecting (Hosting).

server.listen(5)
while True:
    communication_socket, address = server.accept()
    # used to communicate with clients.
    print(f"Connected to {address} \n")
    message = communication_socket.recv(1024).decode('utf-8')
    # messages should be decoded when received to appear in an understandable form.
    print("\nPhysical Layer: ", end="")
    physical_layer("server")
    print("\nData Link Layer: ", datalink_layer(message, "62.34.DF.3A.87.C9"), "\n")
    print("Network Layer: ", network_layer(message, HOST), "\n")
    print("Transport Layer: ", transport_layer(message, "TCP"), "\n")
    print("Session Layer: Building a session between Sender and Receiver...", "\n")
    print("Presentation Layer: ", presentation_layer(message, "server"), "\n")
    print("Application Layer: ", application_layer(message), "\n")

    print(f"Message Received From Client Is: {message}")
    communication_socket.send(f"Got your message! Thank you".encode('utf-8'))
    # messages should be encoded when sent to clients to approve acknowledgement.

    print(f"\nConnection with {address} ended!")



