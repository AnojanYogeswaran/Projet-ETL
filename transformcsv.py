import csv

# Définir le nom du fichier d'entrée et de sortie
fichier_entree = 'pointsDeVente-tous.csv'
fichier_sortie = 'fichier_csv.csv'

# Ouvrir le fichier d'entrée en mode lecture
with open(fichier_entree, 'r', newline='') as fichier_in:
    # Lire les lignes du fichier
    lignes = fichier_in.readlines()

    # Ouvrir le fichier de sortie en mode écriture, avec un dialecte spécifique pour un espace comme délimiteur
    with open(fichier_sortie, 'w', newline='') as fichier_out:
        csv_writer = csv.writer(fichier_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # Parcourir les lignes et écrire chaque ligne dans le fichier CSV
        for ligne in lignes:
            # Supprimer les espaces supplémentaires en début et fin de ligne et diviser la ligne en une liste
            champs = ligne.strip().split()

            # Écrire la liste de champs dans le fichier CSV
            csv_writer.writerow(champs)




