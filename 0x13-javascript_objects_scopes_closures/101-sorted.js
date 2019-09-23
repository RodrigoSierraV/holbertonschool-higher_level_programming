#!/usr/bin/node
const dict = require('./101-data').dict;
const newdict = {};
for (const i in dict) {
  if (!newdict[dict[i]]) {
    newdict[dict[i]] = [];
  }
  newdict[dict[i]].push(i);
}
console.log(newdict);
