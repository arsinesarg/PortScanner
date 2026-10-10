import argparse
from datetime import datetime
import socket
import sys
from concurrent.futures import ThreadPoolExecutor

def scan_port(target_ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            try:
                service = socket.getservbyport(port, "tcp")
            except:
                service = "unknown"
            print(f"[+] Port {port} is OPEN (Service: {service})")
            return port
        s.close()
    except Exception as e:
        pass
    return None

def main():
    parser = argparse.ArgumentParser(description="A simple multi-threaded TCP port scanner.")
    parser.add_argument("target", help="Target IP address or domain to scan")
    parser.add_argument("-p", "--ports", default="1-1024", help="Port range to scan, e.g., 1-1024 (default)")
    parser.add_argument("-t", "--threads", type=int, default=100, help="Number of threads (default: 100)")
    
    args = parser.parse_args()

    target_host = args.target
    
    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print(f"[-] Error: Could not resolve hostname {target_host}")
        sys.exit(1)

    try:
        port_range = args.ports.split("-")
        start_port = int(port_range[0])
        end_port = int(port_range[1])
    except (ValueError, IndexError):
        print("[-] Error: Invalid port range format. Use start-end (e.g., 1-1024)")
        sys.exit(1)

    print("-" * 50)
    print(f"Scanning target: {target_ip}")
    print(f"Time started: {datetime.now()}")
    print("-" * 50)

    open_ports = []

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = [executor.submit(scan_port, target_ip, port) for port in range(start_port, end_port + 1)]
        for future in futures:
            port = future.result()
            if port:
                open_ports.append(port)

    print("-" * 50)
    print(f"Scanning finished. Open ports found: {len(open_ports)}")
    print("-" * 50)

if __name__ == "__main__":
    main()