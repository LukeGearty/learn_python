import socket

# Function to read HTML content from a file
def load_html(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "<h1>404 Not Found</h1>"

# HTTP response headers
def create_http_response(body):
    return f"""\
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: {len(body)}

{body}
"""

# Create a socket (IPv4, TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to an address and port
host = '127.0.0.1'
port = 8080
server_socket.bind((host, port))

# Start listening for incoming connections
server_socket.listen(1)
print(f"Server running on http://{host}:{port}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    # Receive HTTP request
    request = client_socket.recv(1024).decode()
    print(f"Received request:\n{request}")

    # Load the HTML file content
    html_content = load_html("index.html")

    # Create HTTP response
    response = create_http_response(html_content)

    # Send the response
    client_socket.sendall(response.encode())

    # Close the client connection
    client_socket.close()
