#!/usr/bin/env sh
set -eu

SOURCE_DIR="${SOURCE_DIR:-/var/log}"
BACKUP_DIR="${BACKUP_DIR:-/tmp/devops-starter-backups}"
STAMP="$(date +%Y%m%d-%H%M%S)"

mkdir -p "$BACKUP_DIR"
tar -czf "$BACKUP_DIR/logs-$STAMP.tar.gz" "$SOURCE_DIR"
find "$BACKUP_DIR" -type f -name 'logs-*.tar.gz' -mtime +7 -delete

