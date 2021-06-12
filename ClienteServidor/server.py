import socket

def Main():
    # discover the IP from server
    host = '10.0.0.140'
    port = 42424
    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    c, addr = s.accept()
    while True:
        data = c.recv(1024)
        if not data:
            break
        data = str(data).upper()
        c.send(data)
    c.close()
if __name__ == '__main__':
    Main()
