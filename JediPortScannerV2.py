def print_banner():
    print("=" * 70)
    print("                   Jedi Security Port Scanner V2")
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
from datetime import datetime

# List of common ports for Standard Scan
COMMON_PORTS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS",
    3306: "MySQL", 3389: "RDP"
}

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        sock.close()
        return result == 0
    except Exception:
        return False

def standard_scan(target):
    print(f"Starting Standard Scan on {target}...")
    for port, service in COMMON_PORTS.items():
        if scan_port(target, port):
            print(f"[OPEN] {port} ({service})")
    print("Standard Scan complete.")

def advanced_scan(target):
    print(f"Starting Advanced Full Scan on {target}...")
    for port in range(1, 65536):
        if scan_port(target, port):
            print(f"[OPEN] {port}")
    print("Advanced Full Scan complete.")

def main():
    target = input("Enter target IP or hostname: ")
    print("\nChoose Scan Type:")
    print("1. Standard Scan (common ports)")
    print("2. Advanced Full Scan (all ports)")
    choice = input("Enter choice (1 or 2): ").strip()

    start_time = datetime.now()

    if choice == '1':
        standard_scan(target)
    elif choice == '2':
        advanced_scan(target)
    else:
        print("Invalid choice. Exiting.")

    end_time = datetime.now()
    print(f"\nScan completed in {end_time - start_time}")

if __name__ == "__main__":
    main()