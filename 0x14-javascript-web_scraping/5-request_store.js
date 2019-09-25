#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) console.log(err);
  else if (response.statusCode === 200) {
    const fs = require('fs');
    fs.writeFile(process.argv[3], body, 'utf8', (err) => {
      if (err) console.log(err);
    });
  }
});
