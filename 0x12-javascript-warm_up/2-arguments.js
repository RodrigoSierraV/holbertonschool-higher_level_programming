#!/usr/bin/node

const argslen = process.argv.length;
let response = '';
if (argslen === 2) {
  response = 'No argument';
} else if (argslen === 3) {
  response = 'Argument found';
} else {
  response = 'Arguments found';
}
console.log(response);
