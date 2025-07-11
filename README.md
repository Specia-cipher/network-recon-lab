🛰️ Network Recon Lab v2.0 – Chivita Edition A modular, multi-tool reconnaissance lab designed for hands-on mastery of network scanning, enumeration, and parsing workflows.

This upgrade introduces multi-threaded scanning, rich HTML/JSON reporting, and utility scripts for managing lab environments. Built for speed and clarity – from Termux mobile labs to full-blown BackBox VMs.


---

🚀 Quick Start

git clone https://github.com/Specia-cipher/network-recon-lab.git
cd network-recon-lab

# Install dependencies (Termux/Ubuntu)
pkg install nmap python
pip install colorama selenium

Add your targets:

echo "10.0.0.5" >> targets.txt
echo "example.com" >> targets.txt

Run a fast scan:

python3 auto_scan.py --scan fast --threads 5

Parse results:

python3 parse_nmap.py


---

🛠️ Tools Overview


---

1️⃣ Auto Scan Tool – Chivita Edition

Multi-threaded Nmap automation for fast, full, or UDP scans.

python3 auto_scan.py --scan full --threads 8 --file targets.txt

📦 Sample Output:

[~] Scanning example.com (93.184.216.34) with full scan...
[✓] Scan complete: scan-results/example.com_full_20250711-103000.txt

📑 Sample JSON Excerpt:

{
  "target": "example.com",
  "ports": [
    {"port": "22/tcp", "state": "open", "service": "ssh"},
    {"port": "80/tcp", "state": "open", "service": "http"}
  ]
}

🔖 Built with ❤️ by Sanni Idris


---

2️⃣ Auto Recon Tool – Premium++

Aggressive scans with beautiful HTML & JSON reports.

python3 auto_recon.py

📦 Generates:

TXT: scan-results/example.com_recon_<timestamp>.txt

JSON: scan-results/example.com_recon_<timestamp>.json

HTML: scan-results/example.com_recon_<timestamp>.html


📑 HTML Report Features:

Responsive tables

Timestamped summaries

Color-coded services


🔖 Built with ❤️ by Sanni Idris


---

3️⃣ Nmap Parser Tool – Chivita Edition

Parses raw Nmap outputs into clean JSON & HTML summaries.

python3 parse_nmap.py

📦 Output Example:

scan-results/target_summary.json

scan-results/target_summary.html


📑 Sample HTML View:

Port	Service	Details

443/tcp	https	Apache/2.4.29 (Ubuntu)
21/tcp	ftp	vsftpd 3.0.3


🔖 Built with ❤️ by Sanni Idris


---

🧰 Utility Scripts

4️⃣ Update Hosts Utility

Updates /etc/hosts with lab container IPs & generates auto_recon_targets.txt.

sudo bash update_hosts.sh

📦 Output:

Updated /etc/hosts entries.
auto_recon_targets.txt file created/updated.

5️⃣ Restart Exited Containers

Restarts all Docker containers in 'exited' state.

bash restart-exited-containers.sh

📦 Output:

Restarting all exited containers...
Restarted containers:
CONTAINER ID   IMAGE        STATUS
...

🔖 Built with ❤️ by Sanni Idris


---

🐧 Termux & BackBox Notes ✅ Fully tested on Termux, BackBox, and Ubuntu 22.04.
✅ Simulated environments supported (no Docker required).


---


---

👨‍💻 About the Author Built with ❤️ by Sanni Babatunde Idris

GitHub: Specia-cipher LinkedIn: Sanni Idris Gmail: sannifreelancer6779@gmail.com


---

📜 License This project is open-sourced for educational and non-commercial use. Fork. Hack. Share.

