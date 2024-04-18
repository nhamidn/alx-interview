#!/usr/bin/node
const request = require('request');
const filmApi = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request.get(filmApi, async (error, response, body) => {
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
    await new Promise((resolve, reject) => {
      request.get(character, (cerror, cresponse, cbody) => {
        if (cerror) {
          reject(cerror);
        }
        console.log(JSON.parse(cbody).name);
        resolve();
      });
    });
  }
});
