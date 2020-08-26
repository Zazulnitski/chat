import socket ,threading

class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def __init__(self, host = '127.0.0.1', port = 1234):
        self.sock.connect((host, port))

        read_thread = threading.Thread(target=self.read_socket)
        read_thread.daemon = True
        read_thread.start()

        self.username = str(input("Введите ваше имя: "))

        self.sock.send(self.username.encode('UTF-8'))

        while True:
            message = self.username + ': ' + str(input())
            self.sock.send(message.encode('UTF-8'))

    def read_socket(self):
        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            print(data.decode('UTF-8'))

if __name__  == '__main__':
    client = Client()
