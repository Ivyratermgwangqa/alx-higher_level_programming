#!/usr/bin/node

// 9-logme.js
let count = 0;

exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
