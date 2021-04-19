from library import main
from socket import socket
from msgutils import recv_msg, send_msg
import os
import time


def send_recv_func(ip, port):
    with socket() as s:
        s.connect((ip, port))

        while True:
            msg=recv_msg(s)



            choice=input(msg)


            if choice.isnumeric() and int(choice)==0:
                send_msg(s,choice.encode())
                break
            send_msg(s, choice.encode())
        return




if __name__ == "__main__":
    send_recv_func("127.0.0.1", 33450)



