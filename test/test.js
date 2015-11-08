var assert = require('assert');

var chai = require('chai');//Biblioteca para Mocha
var expect = chai.expect;
chai.use(require('chai-fs'));

var request = require('supertest');//Biblioteca para comprobar servidores web
var urlServidor = "http://localhost:8080";//URL del servidor donde se ejecuta la aplicación
var urlServidorRegistro = "http://localhost:8080/registro";//URL (web de registro) del servidor donde se ejecuta la aplicación


describe('Test básicos', function() {




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


  describe('Pruebas de servidor', function () {
/*
    //Solo en local
    it('Comprobando que el servidor está activo', function (done) {
      request(urlServidor).get('/').expect(200).end(function(err, res){
      if (err)
        return done(err)
        done();
      });
    });

    it('Comprobando que la sección de logueo es accesible', function (done) {
      request(urlServidorRegistro).get('/').expect(200).end(function(err, res){
      if (err)
        return done(err)
        done();
      });
    });
*/

  })



});

