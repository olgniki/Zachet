import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
sock.connect(('localhost', 8080))  # подключемся к серверному сокету
sock.send(bytes(input("login:"),encoding='UTF-8'))  # отправляем сообщение
sock.send(bytes(input("password:"),encoding='UTF-8'))  # отправляем сообщение
data = sock.recv(1024)  # читаем ответ от серверного сокета
sock.close()  # закрываем соединение
print(data)