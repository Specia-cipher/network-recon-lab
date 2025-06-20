#!/bin/bash
# Restart all containers that are currently exited

echo "Restarting all exited containers..."

exited_containers=$(docker ps -a -f "status=exited" -q)

if [ -z "$exited_containers" ]; then
  echo "No exited containers to restart."
else
  docker start $exited_containers
  echo "Restarted containers:"
  docker ps --filter "id=$(echo $exited_containers | tr ' ' ',')"
fi
