const expect = require('chai').expect
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', function() {
  let consoleSpy;
  beforeEach(() => {
    consoleSpy = sinon.spy(console, 'log');
  });
  afterEach(() => {
    consoleSpy.restore();
  })
  it('Testing Utils', function() {
    const calcStub = sinon.stub(Utils, 'calculateNumber').returns(10);
    sendPaymentRequestToApi(100, 20);
    expect(consoleSpy.calledOnce).to.be.true;
    expect(consoleSpy.calledWith('The total is: 10')).to.be.true;
    expect(calcStub.calledOnce).to.be.true;
    expect(calcStub.args[0][0]).to.equal('SUM');
    expect(calcStub.args[0][1]).to.equal(100);
    expect(calcStub.args[0][2]).to.equal(20);
    calcStub.restore();
  });
});
