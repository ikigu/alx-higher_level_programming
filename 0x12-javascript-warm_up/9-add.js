#!/usr/bin/node

const firstArgumentAsNumber = parseInt(process.argv[2]);
const secondArgumentAsNumber = parseInt(process.argv[3]);

function add (a, b) {
  return a + b;
}

console.log(add(firstArgumentAsNumber, secondArgumentAsNumber));
