const assert = require('assert');
const calculateNumber = require('./1-calcul')

describe('calculateNumber', () => {
    it('sum should return 0 when both numbers are 0', () => {
        assert.equal(calculateNumber('SUM', 0, 0), 0);
    });
    it('sub should return 0 when both numbers are 0', () => {
      assert.equal(calculateNumber('SUBTRACT', 0, 0), 0);
    });
    it('div should return Error when both numbers are 0', () => {
      assert.equal(calculateNumber('DIVIDE', 0, 0), "Error");
    });
    it('sum should return 0 when numbers are opposite', () => {
        assert.equal(calculateNumber('SUM', 4, -4), 0);
    });
    it('sub should return positive when numbers are opposite', () => {
      assert.equal(calculateNumber('SUBTRACT', 4, -4), 8);
    });
    it('sub should return negative when numbers are opposite', () => {
      assert.equal(calculateNumber('SUBTRACT', -4, 4), -8);
    });
    it('div should return 1 when numbers are igual', () => {
      assert.equal(calculateNumber('DIVIDE', 4, 4), 1);
    });
    it('sum should return 6', () => {
        assert.equal(calculateNumber('SUM', 1.4, 4.5), 6);
    });
    it('sub should return -4', () => {
        assert.equal(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });
    it('div should return 0.2', () => {
        assert.equal(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });
});
