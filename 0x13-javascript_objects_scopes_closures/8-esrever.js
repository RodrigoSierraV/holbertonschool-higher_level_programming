#!/usr/bin/node
exports.esrever = function (list) {
  let newlist = new Array;
  for (let i = list.length - 1; i >= 0; i--) {
    newlist.push(list[i]);
  }
  return newlist;
};
