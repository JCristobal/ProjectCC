#!/bin/bash

# Tendremos que tener Git instalado y con las variables correctamente instaladas
# apt-get install git
git clone https://github.com/JCristobal/ProjectCC

cd ProjectCC

# El toolbelt de Heroku debe estar instalado y configurado
# wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
# heroku login
heroku apps:create --region eu --buildpack heroku/python periodicointeractivo-x

#echo "web: python script.py $PORT" > Procfile # No hace falta, se incluye en el repo

# Declaramos variables internas de Heroku
heroku config:set PORT=8080

# Desplegamos mongoDB
# (no disponemos de targeta de crédito, por lo que no podemos desplegarlo)
# heroku addons:create mongohq:ssd_1g_elastic 

# Desplegamos la aplicación a Heroku
git push heroku master

# Abrimos el navegador con la aplicación
heroku open
