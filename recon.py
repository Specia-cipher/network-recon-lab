import subprocess
import os

# Ensure the output directory exists
os.makedirs("scan-results", exist_ok=True)

# Updated IP addresses from `docker inspect`
targets = {
    "linux-victim": "172.19.0.3",
    "smb-server": "172.19.0.4",
    "vulbapp": "172.19.0.2",
    "ftp-server": "172.19.0.6"
}

for name, ip in targets.items():
    print(f"Scanning {name} ({ip})...")
    result = subprocess.run(["nmap", "-A", "-T4", "-oN", "-", ip], capture_output=True, text=True)
    output_path = f"scan-results/{name}_nmap.txt"
    with open(output_path, "w") as f:
        f.write(result.stdout)
    print(f"Scan of {name} saved to {output_path}")

print("\nRecon finished.")

