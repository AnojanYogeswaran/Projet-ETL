import csv
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <fichier_csv>")
    sys.exit(1)

fichier_csv = sys.argv[1]

# Étape 1 : Compter le nombre de produits par magasin dans la catégorie 5
magasin_produits = {}
top_10_magasins = [60,64,61,65,69,68,66,63,62,67]

with open(fichier_csv, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if len(row) > 4:  # Assurez-vous qu'il y a au moins 5 colonnes
            fabricant = row[1]
            categorie = row[2]
            magasin = row[4]

            if categorie == '5' and magasin in top_10_magasins:
                if magasin in magasin_produits:
                    magasin_produits[magasin] += 1
                else:
                    magasin_produits[magasin] = 1

# Étape 2 : Compter le nombre total de produits dans la catégorie 5 vendus par les magasins du top 10
nombre_total_produits_cat5 = sum(magasin_produits.values())

# Étape 3 : Calculer la part du nombre de produits offerts par le fabricant 1664
fabricant_1664_produits = sum(magasin_produits[magasin] for magasin in magasin_produits if 1664 in magasin)
part_fabricant_1664 = fabricant_1664_produits / nombre_total_produits_cat5

print(f"La part du nombre de produits offerts par le fabricant 1664 dans l'ensemble des produits de la catégorie 5 vendus dans les magasins du top 10 est de : {part_fabricant_1664:.2%}")