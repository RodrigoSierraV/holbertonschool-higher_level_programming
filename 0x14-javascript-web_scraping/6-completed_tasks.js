#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const dict = {};
request(url, function (err, response, body) {
  if (err) console.log(err);
  else if (response.statusCode === 200) {
    for (const i of JSON.parse(body)) {
      if (!dict[i.userId]) dict[i.userId] = 0;
      if (i.completed === true) {
        dict[i.userId] += 1;
      }
    }
    console.log(dict);
  }
});
