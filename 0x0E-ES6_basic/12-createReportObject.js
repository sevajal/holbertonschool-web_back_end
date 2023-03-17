export default function createReportObject(employeesList) {
  const reportObject = {
    allEmployees: employeesList,
    getNumberOfDepartments(object) {
      return Object.keys(object).length;
    },
  };
  return reportObject;
}
