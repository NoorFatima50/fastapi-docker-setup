#!/bin/bash
# Script: count_errors.sh
# Purpose: Count "error" lines in a log file

LOG_FILE="/home/hp/sample.log"

if [ ! -f "$LOG_FILE" ]; then
    echo "Log file not found: $LOG_FILE"
    exit 1
fi

error_count=0

while IFS= read -r line
do
    if echo "$line" | grep -iq "error"; then
        ((error_count++))
    fi
done < "$LOG_FILE"

echo "Total error lines found: $error_count"
