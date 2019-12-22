# This Project Made by
#   Gemian Talasoun Sadek
#   Mohamed Gamal Nagem
#   Mohamed Fatehy Mohamed
#   Hassaan Nabil Hassan


import socket
from pip._vendor.distlib.compat import raw_input

client = socket.socket()
ipaddr = raw_input('Connect to IP: ')
client.connect((ipaddr, 3000))
print('Connected to server')
while True:
    phortxt = 0
    phortxt = int(raw_input('If you want to translate text file press "1", to translate phrase press "2": '))

    if phortxt == 1:
        file_path = ""
        file_path = str(raw_input('Enter file path: '))
        text = ""
        text = open(file_path)
        text = text.read()
        text = text[0:200]
        client.send(text.encode())
    elif phortxt == 2:
        phrase = ""
        phrase = raw_input('Enter your phrase: ')
        client.send(phrase.encode())
    else:
        print("your choice not correct.")
        client.close()
        break

    print('Translate To: \n\t1) Arabic\n\t2) English\n\t3) French\n\t4) Spanish\n')
    lang = 0
    lang = (int(raw_input("Enter number of language: ")))
    client.send(bytes(lang))

    print('Correct is :\n', client.recv(1024).decode(), '\n')
    print('Translate is:\n', client.recv(1024).decode(), '\n')
    print('Sentiment is :\n', bytes(client.recv(1024)), '\n')
    print('subjectivity is :\n', client.recv(1024).decode(), '\n')

    exit = 0
    exit = int(raw_input('If you want to continue press "1" to exit press "0" : '))
    if exit == 0:
        break
    elif exit == 1:
        continue
