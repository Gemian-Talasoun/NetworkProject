# This Project Made by
#   Gemian Talasoun Sadek
#   Mohammed Gamal Nagem
#   Mohammed Fathy
#   Hassaan Nabel


import socket
from textblob import TextBlob, translate

server = socket.socket()
server.bind(('127.0.0.1', 3000))
print('Server ready at 127.0.0.1')
server.listen(1)
client, address = server.accept()
print('Got connection from', address)

while True:
    phrase = ""
    index_1 = 0
    correct_text = ""

    phrase = client.recv(1024)
    index_1 = client.recv(1024)

    blob = TextBlob(phrase.decode())
    correct_text = str(blob.correct())
    client.send(correct_text.encode())

    if index_1 == bytes(1):
        client.send(str(blob.translate(to="ar")).encode())
    elif index_1 == bytes(2):
        client.send(str(blob.translate(to="en")).encode())
    elif index_1 == bytes(3):
        client.send(str(blob.translate(to="fr")).encode())
    elif index_1 == bytes(4):
        client.send(str(blob.translate(to="es")).encode())
    else:
        client.send('your choice not correct.'.encode())

    continue
