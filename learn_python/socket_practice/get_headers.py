import socket

#A program to help with an assignment
def get_headers():
    host = 'localhost' 
    port = 13331 
    
    #AF_INET, and SOCK_STREAM for the HTTP
    #https://stackoverflow.com/questions/1593946/what-is-af-inet-and-why-do-i-need-it
    #SOCK_STREAM is for TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    client_socket.connect((host, port))
    filename = "helloworld.html"
    request = f"GET /{filename} HTTP/1.1\r\nHost: localhost\r\nConnection: close\r\n\r\n"
    client_socket.send(request.encode())

    response = client_socket.recv(1024)
    
    headers = response.decode().split('\r\n\r\n')[0] #splitting based on the 
    print("Response Headers:")
    print(headers)


    client_socket.close()

if __name__ == "__main__":
    get_headers()
