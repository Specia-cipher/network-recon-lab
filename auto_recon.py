import subprocess
import os

def run_nmap_scan(target):
    output_dir = "scan-results"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"{target}_nmap.txt")

    print(f"Running nmap scan on {target}...")
    # -A for aggressive, -T4 for faster scan, save output to file
    cmd = ["nmap", "-A", "-T4", "-oN", output_file, target]

    try:
        subprocess.run(cmd, check=True)
        print(f"Scan complete for {target}, saved to {output_file}")
    except subprocess.CalledProcessError:
        print(f"Error scanning {target}")

def main():
    targets_file = "auto_recon_targets.txt"
    if not os.path.isfile(targets_file):
        print(f"Targets file '{targets_file}' not found!")
        return

    with open(targets_file, "r") as f:
        targets = [line.strip() for line in f if line.strip()]

    for target in targets:
        run_nmap_scan(target)

if __name__ == "__main__":
    main()
