import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import psycopg2
import sqlalchemy


# URL de la page Wikipédia
url = "https://fr.wikipedia.org/wiki/Liste_de_ponts_d%27Italie"

# Récupération du contenu de la page
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Récupération du tableau des ponts
tables = soup.find_all("table", {"class": "wikitable"})

# Liste des noms des colonnes du DataFrame
column_names = ['nom', 'longueur', "bridge_type", "voie_portée_franchie", "date", "localisation", "region"]

# Liste des données à extraire pour chaque pont
data = []

# Parcours des lignes du tableau
for table in tables:
    for row in table.find_all("tr"):
        # Exclusion des lignes inter-tableaux
        if not row.find("th"):
            # Extraction des données de chaque colonne
            columns = row.find_all("td")
            nom = columns[2].text.strip()
            longueur = columns[4].text.strip()
            bridge_type = columns[5].text.strip()
            voie_portée_franchie = columns[6].text.strip()
            date = columns[7].text.strip()
            localisation = columns[8].text.strip()
            region = columns[9].text.strip()

            # Ajout des données dans la liste
            data.append([nom, longueur, bridge_type, voie_portée_franchie, date, localisation, region])

# Création du DataFrame
df = pd.DataFrame(data, columns=column_names)

# Filtre des villes pour n'avoir que les ponts de la ville de "Gênes"
df_filtered = df[df["localisation"].str.startswith("Gênes")]

# link to your database
engine = sqlalchemy.create_engine(
    'postgres://pjyflfrpaycgql:5babc4828af9a0749747e8f288ec088d99b8a8bd6647c904a12397b2131992ee@ec2-34-242-199-141.eu-west-1.compute.amazonaws.com:5432/daq7mhr06h7b1g',
    echo=False)
# attach the data frame (df) to the database with a name of the
# table; the name can be whatever you like
df_filtered.to_sql('base-donnee', conn=engine, if_exists='append')
# run a quick test
print(engine.execute("SELECT * FROM base-donnee").fetchone())

