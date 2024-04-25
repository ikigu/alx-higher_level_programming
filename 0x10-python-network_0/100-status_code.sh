#!/bin/bash
# Prints status code
curl -sI -o /dev/null -w "%{http_code}" "$1"
