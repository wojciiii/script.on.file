#!/bin/bash

filename="$1"
directory=$(basename "$2")

echo "filename:${filename}"
echo "directory:${directory}"

# Run a local script:
echo "Implement me: \"${filename}\" \"${directory}\""
# or remote command:
# ssh -n 192.168.0.2 "/home/username/script.sh \"${filename}\" \"${directory}\""
