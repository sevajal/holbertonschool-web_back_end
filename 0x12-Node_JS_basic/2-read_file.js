const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
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
    console.log(`Number of students: ${totalStudents}`);
    for (const field in studentsByField) {
      let studentsList = '';
      for (const student of studentsByField[field]) {
        if (studentsList.length > 0) {
          studentsList += ', ';
        }
        studentsList += student;
      }
      console.log(`Number of students in ${field}: ${studentsByField[field].length}. List: ${studentsList}`);
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
