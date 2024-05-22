#!/usr/bin/node

const request = require('request');

const apiEndpoint = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request(apiEndpoint, (error, response, body) => {
  if (error) return;

  console.log(JSON.parse(body).title);
});
