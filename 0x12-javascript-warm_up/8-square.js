#!/usr/bin/node

const firstArgumentAsNumber = parseInt(process.argv[2]);

if (Number.isNaN(firstArgumentAsNumber)) {
  console.log('Missing size');
} else {
  let stringToPrint = '';
  let x = 0;

  while (x < firstArgumentAsNumber) {
    stringToPrint += 'x';
    x++;
  }

  x = 0;

  while (x < firstArgumentAsNumber) {
    console.log(stringToPrint);
    x++;
  }
}
