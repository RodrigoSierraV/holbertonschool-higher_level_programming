#!/usr/bin/node
const dict = require('./101-data').dict;
let newdict = {};
for (let i in dict) {
  if (!newdict[dict[i]]) {
    newdict[dict[i]] = []
  }
  newdict[dict[i]].push(i);
}
console.log(newdict);
