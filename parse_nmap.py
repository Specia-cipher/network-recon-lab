import os
import re

SCAN_RESULTS_DIR = "scan-results"

def parse_nmap_output(file_path):
    summary_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
    
    target_name = os.path.basename(file_path).replace("_nmap.txt", "")
    summary_lines.append(f"Summary for {target_name}:\n")
    summary_lines.append("Open ports and services:\n")

    # Updated regex pattern for port/service matching
    port_line_pattern = re.compile(r"^\s*(\d+/tcp)\s+open\s+(\S+)(?:\s+(.*))?")
    for line in lines:
        match = port_line_pattern.match(line)
        if match:
            port = match.group(1)
            service = match.group(2)
            extra_info = match.group(3) if match.group(3) else ""
            summary_lines.append(f"  - Port {port}: {service} {extra_info}".strip())
    
    summary_lines.append("\n")
    return "\n".join(summary_lines)

def main():
    files = [f for f in os.listdir(SCAN_RESULTS_DIR) if f.endswith("_nmap.txt")]
    for file in files:
        file_path = os.path.join(SCAN_RESULTS_DIR, file)
        summary = parse_nmap_output(file_path)
        summary_file = os.path.join(SCAN_RESULTS_DIR, file.replace("_nmap.txt", "_summary.txt"))
        with open(summary_file, "w") as sf:
            sf.write(summary)
        print(f"Summary written to {summary_file}")

if __name__ == "__main__":
    main()

