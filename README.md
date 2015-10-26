# ProjectCC - Submódulo perteneciente a [PeriodicoInteractivo](https://github.com/ProyectCC/PeriodicoInteractivo)

### Submódulo para mejora o cambio de framework de desarrollo y reestructuración de la aplicación.



[![Build Status](https://travis-ci.org/JCristobal/ProjectCC.svg?branch=master)](https://travis-ci.org/JCristobal/ProjectCC)

Responsable del módulo: [José Cristóbal López Zafra](https://github.com/JCristobal).

*Licencia: GPLv2*



##Frameworks

Con la ayuda de los Frameworks podremos desarrollar un sitio web fácilmente: nos ayudaremos de bibliotecas propias de éstos para acceso a base de datos, plantillas y numerosas facilidades que proporcionan. En éste submódulo estudiaremos y trabajaremos con el que más se adapte a nuestro proyecto, dentro del lenguaje principal de la aplicación, python. Algunos de ellos serán:

### web.py

Una de las ventajas de [web.py](http://webpy.org/) es sus sencillez, y la gran cantidad de recursos que tiene:

* URL dispacher
* Templates
* Acceso a Bases de Datos
* Autentificación de usuarios y sesiones
* Formularios
* Servidor web propio para desarrollo


### TurboGears

[Turbogears](http://www.turbogears.org/) es un potente framework con multitud de ventajas:

* Puede empezar como micro-framework hasta alcanzar todas sus funcionalidades
* Código natural y flexible
* Conexión con varias BD y acceso a datos WSGI
* Templates


### Django

[Django](https://www.djangoproject.com/) es un framework web de Python de alto nivel que fomenta el rápido desarrollo y buen diseño. 
Muy potente y usado, se caracteriza por su:

* Rapidez
* Seguridad
* Escalabilidad



***

##Documentación pycco

Para la documentación se usará [pycco](http://fitzgen.github.io/pycco/), "versión python de Docco".

Una vez instalado con `sudo pip install pycco` ejecuto `pycco script.py` o `pycco *.py` si hay varios archivos python.

Los documentos generados (html con sus respectivos css) los puedo ver en el directorio [docs/](https://github.com/JCristobal/ProjectCC/tree/master/docs) 



##Integración continua
![travis-ci](http://i.imgur.com/TRaIpqb.jpg)

Para la integración continua usaremos [Travis-CI](https://travis-ci.org/).

Travis provee integración continua hosteada y tiene una integración con GitHub muy sencilla.
Además soporta despliegue para Openshift, Heroku, etc...

Puedes ver el estado actual del proyecto en el *badge* superior o mediante [este enlace](https://travis-ci.org/JCristobal/ProjectCC).


##Test
![mocha-chai](http://i.imgur.com/fRv28Y6.png)

Los tests los podemos encontrar en [test/test.js](https://github.com/JCristobal/ProjectCC/blob/master/test/test.js). Para los tests se han usado las bibliotecas Mocha y Chai.

[Mocha](http://mochajs.org/) es un framework para NodeJS para hacer tests unitarios y [Chai](http://chaijs.com/) es una biblioteca de aserciones (assertion library) para NodeJS y para el navegador.


Para instalar Mocha, Chai y sus plugins:

`sudo npm install mocha --save-dev`
`sudo npm install chai`
`sudo npm install chai-fs`
