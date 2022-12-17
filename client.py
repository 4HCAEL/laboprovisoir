import socket, multiprocessing

host = 'localhost'
port = 8000
nb_workers = 10

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(1)
    with multiprocessing.Pool(nb_workers) as pool:
        while True:
            conn, address = s.accept()
            pool.apply(handle, (conn, address))

def handle(conn, address):
    with conn:
        buff = conn.recv(512)
        message = buff.decode('utf-8')
        conn.sendall(f"echo : {message}".encode('utf-8'))
