import socket 

# Create socket as an end point
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Make the connection
mysocket.connect(('data.pr4e.org', 80))
# Send HTTP GET Return+Newline x2 and encode in UTF-8
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
# Send request out
mysocket.send(cmd)

# Receive data until server close
while True:
    # recv : wait
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    # Convert to Unicode for Python printing
    print(data.decode(),end='')

mysocket.close()