#!/usr/bin/env python3
"""
Auto Recon - Chivita Premium ++ Edition
by GenCipher (https://github.com/Specia-cipher)

A modern recon tool that produces rich HTML and JSON reports.
"""

import subprocess
import os
import json
from pathlib import Path
from datetime import datetime
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# Output directory
OUTPUT_DIR = Path("scan-results")
OUTPUT_DIR.mkdir(exist_ok=True)


def run_nmap_scan(target):
    """Run aggressive Nmap scan and save outputs (TXT, JSON, HTML)."""
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    base_filename = OUTPUT_DIR / f"{target}_recon_{timestamp}"

    txt_file = f"{base_filename}.txt"
    xml_file = f"{base_filename}.xml"

    print(f"{Fore.YELLOW}[~] Running Nmap scan on {target}...{Style.RESET_ALL}")
    cmd = ["nmap", "-A", "-T4", "-oN", txt_file, "-oX", xml_file, target]

    try:
        subprocess.run(cmd, check=True)
        print(f"{Fore.GREEN}[✓] Scan complete: {txt_file}{Style.RESET_ALL}")

        # Parse results for JSON/HTML
        summary_data = parse_nmap_txt(txt_file)
        json_file = f"{base_filename}.json"
        html_file = f"{base_filename}.html"

        save_json(summary_data, json_file)
        save_html(summary_data, html_file)

    except subprocess.CalledProcessError:
        print(f"{Fore.RED}[!] Scan failed for {target}{Style.RESET_ALL}")


def parse_nmap_txt(txt_file):
    """Parse Nmap TXT output for open ports and services (lightweight)."""
    summary = {"target": Path(txt_file).stem, "ports": []}
    port_line_prefixes = ("PORT", "STATE", "SERVICE")
    with open(txt_file, "r") as f:
        for line in f:
            if any(proto in line for proto in ["/tcp", "/udp"]) and "open" in line:
                parts = line.strip().split()
                if len(parts) >= 3:
                    summary["ports"].append({
                        "port": parts[0],
                        "state": parts[1],
                        "service": parts[2]
                    })
    return summary


def save_json(data, json_file):
    """Save scan summary as JSON."""
    with open(json_file, "w") as f:
        json.dump(data, f, indent=4)
    print(f"{Fore.CYAN}[+] JSON summary saved: {json_file}{Style.RESET_ALL}")


def save_html(data, html_file):
    """Save scan summary as styled HTML report."""
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Recon Report - {data['target']}</title>
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #f4f4f9; color: #333; }}
            h1 {{ color: #444; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            th {{ background-color: #444; color: white; }}
            tr:nth-child(even) {{ background-color: #f2f2f2; }}
            footer {{ margin-top: 20px; font-size: 0.9em; color: #777; }}
        </style>
    </head>
    <body>
        <h1>Recon Report - {data['target']}</h1>
        <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        <h2>Open Ports & Services</h2>
        <table>
            <tr><th>Port</th><th>State</th><th>Service</th></tr>
    """
    for port in data["ports"]:
        html_content += f"<tr><td>{port['port']}</td><td>{port['state']}</td><td>{port['service']}</td></tr>\n"
    html_content += """
        </table>
        <footer>Auto Recon - Chivita Premium ++ Edition | by GenCipher</footer>
    </body>
    </html>
    """
    with open(html_file, "w") as f:
        f.write(html_content)
    print(f"{Fore.MAGENTA}[+] HTML summary saved: {html_file}{Style.RESET_ALL}")


def main():
    targets_file = "auto_recon_targets.txt"
    if not os.path.isfile(targets_file):
        print(f"{Fore.RED}[!] Targets file '{targets_file}' not found!{Style.RESET_ALL}")
        return

    with open(targets_file, "r") as f:
        targets = [line.strip() for line in f if line.strip()]

    for target in targets:
        run_nmap_scan(target)

    print(f"{Fore.GREEN}[✓] All scans completed and reports saved.{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
