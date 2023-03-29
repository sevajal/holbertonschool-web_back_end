const weakMap = new WeakMap();

function queryAPI(endpoint) {
  let queries = weakMap.get(endpoint);
  if (queries === undefined) {
    queries = 1;
  } else {
    queries += 1;
  }
  if (queries >= 5) {
    throw new Error('Endpoint load is high');
  }
  weakMap.set(endpoint, queries);
}

export { queryAPI, weakMap };
