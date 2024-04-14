#!/usr/bin/node
const request = require('request');
if (process.argv.length !== 2) {
  console.error('Expected at least one argument!');
  process.exit(1);
}
const filmApi = `https://swapi.dev/api/films/${process.argv[2]}/?format=json`;

request.get(filmApi, function (error, response, body) {
  if (error) {
    console.error('Error fetching film:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error('Failed to fetch film:', response.statusCode);
    return;
  }

  const characters = JSON.parse(body).characters;
  for (const character of characters) {
    request.get(character, function (ce, cr, cbody) {
      if (ce) {
        console.error('Error fetching character:', ce);
        return;
      }
      if (cr.statusCode !== 200) {
        console.error('Failed to fetch character:', cr.statusCode);
        return;
      }
      const name = JSON.parse(cbody).name;
      console.log(name);
    });
  }
});
