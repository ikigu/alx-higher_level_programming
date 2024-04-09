#!/usr/bin/node

const fs = require('fs');

const sourceFiles = [process.argv[2], process.argv[3]];
const destFile = process.argv[4];

for (const file of sourceFiles) {
  fs.readFile(file, 'utf8', (err, data) => {
    if (err) {
      console.log(err);
    }

    fs.appendFile(destFile, data, (err) => {
      if (err) {
        console.log(err);
      }
    });
  });
}
