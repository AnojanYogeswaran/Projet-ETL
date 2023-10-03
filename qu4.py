import csv
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <fichier_csv>")
    sys.exit(1)

fichier_csv = sys.argv[1]

# Étape 1 : Compter le nombre de produits par magasin dans la catégorie 5
magasin_produits = {}
magasin_produits_176 = {}
top_10_magasins = ['55','65','51','58','76','71','74','75','72','59']
somme = 0

with open(fichier_csv, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        produit = row[1]
        categorie = row[2]
        magasin = row[4]
        if categorie == '5' and magasin in top_10_magasins:
            if magasin in magasin_produits:
                magasin_produits[magasin] += 1
            else:
                magasin_produits[magasin] = 1
        if row[3] == '707' and magasin in top_10_magasins:
                if magasin in magasin_produits_176:
                    magasin_produits_176[magasin] += 1
                else:
                    magasin_produits_176[magasin] = 1
            


# Étape 2 : Compter le nombre total de produits dans la catégorie 5 vendus par les magasins du top 10

print(magasin_produits)
print(magasin_produits_176)
# Étape 3 : Calculer la part du nombre de produits offerts par le fabricant 1664
for cle, valeur in magasin_produits.items():
    print(f'Clé : {magasin_produits[cle]}, Valeur : {magasin_produits_176[cle]}')
    somme = somme + (magasin_produits_176[cle]/magasin_produits[cle])*100
print(somme)


print(f"La part du nombre de produits offerts par le fabricant 1664 dans l'ensemble des produits de la catégorie 5 vendus dans les magasins du top 10 est de : {somme/10}")