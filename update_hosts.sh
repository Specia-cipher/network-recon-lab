#!/bin/bash

# Mapping container hostnames to their current IPs
declare -A container_ips=(
  [ftp-server]="172.19.0.3"
  [smb-server]="172.19.0.4"
  [vulbapp]="172.19.0.2"
  [attacker]="172.19.0.5"
  [linux-victim]="172.19.0.6"
  [juice-shop]="172.17.0.2"
)

echo "Updating /etc/hosts entries for containers..."

for host in "${!container_ips[@]}"
do
  ip="${container_ips[$host]}"
  # Check if entry exists
  if grep -q "$host" /etc/hosts; then
    sudo sed -i "/$host/d" /etc/hosts
  fi
  echo "$ip    $host.local" | sudo tee -a /etc/hosts
done

echo "Created/Updated /etc/hosts entries."

# Create/update targets file for automated scans
cat <<EOF > auto_recon_targets.txt
ftp-server.local
smb-server.local
vulbapp.local
attacker.local
linux-victim.local
juice-shop.local
EOF

echo "auto_recon_targets.txt file created/updated."
