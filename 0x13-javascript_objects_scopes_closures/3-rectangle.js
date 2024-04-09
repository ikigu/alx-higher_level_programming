#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w < 1 || h < 1 || !w || !h) {
      return;
    }

    this.width = w;
    this.height = h;
  }

  print () {
    let i = 0;
    let stringToPrint = '';

    while (i < this.width) {
      stringToPrint += 'X';
      i++;
    }

    i = 0;

    while (i < this.height) {
      console.log(stringToPrint);
      i++;
    }
  }
}

module.exports = Rectangle;
