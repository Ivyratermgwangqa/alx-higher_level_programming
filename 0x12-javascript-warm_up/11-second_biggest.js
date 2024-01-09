#!/usr/bin/node
const args = process.argv.slice(2);
const numArgs = args.length;

if (numArgs <= 1) {
  console.log(0);
} else {
  const numbers = args.map(Number).sort((a, b) => b - a);
  console.log(numbers[1]);
}
