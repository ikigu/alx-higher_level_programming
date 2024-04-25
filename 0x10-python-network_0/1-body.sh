#!/bin/bash
# Display the response body of requested URL
if [ "$(curl -s -o response.txt -w "%{response_code}" "$1")" == "200" ]; then cat response.txt; fi
