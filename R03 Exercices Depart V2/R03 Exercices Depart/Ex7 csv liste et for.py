import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script

# Importez csv



 

# Regardez le contenu du fichier "Ex7 Lan Party.csv"
#          Observez que dans ce fichier, la première ligne comprends les en-têtes de colonne 
#                 Lan Party;Top 1;Top 2; Top 3
#          Top 1, Top 2 et Top 3 sont les jeux les plus populaires dans chaque Lan Party
#          
#          Vous aimez jouer à Valorant
#          Imprimez la liste des Lan Party dans lesquels votre jeu préféré est parmi leurs Tops
# 
#          Aucune instruction détaillée n'est donnée plus bas
import csv

with open("csvs/Ex7 Lan Party.csv","r", encoding="utf-8" ) as lirefichierparty :
    read = csv.reader(lirefichierparty,delimiter=';')
    for list in read :
        if  list[1] == 'Valorant' or list[2] == 'Valorant' or list[3] == 'Valorant'  :
            print(list)