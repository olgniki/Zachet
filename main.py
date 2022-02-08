import telnetlib
import os

Host = input("Введите Ip адрес свитча: ")
Ping = os.system("ping -c 1 " + Host)

if Ping == 0:

    User = input("Username: ").encode()
    Password = input("Password: ").encode()
    tn = telnetlib.Telnet(Host)
    tn.read_until(b'Username:')
    tn.write(User + b'\n')
    tn.read_until(b'Password:')
    tn.write(Password + b'\n')

    tn.write(b'terminal length 512' + b'\n')
    inputCommand = input("Введите команду: ").encode()
    tn.write(inputCommand + b'\n')
    exitLine = input("Введите exit для завершения: ").encode()
    tn.write(exitLine + b'\n')
    showInf = tn.read_all().decode()
    print(showInf)

else:

    print(Host, "Недоступен")

