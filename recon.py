import subprocess

targets = ["vulbapp", "ftp-server", "smb-server", "linux-victim"]

def run_nmap(target):
    print(f"Scanning {target}...")
    result = subprocess.run(["nmap", "-sV", target], capture_output=True, text=True)
    with open(f"{target}_nmap.txt", "w") as f:
        f.write(result.stdout)
    print(f"Scan of {target} saved to {target}_nmap.txt")

def main():
    print("Starting network reconnaissance...\n")
    for target in targets:
        run_nmap(target)
    print("\nRecon finished.")

if __name__ == "__main__":
    main()
