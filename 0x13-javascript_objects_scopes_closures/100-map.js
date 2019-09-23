#!/usr/bin/node
const list = require('./100-data').list;
let index = 0;
const newlist = list.map(x => x * index++);
console.log(list);
console.log(newlist);
