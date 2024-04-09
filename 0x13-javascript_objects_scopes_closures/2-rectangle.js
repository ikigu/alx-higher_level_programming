#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w < 1 || h < 1 || !w || !h) {
      return;
    }

    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
