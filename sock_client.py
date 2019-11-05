import socket
import time
from datetime import datetime


def play_ok(s):
    while True:
        dt = f'"{datetime.now():%Y%m%d_%H%M%S}.mp4"'
        # TODO: писати в папку з датою
        s.send(str.encode(f"ADD 1 FILE {dt} -vcodec libx264 -preset ultrafast\r\n"))
        recv_msg = s.recv(1024)
        if recv_msg.decode() == '202 ADD OK\r\n':
            print('Start rec -', {dt}, data)
        time.sleep(1801)
        s.send(b'REMOVE 1 FILE\r\n')
        recv_msg = s.recv(1024)
        if recv_msg.decode() == '202 REMOVE OK\r\n':
            print(f'{dt} saved!')
        else:
            print('Somethinh wrong!!2')


def play_failed(s):
    s.send(b'REMOVE 1 FILE\r\n')
    sock.send(b'CLEAR 1 \r\n')
    print('Internal server error')


if __name__ == "__main__":

    PORT = 5250
    HOST = 'localhost'
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        sock.send(b' PLAY 1-10 DECKLINK DEVICE 1 FORMAT 1080i5000\r\n')
        data = sock.recv(1024)
        print(data)
        if data.decode() == '202 PLAY OK\r\n':
            play_ok(sock)
        if data.decode() in ['500 FAILED\r\n', '501 PLAY FAILED\r\n']:
            play_failed(sock)

            # TODO: Перезапуск серверного приложения и клиента
