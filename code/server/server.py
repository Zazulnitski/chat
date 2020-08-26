import socket, threading, time

class Server:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []
    def __init__(self, host = '127.0.0.1', port = 1234):
        self.server_socket.bind((host, port))
        self.server_socket.listen(0)

    def accept_client(self, conn):
        username = conn.recv(1024)
        if username:
            self.connections.append([conn, username])
            print(username.decode('UTF-8') + ' join to chat')
        while True:
            data = (conn.recv(1024)).decode('UTF-8')

            for connection in self.connections:
                if conn != connection[0]:
                    connection[0].send(data.encode('UTF-8'))

            if not data:
                break

        self.server_socket.close()

    def run_sever(self):

        print('Server run ' + time.strftime("%d-%m-%Y %X"))
        while True:
            try:
                conn, address = self.server_socket.accept()
                threading_accept = threading.Thread(target=self.accept_client, args=[conn])
                threading_accept.daemon = True
                threading_accept.start()

            except Exception:
                print(Exception)
                print("Server stopped " + time.strftime("%d-%m-%Y %X") + '\n')
                break

    def logging(self):
        pass

if __name__ == '__main__':
    server = Server()
    server.run_sever()

