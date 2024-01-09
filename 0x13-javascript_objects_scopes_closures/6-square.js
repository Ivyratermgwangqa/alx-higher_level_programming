<<<<<<< HEAD
#!/usr/bin/node

// 6-square.js
const Square = require('./5-square');

class Square extends Square {
  constructor(size) {
    super(size);
  }

  charPrint(c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
=======
#!/usr/bin/node

module.exports = class Square extends require('./5-square.js') {
  charPrint(c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) console.log(c.repeat(this.width));
    }
  }
};
>>>>>>> b12ba721fb7b163c8a2eeb16e13b84870a083eed
