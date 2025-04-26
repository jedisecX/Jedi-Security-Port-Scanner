def print_banner():
    print("=" * 70)
    print("                   Jedi Security Port Scanner")
    print("-" * 70)
    print(" Official Domains:")
    print("  - jedi-sec.com")
    print("  - jedi-sec.us")
    print("  - jedi-sec.cloud")
    print("  - jedi-sec.online")
    print("  - jedi-sec.me")
    print("=" * 70)

# Display the banner when the script is executed
if __name__ == "__main__":
    print_banner()
    # ... rest of your script ...

import socket
import threading

# Target IP or domain
target = input("Enter target IP or domain: ")

# Ports to scan (example: 1 to 1024)
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

# Thread lock for printing results properly
print_lock = threading.Lock()

# Function to scan a single port
def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Short timeout for faster scanning
        result = sock.connect_ex((target, port))
        if result == 0:
            with print_lock:
                print(f"[+] Port {port} is OPEN")
        sock.close()
    except Exception as e:
        pass

# Main function to start threads
def main():
    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(port,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()