#!/usr/bin/node

const callMeMoby = function (x, theFunction) {
  let i = 0;

  while (i < x) {
    theFunction();
    i++;
  }
};

module.exports = { callMeMoby };
