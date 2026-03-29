import socket
import threading
from datetime import datetime

# Target details
target = input("Enter Target IP or Domain: ")
start_port = int(input("Start Port: "))
end_port = int(input("End Port: "))

print("\n[+] Scanning Target:", target)
print("[+] Time Started:", datetime.now())
print("-" * 50)

# Lock for thread-safe printing
lock = threading.Lock()

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        with lock:
            if result == 0:
                print(f"[OPEN] Port {port}")
                with open("scan_results.txt", "a") as f:
                    f.write(f"Port {port} is OPEN\n")
            else:
                print(f"[CLOSED] Port {port}")

        sock.close()

    except Exception as e:
        print(f"[ERROR] Port {port}: {e}")

# Multi-threading
threads = []

for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print("\n[+] Scanning Completed at:", datetime.now())