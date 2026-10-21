import socket


def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.settimeout(5)
            client.connect(("127.0.0.1", 8000))
            client.sendall(b"GET / HTTP/1.0\r\nHost: 127.0.0.1\r\n\r\n")

            data = []

            while True:
                chunk = client.recv(4096)
                if chunk == b"":
                    break
                data.append(chunk)
    
    
    except ConnectionRefusedError:
        print("Connection failed: server is not running.")
        return
    except socket.timeout:
        print("Connection timed out.")
        return
    except OSError as e:
        print(f"Network error: {e}")
        return
    
    response = b"".join(data)
    
    raw_headers, _, body = response.partition(b"\r\n\r\n")
    headers = raw_headers.decode("iso-8859-1")
    status_line = headers.splitlines()[0]
    status_code = int(status_line.split()[1])
    
    if 200 <= status_code <= 299:
        print("Request successful")
    else:
        print("Request failed") 

    print("Status:", status_line)
    print("HTTP Headers:")
    print(headers)
    print("\nHTML Body:")
    print(body.decode(errors="replace"))
    
if __name__ == "__main__":
    main()
