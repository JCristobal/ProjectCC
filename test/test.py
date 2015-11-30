# encoding: utf-8
import unittest

import os
import inspect

from script import *



# test para compobar que la ruta a un archivo (o archivo) existe
def existe(ruta):
    if os.stat(ruta):
	return os.stat(ruta)
    else: 
	return 0

# test para comprobar que existe una clase
def existe_clase(clase):
	try:
		return  type(clase)
	except:
		return 0

# test para comprobar que nos hemos conectado
def test_dbcon():
	return db==client.usuarios

# test para compobar el conjunto de meses
def test_meses():
	lista = [1,2,3,4,5,6,7,8,9,10,11,12]
	return lista==meses

# Inserción de un usuario en la base de datos
def insertarUsuario():
        post = {"user": "test",
	    	"nombre": "test_nombre",
	    	"apellidos": "test_appellido",
	    	"correo": "test@correo.es",
	    	"dia": "1",
	    	"mes": "2",
	    	"anio": "2001",
		"direccion": "Calle falsa 123",
	    	"password": "123456",
	    	"pago": "VISA",
	    	"visa": "5555-5555-5555-5555",
	    	}


	posts=db.posts
	post_id = posts.insert_one(post) 

	#Comprobamos si realmente se ha insertado en la base de datos
	query=posts.find({"user": "test"})

	return query.count() != 0

#Edición de un campo del usuario insertado
def editarUsuario():

   	posts=db.posts
        posts.update_one( { "user": "test" }, { '$set': { "nombre": "test_nombre_editado"}})

	#Comprobamos si realmente se ha actualizado bien la base de datos
	query=posts.find({"user": "test"})

	return query[0]["nombre"] == "test_nombre_editado"

#Borrado de un usuario de la base de datos
def borrarUsuario():
	
	posts=db.posts
	posts.delete_one({"user" : "test"})

	query=posts.find({"user": "test"})

	return query.count() == 0



# Clase en la que realizamos los test basicos
class test (unittest.TestCase):

    print "Test básicos"	

    def test_1(self):	
        self.assertTrue(existe("script.py"))

    def test_2_1(self):	
        self.assertTrue(existe("docs/pycco.css"))

    def test_2_2(self):	
        self.assertTrue(existe("docs/script.html"))

    def test_3(self):	
        self.assertTrue(existe_clase(registro))

    def test_4(self):	
        self.assertTrue(existe_clase(login))

    def test_5(self):	
        self.assertTrue(existe_clase(logout))

    def test_6(self):	
        self.assertTrue(existe_clase(ver_perfil))

    def test_7(self):	
        self.assertTrue(existe_clase(editar_perfil))

    def test_8(self):	
        self.assertTrue(existe_clase(mas_visitadas))

    def test_9(self):	
        self.assertTrue(existe_clase(rss))

    def test_10(self):	
        self.assertTrue(existe_clase(highchart))

    def test_11(self):	
        self.assertTrue(existe_clase(mapa))

    def test_12(self):	
        self.assertTrue(existe_clase(twitter))

    def test_13(self):	
        self.assertTrue(existe_clase(eventos_twitter))

    def test_14(self):	
        self.assertTrue(test_dbcon())

    def test_15(self):	
        self.assertTrue(test_meses())


	
# Clase en la que realizamos los test con la BD
class test_bd(unittest.TestCase):

    print "Test con la BD"	

    def test_insertar(self):
        self.assertTrue(insertarUsuario())
	
    def test_editar(self):
        insertarUsuario()
        self.assertTrue(editarUsuario())

    def test_borrar(self):
        insertarUsuario()
        self.assertTrue(borrarUsuario())


if __name__ == "__main__":
    unittest.main()
