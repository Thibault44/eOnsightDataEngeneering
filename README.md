# eOnsightDataEngeneering
Ce projet est un test technique en deux parties: DataEngineering et ImagesSatellite.

## Description

### DataEngineering
Le projet eOnsightDataEngineering vise à extraire les données de ponts (noms, coordonnées géographiques...) présentes sur une page wikipedia dédiée à la ville de Gênes en Italie et les stocker dans une base de données. Le tout peut être exécuté depuis un serveur distant de votre choix (GCP, AWS, Heroku, serveur perso, ...) pour exposer la base de données. 

Le repo contient un fichier Python 'ponts.py' qui traite des données d'ingénierie des ponts, un 'Procfile' pour définir la commande à exécuter par Heroku, un 'requirements.txt' pour déclarer les dépendances Python et un 'runtime.txt' pour spécifier la version de Python utilisée. Les données sont égalements présentes dans le dossier EO_Browser_images_uint16 (1).

### ImagesSatellite
Ce projet vise à présenter ne méthode pour générer une image couleur avec un bon niveau de contraste (similaire à l’image « True color ») représentant un carré d’environ 2km centré autour du viaduc Gênes-Saint-Georges (44°25′34′′N, 8°53′19′′E) en se basant sur les images « Raw » produites par les capteurs optiques de Sentinel-2.

Cette partie contient un fichier Python imageSatellite.py qui traite des images satellites et une image pont_crop.png.

## Installation
### DataEngineering
- Cloner le repo sur votre machine :
```
$ git clone https://github.com/[username]/eOnsightDataEngineering.git
```
- modification de ponts.py avec les logins PostgreSQL
- Installer les dépendances requises :
```
$ pip install -r requirements.txt
```
- Exécuter le script Python :
```
$ python ponts.py
```

## Déploiement sur Heroku
### DataEngineering
- Connexion à heroku
- La base de données sera accessible sur Heroku en utilisant la commande suivante :
```
$ heroku pg:psql -a eonsight2
```

## Utilisation
Les librairies nécessaires sont pandas, requests, bs4, psycopg2, os, osgeo (GDAL), numpy et PIL.
