#!/usr/bin/node

// 101-sorted.js
const { dict } = require('./101-data');

const sortedDict = Object.entries(dict).reduce((result, [id, occurrences]) => {
  result[occurrences] = result[occurrences] || [];
  result[occurrences].push(id);
  return result;
}, {});

console.log(sortedDict);
