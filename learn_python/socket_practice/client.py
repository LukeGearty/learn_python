import socket

HOST = "192.168.1.163" #same since we are on the same laptop as the server
PORT = 4444

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT)) #pass in a tuple of HOST, PORT

socket.send("Hello World!".encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))