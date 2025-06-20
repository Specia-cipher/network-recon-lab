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
# Dionaea Honeypot Setup & Initial Troubleshooting Log

This document chronicles the installation and initial configuration challenges encountered while setting up the Dionaea honeypot, including solutions and current status.

## Project Goal

The primary goal is to successfully deploy and configure Dionaea to emulate various services (SSH, HTTP, Telnet, SMB, etc.) on a dedicated VM, log attack attempts, and store captured malware/interactions for analysis.

## Environment

* **Operating System:** Ubuntu Desktop (likely 20.04 LTS or similar) running in VirtualBox.
* **Dionaea Version:** (Specify if known, otherwise assume latest from source build)
* **VM IP Address:** 10.0.2.15 (This is the target IP for external interactions)

## Installation Summary

Dionaea was installed from source, likely following standard build instructions (e.g., installing dependencies, compiling, `make install`). The installation path is `/opt/dionaea`.

## Initial Configuration & Challenges Faced

### 1. `sqlite3` Database Issues ("Killed" Process)

* **Symptom:** When attempting to interact with the `dionaea.sqlite` database using `sudo sqlite3 dionaea.sqlite`, the process would be "Killed" unexpectedly.
* **Diagnosis (Hypothesis):** This behavior is often indicative of the system running out of memory (OOM Killer) when the `sqlite3` process tries to load the database, especially if the VM has limited RAM.
* **Resolution:** (Mention if you increased VM RAM, or if it was a transient issue you worked around.)
* **Status:** Workaround found / resolved for now, allowing database interaction.

### 2. `emu` Module Preventing Dionaea Startup

* **Symptom:** Dionaea would fail to start or crash immediately, with log messages pointing to issues with the `emu` module or `filter_emu`.
* **Diagnosis:** The `emu` (emulation) module can sometimes be problematic or have dependencies not fully met in certain environments.
* **Resolution:**
    * Edited `/opt/dionaea/etc/dionaea/dionaea.cfg`.
    * Commented out `emu` from the `modules` line in the `[dionaea]` section.
    * Commented out `filter_emu` from the `processors` line.
* **Status:** Dionaea could then start, but other issues persisted.

### 3. "Connection Refused" for Key Honeypot Services (SSH, HTTP, Telnet, SMB)

* **Symptom:** When attempting to connect to the Dionaea VM's IP (10.0.2.15) on standard honeypot ports (e.g., `ssh 10.0.2.15`, `curl http://10.0.2.15`, `telnet 10.0.2.15 23`), the connection was immediately refused.
* **Initial Checks:**
    * Confirmed Dionaea process was running (`ps aux | grep -i dionaea`).
    * Checked network connectivity (VM IP was correct).
* **Key Diagnostic Tool:** `sudo ss -tuln` (checked active listening ports).
* **Critical Finding:** The `ss -tuln` output revealed that Dionaea was **NOT** listening on TCP ports 22 (SSH), 23 (Telnet), 80 (HTTP), or 445 (SMB). It *was* listening on:
    * **TCP:** 27017 (MongoDB - likely for internal logging)
    * **UDP:** 53 (DNS), 69 (TFTP), 111 (RPC), 123 (NTP), 1900 (SSDP), 5060 (SIP)
    * This confirmed that while Dionaea was running, it was not successfully binding to the intended honeypot TCP ports.
* **Attempted Solution (Latest):**
    * Edited `/opt/dionaea/etc/dionaea/dionaea.cfg` again.
    * Modified the `[listen]` section to explicitly bind to the VM's IP:
        ```ini
        [listen]
        # ... other comments ...
        # listen.mode=getifaddrs  <-- COMMENTED OUT
        listen.mode=manual       <-- SET TO MANUAL
        listen.addresses=["10.0.2.15"] # <-- UNCOMMENTED AND SET TO VM IP
        # ... rest of section ...
        ```
* **Current Status of this issue:** The configuration change has been applied.

### 4. Dionaea Silent Startup After Latest Config Change

* **Symptom:** After applying the `listen.mode=manual` change and attempting to restart Dionaea, no startup messages or "cleaning internal updates" output appeared on the console. The process seemed to start silently.
* **Diagnosis:** This usually indicates a critical error preventing full initialization, potentially a syntax error in the configuration or a new binding conflict.
* **Current State:** Dionaea process status after this change needs to be verified (`ps aux`) and its log file (`/opt/dionaea/var/log/dionaea/dionaea.log`) needs to be thoroughly checked for any errors or messages. The `ss -tuln` output after a successful (even if silent) startup is also pending.

## Next Steps (When resuming work)

1.  **Diagnose Silent Startup:**
    * Verify if Dionaea is actually running (`sudo ps aux | grep -i dionaea`).
    * Check `/opt/dionaea/var/log/dionaea/dionaea.log` for any error messages or output from the silent startup.
    * If no logs, re-verify `dionaea.cfg` for any syntax errors in the `[listen]` section.
2.  **Verify Port Bindings:** Once Dionaea starts successfully (with output or silent), run `sudo ss -tuln` to confirm that SSH, HTTP, Telnet, and SMB (and other configured services) are now listening on `10.0.2.15`.
3.  **Test Active Services:** Continue interacting with the currently listening services (MongoDB 27017, UDP 53, 69, 111, 123, 1900, 5060) to generate activity and confirm logging into `dionaea.log` and `dionaea.sqlite`


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

🐍 Cowrie SSH Honeypot (New Component)
To simulate real-world attack patterns and unauthorized SSH access attempts, the lab now includes a Cowrie honeypot container.

🛠️ Features
Emulates an interactive SSH server (and optionally Telnet)

Logs attacker keystrokes, commands, and download attempts

Captures unauthorized login attempts with full session transcripts

Stores downloaded payloads for offline malware analysis

⚙️ Setup Overview
Cowrie was set up inside a dedicated Docker container with the following configuration:

SSH port: 2222

Fake filesystem and command interface

Output logs stored locally for review and analysis

🔍 Example Logs
Captured events include:

Failed SSH login attempts

Commands issued by simulated attackers

Attempts to download or exfiltrate data

Sample log entry:

pgsql
Copy
Edit
2025-06-18T11:04:52+0000 [SSHService ssh-userauth on HoneyPotSSHTransport,0,192.168.1.105] login attempt [root/123456] failed
📂 File Locations
Cowrie logs: cowrie/var/log/cowrie.log

Payloads: cowrie/dl/

Config: cowrie/etc/cowrie.cfg

🎯 Purpose
Including Cowrie in the recon lab allows testing of:

Alerting and log review processes

Incident detection response workflows

Behavioral analysis of brute-force scripts and bots




🙋‍♂️ About Me
I'm a cybersecurity enthusiast currently focusing on:

Penetration testing

Bug bounty hunting

Building and automating lab environments

Follow my journey or connect on LinkedIn 🚀:https://www.linkedin.com/in/sanni-idris-89917a262/

📜 License
This project is open-sourced for educational and non-commercial use. Feel free to fork or suggest improvements.
