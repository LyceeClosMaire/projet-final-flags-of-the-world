def score (surnom,essais,points):
    now = time.ctime()
    date = time.strftime("%d, %H","%m","%s", time.strptime(now))

    donnees = [surnom,essais,points,date]

    fichier_csv = open("Scores.csv", mode='r', newline='')
    entree_csv = csv.reader(fichier_csv, dialect='excel')
    donnees = []

    for ligne in entree_csv:
     donnees.append(ligne)
    fichierCSV.close()

    fichier_csv = open("Scores.csv", mode="w", newline="")
    sortie_csv = csv.writer(fichier_csv, dialect="excel")

    for ligne in donnees :
     sortie_csv.writerow(ligne)
     sortie_csv.writerow(donnees)
    fichier_csv.close()
