#!/usr/bin/node

const request = require('request');

const apiEndpoint = 'https://swapi-api.alx-tools.com/api/films';
const characterId = '18'

request(apiEndpoint, (error, response, body) => {
  if (error) return;

  const responseObject = JSON.parse(body).results;

  let movieCount = 0;

  for (let i = 0; i < responseObject.length; i++) {
    const searchCharacter = `https://swapi-api.alx-tools.com/api/people/${characterId}/`;

    if (responseObject[i].characters.includes(searchCharacter)) {
      movieCount++;
    }
  }

  console.log(movieCount);
});
