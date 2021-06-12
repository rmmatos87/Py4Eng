import socket

def Main():
    host = '10.0.0.140' # IP from HOST
    port = 42424 
    s = socket.socket()
    s.connect((host,port))
    message = raw_input("->") 
    while message != 'q':
        s.send(message)
        data = s.recv(1024)
        message = raw_input("->")
    s.close()

if __name__ == '__main__':
    Main()
