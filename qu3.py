import csv
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <fichier_csv>")
    sys.exit(1)

fichier_csv = sys.argv[1]
i=0
id_occurrences = {}

with open(fichier_csv, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if len(row) > 4 and row[2]=='5':  
            id_5eme_colonne = row[4]
            if id_5eme_colonne in id_occurrences:
                id_occurrences[id_5eme_colonne] += 1
            else:
                id_occurrences[id_5eme_colonne] = 1

top_10_occurrences = sorted(id_occurrences.items(), key=lambda x: x[1], reverse=True)[:10]


for id, occurrences in top_10_occurrences:
    i += 1
    print(f"TOP {i}: magID: {id}, Occurrences: {occurrences}")