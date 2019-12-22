# This Project Made by
#   Gemian Talasoun Sadek
#   Mohamed Gamal Nagem
#   Mohamed Fatehy Mohamed
#   Hassaan Nabil Hassan


import socket
from textblob import TextBlob, translate
from textblob.classifiers import NaiveBayesClassifier

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
    current_lang = "en"

    phrase = client.recv(1024)
    index_1 = client.recv(1024)

    phrase = phrase.decode()
    blob = TextBlob(phrase)
    correct_text = str(blob.correct())
    current_lang = str(blob.detect_language())


    client.send(correct_text.encode())

    if index_1 == bytes(1):
        if current_lang == "ar":
            client.send("Your text is already Arabic.".encode())
        else:
            client.send(str(blob.translate(to="ar")).encode())
    elif index_1 == bytes(2):
        if current_lang == "en":
            client.send("Your text is already English.".encode())
        else:
            client.send(str(blob.translate(to="en")).encode())
    elif index_1 == bytes(3):
        if current_lang == "fr":
            client.send("Your text is already French.".encode())
        else:
            client.send(str(blob.translate(to="fr")).encode())
    elif index_1 == bytes(4):
        if current_lang == "es":
            client.send("Your text is already Spanish.".encode())
        else:
            client.send(str(blob.translate(to="es")).encode())
    else:
        client.send('your choice not correct.'.encode())

    client.send(str(blob.sentiment).encode())
    client.send(str(blob.subjectivity).encode())

    continue
