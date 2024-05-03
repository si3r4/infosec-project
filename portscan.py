import socket
import sys

def banner_grabber(host, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((host, port))
        banner = s.recv(1024)
        return banner.decode().strip()
    except socket.error as e:
        return f"Error: {e}"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python banner_grabber.py <host> <port>")
    else:
        host = sys.argv[1]
        port = int(sys.argv[2])
        print(f"Banner for {host}:{port}: {banner_grabber(host, port)}")
