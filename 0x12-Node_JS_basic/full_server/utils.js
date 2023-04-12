const fs = require('fs');

async function readDatabase(path) {
  return new Promise((resolve, reject) => {
    try {
      const data = fs.readFile(path, 'utf8');
      const lines = data.split('\n');
      const studentsByField = {};
      lines.shift();
      for (const line of lines) {
        const lineArray = line.split(',');
        if (lineArray.length === 4) {
          if (lineArray[3] in studentsByField) {
            studentsByField[lineArray[3]].push(lineArray[0]);
          } else {
            studentsByField[lineArray[3]] = [lineArray[0]];
          }
        }
      }
      resolve(studentsByField);
    } catch (e) {
      reject(new Error('Cannot load the database'));
    }
  });
}

module.exports = readDatabase;
