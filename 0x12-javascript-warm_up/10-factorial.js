#!/usr/bin/node

const firstArgumentAsNumber = parseInt(process.argv[2]);

function factorial (n) {
  if (n === 1 || Number.isNaN(n)) {
    return 1;
  }

  return n + factorial(n - 1);
}

console.log(factorial(firstArgumentAsNumber));
