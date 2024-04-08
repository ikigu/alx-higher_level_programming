#!/usr/bin/node

function findSecondBiggest () {
  if (process.argv.length < 4) return console.log(0);

  const args = process.argv.slice(2);

  for (let i = 0; i < args.length; i++) {
    args[i] = parseInt(args[i]);
  }
  
  args.sort((a, b) => b - a);
  console.log(args[1]);
}

findSecondBiggest();
