#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const pattern = 'X';
    for (let x = 0; x < this.height; x++) {
      console.log(pattern.repeat(this.width));
    }
  }

  rotate () {
    const pivot = this.width;
    this.width = this.height;
    this.height = pivot;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Rectangle;
module.exports = Square;
