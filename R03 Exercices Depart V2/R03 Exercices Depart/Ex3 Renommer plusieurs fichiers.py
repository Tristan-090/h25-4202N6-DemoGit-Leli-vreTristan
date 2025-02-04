# importez os
# # allez dans le dossier Ex3 Videos
# # avec la boucle for, passez à travers chacun des dossiers de os.listdir()
# #     utilisez os.path.splitext pour obtenir le filename et l'extension
# #     utilisez split sur le filename pour obtenir le titre, le cours et le numéro du cours
# #     utilisez strip pour enlever les espaces qui pourraient rester pour le titre et le numéro
# #     en plus utilisez zfill pour remplir le numéro de sorte que 1 deviendra 01
# #     recréez le nouveau nom de fichier#   utliser os.rename pour renommer le fichier
import os

#os.chdir("c:/Users/2181650\Downloads/R03 Exercices Depart/Ex3 Videos")
os.chdir("C:/Users/trist/Desktop/R03 Exercices Depart/Ex3 Videos")
chemin = "C:/Users/trist/Desktop/R03 Exercices Depart/Ex3 Videos"
dossier = os.listdir()
nom = []
cours = []
for boucle in  dossier :
    os.path.splitext
    #split = boucle.split("_")
    nom, cours = os.path.splitext(boucle)
    
    
    print(f"Nom du fichier: {nom}   Nom de l'extension: {cours}")
    #print(os.path.splitext())