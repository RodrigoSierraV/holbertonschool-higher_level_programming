#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    const pattern = 'X';
    for (let x = 0; x < this.height; x++) {
      console.log(pattern.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
