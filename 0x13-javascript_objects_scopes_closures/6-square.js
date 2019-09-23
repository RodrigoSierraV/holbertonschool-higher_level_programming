#!/usr/bin/node
const lastSquare = require('./5-square');
class Square extends lastSquare {
  charPrint (c) {
    const pattern = c || 'X';
    for (let i = 0; i < this.width; i++) {
      console.log(pattern.repeat(this.width));
    }
  }
}
module.exports = Square;
