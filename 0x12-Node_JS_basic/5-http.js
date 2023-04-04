const http = require('http');
const fs = require('fs');

const hostname = '127.0.0.1';
const port = 1245;

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  if (req.url === '/') {
    res.write('Hello Holberton School!');
  }
  if (req.url === '/students') {
    res.write('This is the list of our students\n');
    try {
      const data = fs.readFileSync(process.argv[2], 'utf8');
      const lines = data.split('\n');
      lines.shift();
      const studentsByField = {};
      let totalStudents = 0;
      for (const line of lines) {
        const lineArray = line.split(',');
        if (lineArray.length === 4) {
          totalStudents += 1;
          if (lineArray[3] in studentsByField) {
            studentsByField[lineArray[3]].push(lineArray[0]);
          } else {
            studentsByField[lineArray[3]] = [lineArray[0]];
          }
        }
      }
      res.write(`Number of students: ${totalStudents}\n`);
      let response = '';
      for (const field in studentsByField) {
        let studentsList = '';
        for (const student of studentsByField[field]) {
          if (studentsList.length > 0) {
            studentsList += ', ';
          }
          studentsList += student;
        }
        response += `Number of students in ${field}: ${studentsByField[field].length}. List: ${studentsList}\n`;
      }
      res.write(response.slice(0, -1));
    } catch (err) {
      res.write('Cannot load the database');
    }
  }
  res.end();
});

app.listen(port, hostname);

module.exports = app;
