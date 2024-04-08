#!/usr/bin/node

const firstArgumentAsNumber = parseInt(process.argv[2]);

if (Number.isNaN(firstArgumentAsNumber)) {
  console.log('Missing number of occurences');
} else {
  let x = 0;

  while (x < firstArgumentAsNumber) {
    console.log('C is fun');
    x++;
  }
}
