# eOnsightDataEngeneering
## Description
Le projet eOnsightDataEngineering vise à extraire les données de ponts (noms, coordonnées géographiques...) présentes sur une page wikipedia dédiée à la ville de Gênes en Italie et les stocker dans une base de données. Le tout peut être exécuté depuis un serveur distant de votre choix (GCP, AWS, Heroku, serveur perso, ...) pour exposer la base de données. Le repo contient un fichier Python 'ponts.py' qui traite des données d'ingénierie des ponts, un 'Procfile' pour définir la commande à exécuter par Heroku, un 'requirements.txt' pour déclarer les dépendances Python et un 'runtime.txt' pour spécifier la version de Python utilisée.

## Installation
Cloner le repo sur votre machine :
shell
Copy code
$ git clone https://github.com/[username]/eOnsightDataEngineering.git
Installer les dépendances requises :
ruby
Copy code
$ pip install -r requirements.txt
Exécuter le script Python :
ruby
Copy code
$ python ponts.py
