#!/bin/bash
# Displays the size of the body of the response from a URL

url=$1
response=$(curl -sI "$url" | grep 'Content-Length' | cut -d ':' -f 2)
echo "$response"