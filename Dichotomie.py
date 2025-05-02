
liste = [1, 3, 5, 7, 9, 11]
longueur_liste = len(liste)
print("Il y a ",longueur_liste,'elements dans la liste')

def recherche_dichotomique (liste, element):
    if len(liste) == 1:
        if liste[0] == element:
            return 0
        else: 
            return -1
    else:
        milieu_liste = len(liste)//2

        if liste[milieu_liste] > element:
            resultat = recherche_dichotomique(liste[0:milieu_liste],element)
            return resultat if resultat != -1 else -1
        else :
            resultat = recherche_dichotomique(liste[milieu_liste:],element)
            return resultat + milieu_liste if resultat != -1 else -1

print(recherche_dichotomique(liste,18))