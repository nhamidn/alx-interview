#!/usr/bin/node
const request = require('request');
if (process.argv.length !== 2) {
  console.error('Expected at least one argument!');
  process.exit(1);
}
const film_api = `https://swapi.dev/api/films/${process.argv[2]}/?format=json`;

request.get(film_api, function (error, response, body) {
  const characters = JSON.parse(body).characters;
  for (const character of characters) {
    request.get(character, function (ce, cr, cbody) {
      const name = JSON.parse(cbody).name;
      console.log(name);
    });
  }
});
