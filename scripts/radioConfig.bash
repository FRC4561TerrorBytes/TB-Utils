#!/usr/bin/env bash

set -euo pipefail

if [[ $# -ne 2 ]]; then
    echo "Usage: $0 <suffix> <key>"
    exit 1
fi

suffix="$1"
key="$2"

payload=$(printf '{"mode":"TEAM_ROBOT_RADIO","teamNumber":4561,"wpaKey6":"%s-%s","wpaKey24":"%s-%s"}' \
    "$key"  "$key")

curl --fail-with-body -X POST "http://192.168.69.1/configuration" \
    -H "Content-Type: application/json" \
    -d "$payload"
    
echo