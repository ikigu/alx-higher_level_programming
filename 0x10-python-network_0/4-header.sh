#!/bin/bash
# takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response, a header variable X-School-User-Id must be sent with the value 98
curl -sL "$1" -H "X-School-User-Id: 98"
