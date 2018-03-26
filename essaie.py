import random
import csv
import os

pays = ["Afghanistan", "Afrique du sud", "Albanie", "Algérie", "Allemagne", "Ancienne République yougoslave de Macédoine", "Andorre", "Angola", "Antigua-et-Barbuda", "Arabie Saoudite", "Argentine", "Arménie", "Australie", "Autriche", "Azerbaïdjan", "Bahamas", "Bahreïn", "Bangladesh", "Barbade", "Bélarus", "Belgique", "Belize", "Bénin", "Bhoutan", "Bolivie", "Bosnie-et-Herzégovine", "Botswana", "Brésil", "Brunei", "Bulgarie", "Burkina Faso", "Burundi", "Cambodge", "Cameroun", "Canada", "Cap-Vert", "Chili", "Chine", "Chypre", "Colombie", "Comores", "République Démocratique du Congo", "République du Congo", "République de Corée", "République Populaire Démocratique de Corée", "Costa Rica", "Côte d'Ivoire", "Croatie", "Cuba", "Danemark", "Djibouti", "Dominique", "Égypte", "El Salvador", "Émirats Arabes unis", "Équateur", "Érythrée", "Espagne", "Estonie", "État da la Cité du Vatican", "États-Unis d'Amérique", "Éthiopie", "Fidji", "Finlande", "France", "Gabon", "Gambie", "Géorgie", "Ghana", "Grèce", "Grenade", "Guatemala", "Guinée", "Guinée-Bissau", "Guinée Équatoriale", "Guyana", "Haïti", "Honduras", "Hongrie", "Îles Marshall", "Îles Salomon", "Inde", "Indonésie", "Iraq", "Iran", "Irlande", "Islande", "Israël", "Italie", "Jamaïque", "Japon", "Jordanie", "Kazakhstan", "Kenya", "Kirghizistan", "Kiribati", "Kosovo", "Koweït", "Laos", "Lesotho", "Lettonie", "Liban", "Liberia", "Libye", "Liechtenstein", "Lituanie", "Luxembourg", "Madagascar", "Malaisie", "Malawi", "Maldives", "Mali", "Malte", "Maroc", "Maurice", "Mauritanie", "Mexique", "Micronésie", "Moldavie", "Monaco", "Mongolie", "République du Monténégro", "Mozambique", "Myanmar", "Namibie", "Nauru", "Népal", "Nicaragua", "Niger", "Nigéria", "Norvège", "Nouvelle-Zélande", "Oman", "Ouganda", "Ouzbékistan", "Pakistan", "Palau", "Panama", "Papouasie-Nouvelle-Guinée", "Paraguay", "Pays-Bas", "Pérou", "Philippines", "Pologne", "Portugal", "Qatar", "République Centrafricaine", "République Dominicaine", "Roumanie", "Royaume-Uni", "Russie", "Rwanda", "Saint-Christophe-et-Nevis", "Sainte-Lucie", "Saint-Marin", "Saint-Vincent-et-Les-Grenadines", "Samoa de l'Ouest", "São-Tomé-et-Príncipe", "Sénégal", "République de Serbie", "Seychelles", "Sierra Leone", "Singapour", "Slovaquie", "Slovénie", "Somalie", "Soudan", "République du Soudan du sud", "Sri Lanka", "Suède", "Suisse", "Suriname", "Swaziland", "Syrie", "Tadjikistan", "Tanzanie", "Tchad", "République Tchèque", "Thaïland", "République Democratique du Timor Oriental", "Togo", "Tonga", "Trinidad-et-Tobago", "Tunisie", "Turkménistan", "Turquie", "Tuvalu", "Ukraine", "Uruguay", "Vanuatu", "Venezuela", "Viet Nam", "Yémen", "Zambie", "Zimbabwe"]
jeu = True
europe = ["Albanie", "Allemagne", "Ancienne République yougoslave de Macédoine", "Andorre", "Autriche", "Bélarus", "Belgique", "Bosnie-et-Herzégovine", "Bulgarie", "Croatie", "Chypre", "Danemark", "Espagne", "Estonie", "État da la Cité du Vatican", "Finlande", "France", "Grèce", "Hongrie", "Irlande", "Islande", "Italie", "Kosovo", "Lettonie", "Liechtenstein", "Lituanie", "Luxembourg", "Malte", "Moldavie", "Monaco", "République du Monténégro", "Norvège", "Pays-Bas", "Pologne", "Portugal", "Roumanie", "Royaume-Uni", "Russie", "Saint-Marin", "Slovaquie", "Slovénie", "République de Serbie", "Suède", "Suisse", "République Tchèque", "Turquie", "Ukraine" ,"Cuba", "Panama", ]
asie = ["Afghanistan", "Arabie Saoudite", "Arménie", "Azerbaïdjan", "Bahreïn", "Bangladesh", "Bhoutan", "Brunei", "Cambodge", "Chine", "République de Corée", "République Populaire Démocratique de Corée", "Émirats Arabes unis", "Géorgie", "Inde", "Indonésie", "Iraq", "Iran", "Israël", "Japon", "Jordanie", "Kazakhstan", "Kirghizistan", "Koweït", "Laos", "Liban", "Malaisie", "Maldives", "Mongolie", "Myanmar", "Népal", "Oman", "Ouzbékistan", "Pakistan", "Philippines", "Qatar", "Russie", "Singapour", "Sri Lanka", "Syrie", "Tadjikistan", "Thaïland", "République Democratique du Timor Oriental", "Turkménistan", "Turquie", "Viet Nam", "Yémen", ]
afrique = ["Afrique du sud", "Algérie", "Angola", "Bénin", "Botswana", "Burkina Faso", "Burundi", "Cameroun", "Cap-Vert", "Comores", "République Démocratique du Congo", "République du Congo", "Djibouti", "Égypte", "Érythrée", "Éthiopie", "Gabon", "Gambie", "Ghana", "Guinée", "Guinée-Bissau", "Guinée Équatoriale", "Kenya", "Lesotho", "Liberia", "Libye", "Madagascar", "Malawi", "Mali", "Maroc", "Maurice", "Mauritanie", "Mozambique", "Namibie", "Niger", "Nigéria", "Ouganda", "République Centrafricaine", "Rwanda", "São-Tomé-et-Príncipe", "Sénégal", "Seychelles", "Sierra Leone", "Somalie", "Soudan", "République du Soudan du sud", "Swaziland", "Tanzanie", "Tchad", "Togo", "Tunisie", "Zambie", "Zimbabwe"]
océanie = ["Australie", "Fidji", "Îles Salomon", "Îles Marshall", "Kiribati", "Micronésie", "Nauru", "Nouvelle-Zélande", ]
amerique_du_sud = []
amerique_du_nord =[]
drapeau_facile = ["États-Unis d'Amérique", "Israël", "Canada", "Japon", "République de Corée", "Chine", "Australie", "Brésil", "Afrique du sud", "Mexique", "Argentine", "Liban", "Tunisie", "Inde", "Égypte", "Venezuela", "Algérie", "Iran", "Népal", "Rwanda", "Myanmar", "Colombie", "Bangladesh", "Tanzanie", "Afghanistan", "Kenya", "Pérou", "République Démocratique du Congo", "Arabie Saoudite", "Pakistan", "Libye", "Cambodge", "Panama", "Chili", "Mongolie", "Philippines", "Bahreïn", "Koweït"]


