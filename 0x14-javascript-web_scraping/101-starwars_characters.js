#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const filmsApiEndpoint = `https://swapi-api.alx-tools.com/api/films/${filmId}`;
let characters = [];

request(filmsApiEndpoint, (err, res, body) => {
  if (err) return;

  const responseContent = JSON.parse(body);
  characters = responseContent.characters;
  printCharacters(0);
});

function printCharacters (index) {
  if (index === characters.length) return;

  request(characters[index], (err, res, body) => {
    if (err) return;

    const responseContent = JSON.parse(body);
    console.log(responseContent.name);
    printCharacters(index + 1);
  });
}
