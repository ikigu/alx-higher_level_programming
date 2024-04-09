#!/usr/bin/node

exports.esrever = function (list) {
  if (!list) return [];

  let i;
  const reversedList = [];

  for (i = list.length - 1; i > -1; i--) {
    reversedList.push(list[i]);
  }

  return reversedList;
};
