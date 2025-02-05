import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script

# Importez csv
import csv

 

# Vous utiliserez encore le fichier "Ex7 Lan Party.csv"
# 
#         Vous voulez créer un dossier par Lan Party
#         Et pour chaque Lan Party, créez des sous-dossier pour chaque jeu
#                   (On y mettra éventuellement la liste des participants du Lan qui veulent jouer à ce jeu)
#         ATTENTION: Pour le nom de chaque jeu: changez le ':' pour un '_' et gardez juste les 20 premiers caractères

#         Si besoin, des instructions détaillées sont données plus bas























# INSTRUCTIONS DÉTAILLÉES
#      Commencez par créer une liste des différents jeux vide
#      Ouvrez le fichier 'Ex4 Lan Party.csv' en lecture
#      utilisez csv.reader pour lire le fichier avec le bon delimiter
#      Sautez la première ligne de l'entête
#      Faites une boucle pour passer à travers chacune des lignes 
#      Créez un dossier pour le nom du Lan Party
#      Déplacez vous dans ce dossier
#      Utilisez le slicing pour garder uniquement les 3 jeux
#      Faites une boucle pour passer à travers chacun des jeux
#      Pour le nom de chaque jeu: changez le ':' pour un '_' et gardez juste les 20 premiers caractères
#      Créez un dossier pour le jeu avec le nouveau nom de jeu
#      Revenez au dossier parent
import os

jeuxvide= []
mot = []
with open("csvs/Ex7 Lan Party.csv","r", encoding="utf-8") as readfichierEx9:
    read = csv.reader(readfichierEx9,delimiter=';')
    os.makedirs("Lan Party",exist_ok= True)
    next(read)
    os.chdir("Lan Party")
    for ligne in read :
        ligneV2 = ligne[1:]
        for split in ligneV2 :
            split = split.replace(':','_')
            if  jeuxvide.count(split) == 0 :
                    jeuxvide.append(split)
                    
                    os.makedirs(split,exist_ok=True)
                    print(split)
        

                    

                
                        

                
        
            
# for lettre in split :
#                     if lettre == ':':
#                         lettre = '_'
#                         print(lettre)
#                     else :
#                         mot += lettre
#                         print(lettre)