from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive messages")
while True:
    message, address = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    print(f"Received: message = {message.decode()}")
    serverSocket.sendto(modifiedMessage.encode(), address)
