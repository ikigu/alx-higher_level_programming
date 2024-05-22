#!/usr/bin/node

const request = require('request');

const apiEndpoint = process.argv[2];

request(apiEndpoint, (error, response, body) => {
  if (error) return;

  const responseContent = JSON.parse(body);

  const summary = {};

  responseContent.forEach(todo => {
    if (todo.completed) {
      if (!summary[todo.userId]) {
        summary[todo.userId] = 0;
      }

      summary[todo.userId] += 1;
    }
  });
  console.log(summary);
});
