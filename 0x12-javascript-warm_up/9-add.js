#!/usr/bin/node

const firstArgumentAsNumber = parseInt(process.argv[2]);
const secondArgumentAsNumber = parseInt(process.argv[3]);

function add(a, b) {
  console.log(a + b);
}

add(firstArgumentAsNumber, secondArgumentAsNumber);