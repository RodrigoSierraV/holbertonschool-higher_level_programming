#!/usr/bin/node

const arg = parseInt(process.argv[2]);
let ch = 'X';
if (arg) {
  for (let x = 0; x < (arg - 1); x++) {
    ch += 'X';
  }
  for (let z = 0; z < arg; z++) {
    console.log(ch);
  }
} else {
  console.log('Missing size');
}
