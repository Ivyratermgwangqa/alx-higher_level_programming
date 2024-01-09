#!/usr/bin/node

// 6-square.js
const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  constructor (size) {
    super(size);
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
