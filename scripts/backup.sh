#!/bin/bash
# Script: backup.sh
# Purpose: Backup files from test_folder to backup_folder

SOURCE=~/test_folder
DEST=~/backup_folder

# Create backup folder if not exists
mkdir -p $DEST

# Copy all files
cp -r $SOURCE/* $DEST/

echo "Backup completed successfully!"
