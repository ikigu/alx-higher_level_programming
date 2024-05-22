#!/usr/bin/node

const request = require('request');

const apiEndpoint = process.argv[2];
const characterId = "18";

request(apiEndpoint, (error, response, body) => {
  if (error) return;

  const responseObject = JSON.parse(body).results;

  let movieCount = 0;

  for (let i = 0; i < responseObject.length; i++) {
	responseObject[i].characters.forEach(character => {
	  if (character.includes(characterId)) {
		movieCount++;
	  }
	});
  }

  console.log(movieCount);
});
