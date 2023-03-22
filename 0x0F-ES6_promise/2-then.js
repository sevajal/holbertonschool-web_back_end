export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => {
      const myObj = {
        status: 200,
        body: 'success',
      };
      return (myObj);
    })
    .catch(() => Error())
    .finally(() => {
      console.log('Got a response from the API');
    });
}
