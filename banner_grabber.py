import socket
import sys

def banner_grabber(ip, port):
    try:
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        print("Banner: " + banner.decode().strip())
    except Exception as e:
        print("Error: " + str(e))
    finally:
        s.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python banner_grabber.py <ip> <port>")
        sys.exit(1)

    ip = sys.argv[1]
    port = int(sys.argv[2])
    banner_grabber(ip, port)
