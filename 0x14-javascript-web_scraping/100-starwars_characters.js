#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
request(url, function (err, response, body) {
  if (err) console.log(err);
  else if (response.statusCode === 200) {
    for (const x of JSON.parse(body).characters) {
      request(x, function (err, response, body) {
        if (err) console.log(err);
        console.log(JSON.parse(body).name);
      });
    }
  }
});
