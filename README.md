# eOnsightDataEngeneering
## Description
Le projet eOnsightDataEngineering vise à extraire les données de ponts (noms, coordonnées géographiques...) présentes sur une page wikipedia dédiée à la ville de Gênes en Italie et les stocker dans une base de données. Le tout peut être exécuté depuis un serveur distant de votre choix (GCP, AWS, Heroku, serveur perso, ...) pour exposer la base de données. Le repo contient un fichier Python 'ponts.py' qui traite des données d'ingénierie des ponts, un 'Procfile' pour définir la commande à exécuter par Heroku, un 'requirements.txt' pour déclarer les dépendances Python et un 'runtime.txt' pour spécifier la version de Python utilisée. Les données sont égalements présentes dans le dossier EO_Browser_images_uint16 (1).

## Installation
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
- Connexion à heroku
- La base de données sera accessible sur Heroku en utilisant la commande suivante :
```
$ heroku pg:psql -a eonsight2
```

## Utilisation
Les librairies nécessaires sont pandas, requests, bs4 et psycopg2.
