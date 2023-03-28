export default function getStudentIdsSum(studentList) {
  const sumId = 0;
  return studentList.reduce(
    (sumIds, student) => sumIds + student.id, sumId,
  );
}
