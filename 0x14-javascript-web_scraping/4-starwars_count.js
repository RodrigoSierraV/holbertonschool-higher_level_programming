#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0;
const char = 'https://swapi.co/api/people/18/';
request(url, function (err, response, body) {
  if (err) console.log(err);
  else if (response.statusCode === 200) {
    for (const i of JSON.parse(body).results) {
      for (const x of i.characters) {
        if (x === char) count++;
      }
    }
    console.log(count);
  }
});
