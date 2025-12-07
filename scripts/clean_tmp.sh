#!/bin/bash
# Script: clean_tmp.sh
# Purpose: Delete files older than 7 days from /tmp folder

find /tmp -type f -mtime +7 -exec rm -f {} \; 2>/dev/null
echo "Old temporary files cleaned from /tmp!"
