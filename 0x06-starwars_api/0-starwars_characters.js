#!/usr/bin/node

const request = require('request');
const baseurl = 'https://swapi-api.alx-tools.com/api/films/';

function fetch (url) {
  return new Promise((resolve, reject) => {
    request.get({ url, json: true }, (err, res, body) => {
      if (err) return reject(err);
      resolve(body);
    });
  });
}

async function fetchCharacters (filmId) {
  try {
    const film = await fetch(baseurl + filmId);
    for (const character of film.characters) {
      const characterData = await fetch(character);
      console.log(characterData.name);
    }
  } catch (err) {
    console.error(err);
  }
}

fetchCharacters(process.argv[2]);
