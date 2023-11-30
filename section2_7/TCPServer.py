from socket import *

servport = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', servport))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    conn, addr = serverSocket.accept()
    sentence = conn.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    conn.send(capitalizedSentence.encode())
    conn.close()
