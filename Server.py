import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
sock.bind(('', 8080))  # связываем сокет с портом
sock.listen(10)  # указываем сколько может сокет принимать соединений
log_psw = {"User1": "password1", "User2": "password2"} # создаем словарь логин - пароль
print('Server is running, please, press ctrl+c to stop')

while True:
    conn: socket
    conn, addr = sock.accept()  # начинаем принимать соединения
    print('connected:', addr)  # информация о подключении
    login = conn.recv(1024).decode("utf-8", "ignore")  # принимаем данные от клиента
    password = conn.recv(1024).decode("utf-8", "ignore")  # принимаем данные от клиента
    print(login)
    print(password)
    if login in log_psw and log_psw[login] == password:
       print("WELCOME")
       conn.send(bytes('WELCOME', encoding='UTF-8'))
    else:
        print("Неверный логин и пароль")
        conn.send(bytes('not WELCOME', encoding='UTF-8'))  # отправляем сообщение клиенту
conn.close()  # закрываем соединение

