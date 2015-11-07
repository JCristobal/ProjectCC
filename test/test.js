var assert = require('assert');

var chai = require('chai');//Biblioteca para Mocha
var expect = chai.expect;
chai.use(require('chai-fs'));

/*
objCalculator = {
  addNumber: function(a, b){
    return a + b;
  },

  substractNumber: function(a, b){
    return a - b;
  },

  multiplyNumber: function(a, b){
    return a * b;
  },

  divideNumber: function(a, b){
    return a / b;
  }
}
*/

describe('Test básicos', function() {

/*
  describe('Elementos con indexOf()', function () {
    it('basic test: should return -1 when the value is not present', function (done) {
      assert.equal(-1, [1,2,3].indexOf(5));
      assert.equal(-1, [1,2,3].indexOf(0));
      done();
    });
  });
*/

/*
  describe('Operaciones básicas con funciones locales', function () {
    it('Sumamos 2 y 3', function (done) {
      assert.equal(5, objCalculator.addNumber(2, 3));
      done();
    });
    it('Multiplicamos 2 y 2', function (done) {
      assert.equal(4, objCalculator.multiplyNumber(2, 2));
      done();
    });
    it('Dividimos 3 y 1', function (done) {
      assert.equal(3, objCalculator.divideNumber(3, 1));
      done();
    });
  });
*/


  describe('Comprobamos archivos', function () {

    it('El fichero principal existe', function (done) {
      expect('script.py').to.be.a.file();
      done();
    });

    it('Archivos de documentación "pycco" existen', function (done) {
      expect('docs/script.html').to.be.a.file();
      expect('docs/pycco.css').to.be.a.file();
      done();
    });

  });






});

