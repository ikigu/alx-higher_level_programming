#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const filmsApiEndpoint = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

request(filmsApiEndpoint, (err, res, body) => {
  if (err) return;

  const responseContent = JSON.parse(body);

  responseContent.characters.forEach(characterURL => {
    request(characterURL, (err, res, body) => {
      if (err) return;

      const responseContent = JSON.parse(body);
      console.log(responseContent.name);
    });
  });
});
