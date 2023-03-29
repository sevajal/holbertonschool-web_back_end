export default function updateStudentGradeByCity(studentList, city, newGrades) {
  const studentsFromCity = studentList.filter((student) => student.location === city);
  const newStudentList = studentsFromCity.map((student) => {
    const newStudent = student;
    const newGrade = newGrades.filter((grade) => grade.studentId === student.id);
    if (newGrade[0]) {
      newStudent.grade = newGrade[0].grade;
    } else {
      newStudent.grade = 'N/A';
    }
    return newStudent;
  });
  return newStudentList;
}
