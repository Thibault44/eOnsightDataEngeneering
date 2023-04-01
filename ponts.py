import pandas as pd
import requests
from bs4 import BeautifulSoup
import psycopg2


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

# Connexion à la base de données
conn = psycopg2.connect(
    host="ec2-34-251-233-253.eu-west-1.compute.amazonaws.com",
    database="de20cp98et6s4n",
    user="uvueqhtwwixald",
    password="6f5c9ce8db7795af0068d8f4e5c3879551bd73959a2e7100d439d22c964bc013"
)
# Insertion des données dans la base de données
cur = conn.cursor()
for index, row in df_filtered.iterrows():
    cur.execute("INSERT INTO ponts (nom, longueur, bridge_type, voie_portée_franchie, date, localisation, region) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (row['nom'], row['longueur'], row['bridge_type'], row['voie_portée_franchie'], row['date'],
                 row['localisation'], row['region'],))
conn.commit()

# Fermeture de la connexion
cur.close()
conn.close()
