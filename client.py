import socket
from layers import *

HOST = '192.168.1.13'
# same as server. (same device)

PORT = 9091

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))
# "connect" is used to connect with the server.
# should connect to the same PORT and HOST of the server.
# HOST may change when different devices are used.

message = "Hello World!"

print("\nApplication Layer: ", application_layer(message), "\n")
print("Presentation Layer: ", presentation_layer(message, "client"), "\n")
print("Session Layer: Building a session between Sender and Receiver...", "\n")
print("Transport Layer: ", transport_layer(message, "TCP"), "\n")
print("Network Layer: ", network_layer(message, HOST), "\n")
print("Data Link Layer: ", datalink_layer(message, "62.34.DF.3A.87.C9"), "\n")
print("Physical Layer: ", end="")
physical_layer("client")
socket.send(message.encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))

