import unittest
import os

def factorial(n):
    return 1 if n < 1 else n * factorial(n-1)

def existe(ruta):
    if os.stat(ruta):
	return os.stat(ruta)
    else: 
	return 0


class tester (unittest.TestCase):
    def test_1(self):
	self.assertEqual('foo'.upper(), 'FOO')	
	self.assertEqual(1, 1, "broken") 

    def test_2(self):	
	existe("test.py")

    def test_3(self):	
	existe("../script.py")

    def test_4(self):	
	existe("../docs")




if __name__ == "__main__":
    unittest.main()
