import subprocess
import os
import socket

# Ensure output directory exists
os.makedirs("scan-results", exist_ok=True)

def resolve_target(target):
    try:
        # Try resolving target to IP if it's a hostname
        ip = socket.gethostbyname(target)
        return ip
    except socket.gaierror:
        # If already an IP or failed to resolve, return as is
        return target

def run_nmap_scan(target, ip):
    print(f"Scanning {target} ({ip}) ...")
    result = subprocess.run(
        ["nmap", "-A", "-T4", "-oN", f"scan-results/{target}_nmap.txt", ip],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        print(f"Scan of {target} saved to scan-results/{target}_nmap.txt")
    else:
        print(f"Error scanning {target}: {result.stderr}")

def main():
    if not os.path.isfile("targets.txt"):
        print("Create a 'targets.txt' file with one target (IP or hostname) per line.")
        return
    
    with open("targets.txt") as f:
        targets = [line.strip() for line in f if line.strip()]
    
    for target in targets:
        ip = resolve_target(target)
        run_nmap_scan(target, ip)
    
    print("\nAll scans completed.")

if __name__ == "__main__":
    main()
