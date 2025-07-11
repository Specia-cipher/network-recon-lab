# 🛰️ Network Reconnaissance Lab v2.0

Welcome to **Network Recon Lab**, a modular, multi-tool environment built for practicing **network reconnaissance** and basic enumeration techniques. This upgrade introduces **multi-threaded scanning**, cleaner automation workflows, and prepares the ground for a future **Recon Dashboard** UI.

---

## 📦 Features

- 🔥 **Modular tools**: Each script targets a specific reconnaissance or parsing task.
- ⚡ **Multi-threaded scans**: Faster, efficient network sweeps (via `auto_scan.py`).
- 📊 **Structured scan results**: Organized outputs in `scan-results/`, ready for parsing or reporting.
- 🕵️ **DOM XSS tester**: Uses Selenium to hunt DOM-based XSS vulnerabilities.
- 🛠️ **Update utilities**: Quickly refresh `/etc/hosts`, restart containers, or update targets list.
- ✅ **Termux friendly**: All tools tested on Termux, BackBox, and Ubuntu.

---

## 📂 Project Structure

network-recon-lab/ ├── auto_scan.py           # Multi-threaded Nmap automation ├── parse_nmap.py          # Parses raw Nmap output into summaries ├── dom_xss_checker.py     # Automated DOM XSS fuzzing ├── scan-results/          # Folder for all scan outputs ├── targets.txt            # List of targets for scanning ├── update_hosts.sh        # Utility: Update /etc/hosts with lab targets ├── restart-exited-containers.sh  # Utility: Restart stopped containers └── README.md              # You're here!

---

## ⚡ Quickstart

1. **Clone the repo:**
   ```bash
   git clone https://github.com/Specia-cipher/network-recon-lab.git
   cd network-recon-lab

2. Install dependencies:

Nmap

Python 3, pip packages: colorama, selenium

GeckoDriver (for dom_xss_checker.py)

(Optional) Docker for future dashboard integration



3. Add targets to targets.txt:

10.0.0.5
example.com
192.168.1.10


4. Run a scan:

python3 auto_scan.py --scan fast
python3 auto_scan.py --scan full


5. Parse results:

python3 parse_nmap.py


6. Test for DOM XSS:

python3 dom_xss_checker.py




---

📖 Usage Examples

🚀 Fast Nmap Scan

python3 auto_scan.py --scan fast

📊 Generate Summaries

python3 parse_nmap.py

🕷️ DOM XSS Fuzzing

python3 dom_xss_checker.py


---

🛠️ Termux Tips

> Yes, it works in Termux!
Install dependencies:



pkg install nmap python
pip install colorama selenium


---

📌 Next Up (v3 Roadmap)

🌐 Recon Dashboard: Web UI to view scan results in real time.

🐳 Docker support for one-command deployment.

📡 Integration of vulnerability scanners (Nikto, OpenVAS).

🧠 Smarter parsing: JSON, CSV, and PDF reports.



---

👨‍💻 About the Author

Built with passion by Sanni Idris (Specia-cipher) 🌍
A cybersecurity enthusiast and future DevSecOps Engineer.
"Luxury or Nothing."


---

📜 License

This project is open-sourced for educational and non-commercial use.
Feel free to fork, hack, and suggest improvements.

---
