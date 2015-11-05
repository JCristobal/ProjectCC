# ProjectCC - Submódulo perteneciente a [PeriodicoInteractivo](https://github.com/ProyectCC/PeriodicoInteractivo)

[![Join the chat at https://gitter.im/JCristobal/ProjectCC](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/JCristobal/ProjectCC?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

### Submódulo para mejora o cambio de framework de desarrollo y reestructuración de la aplicación.



[![Build Status](https://travis-ci.org/JCristobal/ProjectCC.svg?branch=master)](https://travis-ci.org/JCristobal/ProjectCC)

Responsable del módulo: [José Cristóbal López Zafra](https://github.com/JCristobal).

*Licencia: GPLv2*


##Motivación

Partimos de una aplicación base de un "periódico" que se puede decir que sólo es el esqueleto de lo que será nuestra aplicación. De ésta base contruiremos un *periódico interactivo* en el que los usuarios podrán participar y valorar en distintas noticias.

En este submódulo se construirá la aplicación para conseguir una mejor estructura y ampliar sus funcionalidades. Para ello se trabajará en este repositorio con unas noticias (y sus respectivas valoraciones), análisis y usuarios estándar, que los otros submódulos se encargarán de gestionar.


##Procedimiento de realización

Realizaremos la aplicación de la forma más modular posible, centrándonos en cada módulo en un aspecto: mejora de la estructura, apariencia, gestión de la base de datos y usuarios, y realizando análisis y valoraciones. 

Ya que éste módulo se encargará de la estructura y del framework que se use, se usará uno de los siguientes, el que se adapte mejor a los requisitos del proyecto, mejorando el actual "periódico".

###Frameworks

Con la ayuda de los Frameworks podremos desarrollar un sitio web fácilmente: nos ayudaremos de bibliotecas propias de éstos para acceso a base de datos, plantillas y numerosas facilidades que proporcionan. En éste submódulo estudiaremos y trabajaremos con el que más se adapte a nuestro proyecto, dentro del lenguaje principal de la aplicación, python. Algunos de ellos serán:

#### web.py

Una de las ventajas de [web.py](http://webpy.org/) es sus sencillez, y la gran cantidad de recursos que tiene:

* URL dispacher
* Templates
* Acceso a Bases de Datos
* Autentificación de usuarios y sesiones
* Formularios
* Servidor web propio para desarrollo


#### TurboGears

[Turbogears](http://www.turbogears.org/) es un potente framework con multitud de ventajas:

* Puede empezar como micro-framework hasta alcanzar todas sus funcionalidades
* Código natural y flexible
* Conexión con varias BD y acceso a datos WSGI
* Templates


#### Django

[Django](https://www.djangoproject.com/) es un framework web de Python de alto nivel que fomenta el rápido desarrollo y buen diseño. 
Muy potente y usado, se caracteriza por su:

* Rapidez
* Seguridad
* Escalabilidad



##Relación con la asignatura [CC](https://github.com/JJ/clases-CC-2015-16/)

Con el proyecto realizaremos un desarrollo DevOps, con múltiples herramientas evolucionando a lo largo del curso y practicando los distintos contenidos de éste. Realizaremos test para hacer pruebas unitarias, integración continua, provisionamiento y despligue automático. Dichas actividades se harán coincidiendo con la evolución de la asignatura.



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
