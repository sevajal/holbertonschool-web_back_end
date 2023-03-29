export default function cleanSet(set, startString) {
  let result = '';
  if (typeof (startString) === 'undefined' || startString.length === 0) {
    return result;
  }
  for (const element of set) {
    if (element && element.substring(0, startString.length) === startString) {
      if (result.length > 0) {
        result += '-';
      }
      result += element.substring(startString.length);
    }
  }
  return result;
}
