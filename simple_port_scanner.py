import socket
import threading
from queue import Queue

# Define target and port range
TARGET = "scanme.nmap.org"  # Replace with desired IP or hostname
PORT_RANGE = 100            # Number of ports to scan
THREADS = 100               # Number of threads to use

# Thread-safe queue of ports to scan
queue = Queue()

# Thread lock for clean output
print_lock = threading.Lock()

def port_scan(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Timeout for response
            result = s.connect_ex((TARGET, port))
            if result == 0:
                with print_lock:
                    print(f"[+] Port {port} is open")
    except Exception as e:
        pass  # Ignore errors silently for speed

def fill_queue():
    for port in range(1, PORT_RANGE + 1):
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        port_scan(port)
        queue.task_done()

def main():
    print(f"[*] Starting scan on {TARGET}")
    fill_queue()

    threads = []
    for _ in range(THREADS):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("[*] Scan complete.")

if __name__ == "__main__":
    main()
