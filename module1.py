import csv
import os


dossier_de_travail = "\\DC1-0210006T\SI - Echange\ISN\Projet Final\Projet final B.L.L. Flags of the world"
os.chdir(dossier_de_travail)

nom_csv = "Europe.csv"

fichier_csv = open(Europe.csv, mode='r', newline='')

entree_csv = csv.reader(fichier_csv, dialect='excel')

donnees = []

for ligne in entree_csv:
   print(ligne)
   donnees.append(ligne)

fichier_csv.close()