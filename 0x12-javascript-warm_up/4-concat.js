#!/usr/bin/node

let arg1 = process.argv[2];
let arg2 = process.argv[3];
if (!arg1) {
  arg1 = 'undefined';
}
if (!arg2) {
  arg2 = 'undefined';
}
console.log(arg1 + ' is ' + arg2);
