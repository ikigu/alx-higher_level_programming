#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const webPage = process.argv[2];
const writeFile = process.argv[3];

request(webPage).pipe(fs.createWriteStream(writeFile, 'utf8'));
