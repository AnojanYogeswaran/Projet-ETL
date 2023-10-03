import csv
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <fichier_csv>")
    sys.exit(1)

fichier_csv = sys.argv[1]

count = 0
panierFabricant = []
liste = []
panierProduit = []

with open(fichier_csv, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if len(row) > 2 and row[2] == '5':
            if row[3] not in panierFabricant:
                panierFabricant.append(row[3])
    csvfile.seek(0)
    reader = csv.reader(csvfile)        
    for row in reader:
        if len(row) > 2 and row[2] == '5':
            if row[3] in panierFabricant:
                panierProduit.append((row[3], row[1]))
                count = count + 1

# Créer un dictionnaire pour stocker les produits par fabricant
fabricant_produits = {}

# Compter les produits par fabricant
for fabricant, produit in panierProduit:
    if fabricant in fabricant_produits:
        fabricant_produits[fabricant].add(produit)
    else:
        fabricant_produits[fabricant] = {produit}

# Afficher le nombre de produits par fabricant
for fabricant, produits in fabricant_produits.items():
    print(f"Fabricant {fabricant} : {len(produits)} produits")

# Calculer la moyenne
moyenne_produits_par_fabricant = sum(len(produits) for produits in fabricant_produits.values()) / len(fabricant_produits)

print(len(fabricant_produits))
print(sum(len(produits) for produits in fabricant_produits.values()))

print(f"Moyenne de produits par fabricant : {moyenne_produits_par_fabricant}")