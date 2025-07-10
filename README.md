# 🛰️ Network Reconnaissance Lab

This lab simulates a real-world network environment for practicing **network reconnaissance**, enumeration, and automation using Python and Nmap. Designed as a modular playground for pentesters and bug bounty hunters.

---

## 📂 Project Structure

network-recon-lab/ ├── recon.py                # Automated Nmap scanning script ├── parse_nmap.py           # Parses Nmap output into summaries ├── dom_xss_checker.py      # Checks for DOM-based XSS in targets ├── auto_recon.py           # Chains recon tasks for multiple hosts ├── targets.txt             # List of target hosts/IPs ├── scan-results/           # Stores raw and parsed scan outputs │   ├── vulbapp_nmap.txt │   ├── smb-server_nmap.txt │   ├── ftp-server_nmap.txt │   ├── vulbapp_summary.txt │   └── ... └── cowrie-setup/           # Scripts for deploying Cowrie SSH honeypot

---

## 🚀 Lab Overview

This lab replicates the **Reconnaissance Phase** of a real penetration test. It includes:  

- Scanning simulated targets for open ports/services  
- Parsing scan results for key insights  
- A DOM-based XSS checker for web targets  
- Cowrie honeypot for SSH attack emulation  
- Modular Python automation to tie it all together  

---

## 🕵️‍♂️ How It Works

### 🔎 Reconnaissance Automation

The `recon.py` script uses Nmap to scan targets from `targets.txt`. It stores results in `scan-results/`.

```bash
python3 recon.py

📄 Sample Output (vulbapp_nmap.txt):

PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
80/tcp open  http    Apache httpd 2.4.41
139/tcp open  netbios-ssn Samba smbd 4.10.16
445/tcp open  microsoft-ds Samba smbd 4.10.16


---

📑 Parsing Nmap Results

For cleaner reports, run:

python3 parse_nmap.py

📄 Sample Summary (vulbapp_summary.txt):

Host: vulbapp.local (192.168.56.105)
Open Ports:
 - 21/tcp (ftp)
 - 80/tcp (http)
 - 445/tcp (Samba)


---

🕸️ DOM XSS Checker

Scan web apps for DOM-based XSS vectors:

python3 dom_xss_checker.py

📄 Sample Output:

Found potential DOM XSS in /app.js at line 45:
document.write(location.hash)


---

🐍 Cowrie SSH Honeypot

Cowrie deployed natively to log brute force SSH attacks and collect malware samples.

📄 Captured Logs:

2025-06-18 11:04:52 login attempt [root/123456] failed
2025-06-18 11:05:07 login attempt [admin/admin] succeeded


---

🎯 Learning Objectives

✅ Automate enumeration workflows with Python
✅ Gain hands-on experience with Nmap scanning and parsing
✅ Simulate attacker behaviors using honeypots
✅ Build reporting habits critical for penetration testing


---

⚡ Getting Started

1. Install prerequisites:

sudo apt update && sudo apt install nmap python3


2. Add target hosts to targets.txt.


3. Run scripts as needed from project root.




---

📖 Notes

🖥️ Environment: Backbox Linux VM (bare-metal, no containers)

⚠️ For educational purposes only. Do NOT run against networks you don’t own or have explicit permission to test.



---

✨ About the Author

Sanni Babatunde Idris
LinkedIn 🔗 • GitHub 🔗


---

© 2025 Sanni Babatunde Idris. All rights reserved.

---
