#!/usr/bin/env python3
"""
parse_nmap.py - Chivita Edition
by GenCipher (https://github.com/Specia-cipher)

Parses Nmap scan results and generates clean JSON and HTML summaries.
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    print("Colorama not installed. Run: pip install colorama")
    exit(1)

SCAN_RESULTS_DIR = Path("scan-results")

def parse_nmap_output(file_path):
    """Parse Nmap text output into structured data"""
    results = {
        "target": file_path.stem.replace("_nmap", ""),
        "date": datetime.now().isoformat(),
        "open_ports": []
    }

    port_pattern = re.compile(r"^\s*(\d+/tcp)\s+open\s+(\S+)\s*(.*)")
    with open(file_path, "r") as f:
        for line in f:
            match = port_pattern.match(line)
            if match:
                port_info = {
                    "port": match.group(1),
                    "service": match.group(2),
                    "details": match.group(3).strip()
                }
                results["open_ports"].append(port_info)
    return results

def save_json_summary(data, output_file):
    """Save parsed data as JSON"""
    with open(output_file, "w", encoding="utf-8") as jf:
        json.dump(data, jf, indent=4)
    print(f"{Fore.GREEN}[+] JSON summary saved: {output_file}{Style.RESET_ALL}")

def save_html_summary(data, output_file):
    """Save parsed data as HTML"""
    html = f"<html><head><title>Scan Summary for {data['target']}</title></head><body>"
    html += f"<h2>Scan Summary for {data['target']}</h2><p>Date: {data['date']}</p>"
    html += "<table border='1' cellpadding='5'><tr><th>Port</th><th>Service</th><th>Details</th></tr>"
    for port in data['open_ports']:
        html += f"<tr><td>{port['port']}</td><td>{port['service']}</td><td>{port['details']}</td></tr>"
    html += "</table></body></html>"

    with open(output_file, "w", encoding="utf-8") as hf:
        hf.write(html)
    print(f"{Fore.GREEN}[+] HTML summary saved: {output_file}{Style.RESET_ALL}")

def main():
    print(f"{Fore.CYAN}[*] Parsing Nmap results in '{SCAN_RESULTS_DIR}'...{Style.RESET_ALL}")
    nmap_files = list(SCAN_RESULTS_DIR.glob("*_nmap.txt"))

    if not nmap_files:
        print(f"{Fore.RED}[!] No Nmap result files found in '{SCAN_RESULTS_DIR}'{Style.RESET_ALL}")
        return

    for file in nmap_files:
        parsed_data = parse_nmap_output(file)
        json_file = file.with_name(file.stem.replace("_nmap", "_summary") + ".json")
        html_file = file.with_name(file.stem.replace("_nmap", "_summary") + ".html")
        save_json_summary(parsed_data, json_file)
        save_html_summary(parsed_data, html_file)

    print(f"{Fore.GREEN}[✓] All summaries generated successfully.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
