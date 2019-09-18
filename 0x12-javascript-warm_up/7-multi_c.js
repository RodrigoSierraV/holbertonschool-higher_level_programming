#!/usr/bin/node

const arg = parseInt(process.argv[2]);
if (arg) {
  const phrase = 'C is fun';
  for (let x = 0; x < arg; x++) {
    console.log(phrase);
  }
} else {
  console.log('Missing number of occurrences');
}
