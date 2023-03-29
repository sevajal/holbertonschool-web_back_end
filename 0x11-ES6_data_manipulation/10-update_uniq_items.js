export default function updateUniqueItems(argMap) {
  if (argMap instanceof Map) {
    for (const element of argMap) {
      if (element[1] === 1) {
        argMap.set(element[0], 100);
      }
    }
    return argMap;
  }
  throw Error('Cannot process');
}
