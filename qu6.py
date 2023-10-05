
import csv
from datetime import datetime

# Vérification des arguments
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <fichier_csv>")
    sys.exit(1)

fichier_csv = sys.argv[1]

# Initialisation du compteur
count = 0
panier = []
# Lecture du fichier CSV
with open(fichier_csv, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        date_string = row[0]
        datehour = datetime.strptime(date_string, '%Y%m%d')
        mois = datehour.month
        
        if len(row) > 2 and row[2] == '5' and datetime(2022, 1, 10) <= datehour <= datetime(2022, 2, 6):
            if row[3] not in panier:
                panier.append(row[3])
            

print(f"Nombre de lignes avec la troisième colonne égale à 3 : {len(panier)}")
