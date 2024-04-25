#!/bin/bash
# Sends json to server
curl -s -X POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
