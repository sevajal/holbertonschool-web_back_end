import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, filename) {
  const user = signUpUser(firstName, lastName);
  const photo = uploadPhoto(filename);
  const promise = [];
  await user.then((value) => {
    promise.push({
      status: 'fulfilled',
      value,
    });
  })
    .catch((error) => {
      promise.push({
        status: 'rejected',
        value: `Error: ${error.message}`,
      });
    });
  await photo.then((value) => {
    promise.push({
      status: 'fullfilled',
      value,
    });
  })
    .catch((error) => {
      promise.push({
        status: 'rejected',
        value: `Error: ${error.message}`,
      });
    });
  return promise;
}
