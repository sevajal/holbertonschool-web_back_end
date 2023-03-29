export default function hasValuesFromArray(set, array) {
  for (const obj of array) {
    if (!set.has(obj)) {
      return false;
    }
  }
  return true;
}
