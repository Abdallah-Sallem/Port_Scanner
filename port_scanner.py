import socket

from concurrent.futures import ThreadPoolExecutor
target=input("Enter taget IP or domain: ")
start_port=int(input("Enter start port : "))
end_port=int(input("Enter end port : "))

def scan_port(port):

    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result=s.connect_ex((target,port))

        if result ==0:
            print(f"[+]port {port} is OPEN")
        s.close()
    except Exception as e:
        pass


print(f"Scanning ports from {start_port} to {end_port} on {target}...")

with ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(start_port,end_port+1):
        executor.submit(scan_port,port)