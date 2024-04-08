#!/usr/bin/node

const firstArgumentAsNumber = parseInt(process.argv[2]);

if (Number.isNaN(firstArgumentAsNumber)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${firstArgumentAsNumber}`);
}
