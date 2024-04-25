#!/bin/bash
# Displays the size of the body of the response from a URL
echo $(curl -sI "$1" | grep 'Content-Length' | cut -d ':' -f 2)