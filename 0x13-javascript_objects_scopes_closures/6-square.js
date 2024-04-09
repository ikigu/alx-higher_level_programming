#!/usr/bin/node

const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c = 'X') {
    let i = 0;
    let stringToPrint = '';

    while (i < this.width) {
      stringToPrint += c;
      i++;
    }

    i = 0;

    while (i < this.height) {
      console.log(stringToPrint);
      i++;
    }
  }
}

module.exports = Square;
