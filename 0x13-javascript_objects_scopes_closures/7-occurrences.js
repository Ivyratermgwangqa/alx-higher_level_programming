#!/usr/bin/node

// 7-occurrences.js
exports.nbOccurences = function (list, searchElement) {
  return list.filter(element => element === searchElement).length;
};
