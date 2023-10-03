import requests

urlProduits = "http://51.255.166.155:1353/logProduits/1664/"
urlVente = "http://51.255.166.155:1353/logAccordsVente/1664/"
responseProduits = requests.get(urlProduits)
responseVente = requests.get(urlVente)

if responseProduits.status_code == 200:
    dataProduits = responseProduits.json()  # Si la réponse est au format JSON
    print(dataProduits)  # Faites ce que vous voulez avec les données
    
else:
    print(f"Erreur lors de la requête. Statut : {responseProduits.status_code}")
   
if responseVente.status_code == 200:
    dataVente = responseVente.json()
    print(dataVente)

else: 
    print(f"Erreur lors de la requête. Statut : {responseVente.status_code}")