#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i;
  let occurences = 0;

  for (i = 0; i < list.length; i++) {
    if (list[i] === searchElement) occurences++;
  }

  return occurences;
};
