import socket

HOST = "192.168.1.163"
PORT = 4444
# host = socket.gethostbyname(socket.gethostname()) #automatically get the IP address
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))

#start to listen for incoming connections
server.listen() #we can pass in an integer to limit connections, or leave it blank


while True:
    communication_socket, address = server.accept() #this returns another socket for communication and the address of the incoming connection

    print(f"Connected to {address}")
    message = communication_socket.recv(1024).decode('utf-8') #it takes in the buffer size. Sending message with sockets are encoded and must be decoded
    print(f"Message from client is {message}")
    communication_socket.send(f"Got your message! Thank you!".encode('utf-8'))
    communication_socket.close()
    print(f"Connection with {address} ended")