const sqlite = require('sqlite');

async function setup() {
    const db = await sqlite.open('./db.sqlite');
}

setup();