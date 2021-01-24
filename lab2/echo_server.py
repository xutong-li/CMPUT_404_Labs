#!/usr/bin/env python3
# Download from University of Alberta CMPUT404W21 eClass
import socket
import time

# define address & buffer size
HOST = ""
PORT = 8003
BUFFER_SIZE = 1024


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # instruct the OS to let us reuse the same bind port
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # bind socket to address
        s.bind((HOST, PORT))
        # set to listening mode
        s.listen(2)

        # continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)

            # recieve data, wait a bit, then send it back
            full_data = conn.recv(BUFFER_SIZE)
            print(full_data)
            time.sleep(0.5)
            conn.sendall(full_data)
            conn.close()


if __name__ == "__main__":
    main()
