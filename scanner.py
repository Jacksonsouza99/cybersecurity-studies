import argparse
import socket
from concurrent.futures import ThreadPoolExecutor
from functools import partial

def scan_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            if s.connect_ex((target, port)) == 0:
                return port
    except OSError:
        pass
    return None

def service_name(port):
    try:
        return socket.getservbyport(port, "tcp")
    except OSError:
        return "unknown"


def main():
    parser = argparse.ArgumentParser(description="Simple TCP port scanner")
    parser.add_argument("target", help="IP or hostname (e.g 127.0.0.1)")
    parser.add_argument("-s","--start", type=int, default=1, help="first port")
    parser.add_argument("-e","--end", type=int, default=1024, help="last port")
    parser.add_argument("-w","--workers", type=int, default=100, help="threads")
    args = parser.parse_args()
    
    if args.workers <= 0:
        parser.error("workers must be greater than 0")
        
    
    
    if args.start < 1 or args.end > 65535 or args.start > args.end:
        parser.error("ports must be between 1 and 65535, and start <= end")
        
    try:
        ip = socket.gethostbyname(args.target)
    except socket.gaierror:
        parser.error(f"could not resolve {args.target}")   
        
        
    print(f"Scanning {args.target} ({ip})...")
    ports = range(args.start, args.end + 1)

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        results = executor.map(partial(scan_port, ip), ports)


    for port in results:
        if port is not None:
            print(f"Port {port} is OPEN {service_name(port)}")
    print("Scan complete.")
        
if __name__ == "__main__":
    main()
