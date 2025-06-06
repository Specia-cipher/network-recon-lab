# 🛰️ Network Reconnaissance Lab

This project simulates a small networked environment for practicing **network reconnaissance**, a foundational phase in penetration testing. It was built to strengthen my understanding of enumeration techniques using tools like **Nmap**, and to prepare for real-world scenarios like **internal network assessments** and **bug bounty engagements**.

---

## 📂 Project Structure

network-recon-lab/
├── recon.py # Automated Nmap scanning script
├── scan-results/ # Folder containing scan output for each host
│ ├── vulbapp_nmap.txt
│ ├── ftp-server_nmap.txt
│ ├── smb-server_nmap.txt
│ └── linux-victim_nmap.txt
├── .gitignore
└── README.md # You're here!


---

## 🚀 How It Works

1. Docker is used to simulate a mini internal lab with:
   - `vulbapp` – a deliberately vulnerable web app
   - `ftp-server` – exposes FTP services
   - `smb-server` – runs SMB for file sharing
   - `linux-victim` – a basic Linux target

2. `recon.py` performs an automated Nmap scan of each container using aggressive detection options:
   ```bash
   nmap -A -T4 target
🛠️ Technologies Used
Docker – For building and managing isolated lab containers

Nmap – The core reconnaissance tool used in the script

Python 3 – Automation using subprocess module

BackBox Linux – The project environment

📖 Learning Objectives
Practice network reconnaissance in a safe, offline environment

Automate enumeration using Python

Gain hands-on experience with common network protocols (FTP, SMB, HTTP)

Build habit of documenting findings — essential for pentesting and bug bounty reports

⚡ Getting Started
Run from the host machine after your containers are up:python3 recon.py

All results will be saved inside the scan-results/ folder.

🔍 Sample Output Snippet
From vulbapp_nmap.txt:

PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.41
|_http-title: VulnApp Login
...
💡 Next Steps
Add more services (e.g., DNS, MySQL) to expand the lab

Integrate vulnerability scanners like Nikto or OpenVAS

Write custom parsers to summarize Nmap results

📎 Related Projects
You can find my Vulnerable Bank App — a Dockerized web pentesting lab — as a companion project.

## 📄 Nmap Scan Parsing (New Feature)

To improve readability and reporting, this project now includes a parsing script that automatically extracts key information from raw Nmap scans and generates human-readable summaries.

### 🔧 How It Works
- The script `parse_nmap.py` reads raw `.txt` output files in the `scan-results/` directory.
- For each scan file (e.g., `vulbapp_nmap.txt`), it creates a corresponding summary file (e.g., `vulbapp_summary.txt`).
- Summaries include:
  - Host and IP information
  - Open ports and associated services
  - Basic version info of detected services

### 📁 File Structure (Updated)

network-recon-lab/
├── recon.py # Automated Nmap scanning script
├── parse_nmap.py # New! Script to extract summaries from scans
├── scan-results/ # Organized scan outputs
│ ├── vulbapp_nmap.txt # Full raw Nmap output
│ ├── vulbapp_summary.txt # Parsed summary output
│ └── ...
└── README.md # You're here!


### 🧪 Usage
```bash
python3 parse_nmap.py


🙋‍♂️ About Me
I'm a cybersecurity enthusiast currently focusing on:

Penetration testing

Bug bounty hunting

Building and automating lab environments

Follow my journey or connect on LinkedIn 🚀:https://www.linkedin.com/in/sanni-idris-89917a262/

📜 License
This project is open-sourced for educational and non-commercial use. Feel free to fork or suggest improvements.
