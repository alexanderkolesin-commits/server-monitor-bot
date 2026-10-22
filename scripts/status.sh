#!/bin/bash
echo "Server: $(hostname)"
echo "Checked at: $(date '+%Y-%m-%d %H:%M:%S')"
echo "Time: $(uptime -p)"
echo "Memory:"
free -h
echo "Disk:"
df -h /
disk_usage=$(df -h / | tail -n 1 | awk '{print $5}' | tr -d %)
disk_threshold=80
if [ "$disk_usage" -ge "$disk_threshold" ]; then
	echo "Disk usage is high: $disk_usage%"
else
	echo "Disk usage is normal: $disk_usage%"
fi