print("Par quel niveau de difficulté voulez-vous commencer ? \n   facile \n   moyen \n   difficile \n")
difficulter = input("Quelle difficulté voulez-vous ?")

print("combien de pays voulez-vous ? \n")
nb_pays = int(input("nombre de pays souhaiter ="))


dossier_de_travail = "\\DC1-0210006T\SI - Echange\ISN\Projet Final\Projet final B.L.L. Flags of the world"
os.chdir(dossier_de_travail)

nom_csv = "pays-du-monde.csv"

fichier_csv = open("pays-du-monde.csv", mode='r', newline='')

entree_csv = csv.reader(fichier_csv, dialect='excel')

donnees = []

for ligne in entree_csv:
   print(ligne)
   donnees.append(ligne)

fichier_csv.close()


print("Par quel niveau de difficulté voulez-vous commencer ? \n   facile \n   moyen \n   difficile \n")
difficulter = input("Quelle difficulté voulez-vous ?")

print("combien de pays voulez-vous ? \n")
nb_pays = int(input("nombre de pays souhaiter ="))

print("Dans quel continent vivez-vous ? \n   -europe \n   -asie \n   -afrique \n   -océanie \n   -amérique du sud \n   -amérique du nord \n")
continent_originaire = input("je vie en ")

while nb_pays >0:

    if difficulter == "facile":
        essaie = 0
        selection_pays = random.sample(drapeau_facile,1)
        print(selection_pays)
        print("\n")

    elif difficulter == "moyen":
        if continent_originaire == "europe":
            difficulter_moyen = europe + drapeau_facile

        elif continent_originaire == "asie":
            difficulter_moyen = asie + drapeau_facile

        elif continent_originaire == "afrique":
            difficulter_moyen = afrique + drapeau_facile

        elif continent_originaire == "océanie":
            difficulter_moyen = océanie + drapeau_facile

        elif continent_originaire == "amérique du sud":
            difficulter_moyen = amerique_du_sud + drapeau_facile

        elif continent_originaire == "amérique du nord":
            difficulter_moyen = amerique_du_nord + drapeau_facile
        essaie = 0
        selection_pays = random.sample(difficulter_moyen,1)
        print(selection_pays)
        print("\n")
        nb_pays -= 1
        print("il reste ", nb_pays)
        print("\n")


    elif difficulter == "difficile":
        essaie = 0
        selection_pays = random.sample(pays,1)
        print(selection_pays)
        print("\n")

