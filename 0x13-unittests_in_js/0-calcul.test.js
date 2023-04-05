const assert = require('assert');
const calculateNumber = require('./0-calcul')

describe('calculateNumber', () => {
  it('should return 4', () => {
      assert.equal(calculateNumber(3, 1), 4);
  });
  it('should return 5', () => {
      assert.equal(calculateNumber(1, 3.7), 5);
  });
  it('should also return 5', () => {
      assert.equal(calculateNumber(1.2, 3.7), 5);
  });
  it('should return 6', () => {
      assert.equal(calculateNumber(1.5, 3.7), 6);
  });
  it('should return 0', () => {
      assert.equal(calculateNumber(-1, 1), 0);
  });
  it('should return also 0', () => {
    assert.equal(calculateNumber(0, 0), 0);
});
});
