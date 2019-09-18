#!/usr/bin/node

const arg1 = process.argv[2];
if (!arg1 || !parseInt(arg1)) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(arg1));
}
