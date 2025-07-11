#!/usr/bin/env python3
"""
Auto Recon - Chivita Edition
by GenCipher (https://github.com/Specia-cipher)

A modular and threaded network scanning tool for fast recon.
"""

import subprocess
import socket
import os
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
import argparse
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    print("Colorama not installed. Run: pip install colorama")
    exit(1)

# Global variables
OUTPUT_DIR = Path("scan-results")
OUTPUT_DIR.mkdir(exist_ok=True)

def resolve_target(target):
    """Resolve hostname to IP"""
    try:
        ip = socket.gethostbyname(target)
        print(f"{Fore.CYAN}[+] Resolved {target} to {ip}{Style.RESET_ALL}")
        return ip
    except socket.gaierror:
        print(f"{Fore.RED}[!] Could not resolve {target}. Using as is.{Style.RESET_ALL}")
        return target

def run_nmap_scan(target, scan_type="fast"):
    """Run an Nmap scan on a single target"""
    ip = resolve_target(target)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_file = OUTPUT_DIR / f"{target}_{scan_type}_{timestamp}.txt"
    flags = {
        "fast": ["-T4", "--top-ports", "100"],
        "full": ["-A", "-T4"],
        "udp": ["-sU", "-T4"]
    }

    cmd = ["nmap"] + flags.get(scan_type, ["-T4"]) + ["-oN", str(output_file), ip]
    print(f"{Fore.YELLOW}[~] Scanning {target} ({ip}) with {scan_type} scan...{Style.RESET_ALL}")

    try:
        subprocess.run(cmd, check=True)
        print(f"{Fore.GREEN}[✓] Scan complete: {output_file}{Style.RESET_ALL}")
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}[!] Scan failed for {target}{Style.RESET_ALL}")

def load_targets(file_path):
    """Load targets from file"""
    if not Path(file_path).is_file():
        print(f"{Fore.RED}[!] Targets file '{file_path}' not found!{Style.RESET_ALL}")
        return []
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]

def threaded_scans(targets, scan_type, threads):
    """Run scans in parallel"""
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(run_nmap_scan, t, scan_type): t for t in targets}
        for future in as_completed(futures):
            target = futures[future]
            try:
                future.result()
            except Exception as e:
                print(f"{Fore.RED}[!] Error scanning {target}: {e}{Style.RESET_ALL}")

def main():
    parser = argparse.ArgumentParser(description="Auto Recon - Chivita Edition")
    parser.add_argument("-f", "--file", default="targets.txt",
                        help="File with list of targets (default: targets.txt)")
    parser.add_argument("-t", "--threads", type=int, default=4,
                        help="Number of parallel scans (default: 4)")
    parser.add_argument("-s", "--scan", choices=["fast", "full", "udp"], default="fast",
                        help="Scan type: fast, full, udp (default: fast)")
    args = parser.parse_args()

    targets = load_targets(args.file)
    if not targets:
        print(f"{Fore.RED}[!] No targets found. Exiting.{Style.RESET_ALL}")
        return

    print(f"{Fore.MAGENTA}[*] Starting {args.scan} scans on {len(targets)} targets using {args.threads} threads...{Style.RESET_ALL}")
    threaded_scans(targets, args.scan, args.threads)
    print(f"{Fore.GREEN}[✓] All scans completed.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
