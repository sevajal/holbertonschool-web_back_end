const calculateNumber = require('./2-calcul_chai')
const expect = require('chai').expect

describe('calculateNumber', () => {
  it('sum should return 0 when both numbers are 0', () => {
    expect(calculateNumber('SUM', 0, 0)).to.equal(0);
  });
  it('sub should return 0 when both numbers are 0', () => {
    expect(calculateNumber('SUBTRACT', 0, 0)).to.equal(0);
  });
  it('div should return Error when both numbers are 0', () => {
    expect(calculateNumber('DIVIDE', 0, 0)).to.equal("Error");
  });
  it('sum should return 0 when numbers are opposite', () => {
    expect(calculateNumber('SUM', 4, -4)).to.equal(0);
  });
  it('sub should return positive when numbers are opposite', () => {
    expect(calculateNumber('SUBTRACT', 4, -4)).to.equal(8);
  });
  it('sub should return negative when numbers are opposite', () => {
    expect(calculateNumber('SUBTRACT', -4, 4)).to.equal(-8);
  });
  it('div should return 1 when numbers are igual', () => {
    expect(calculateNumber('DIVIDE', 4, 4)).to.equal(1);
  });
  it('sum should return 6', () => {
    expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
  });
  it('sub should return -4', () => {
    expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
  });
  it('div should return 0.2', () => {
    expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
  });
});
