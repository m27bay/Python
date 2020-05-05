# Chemin pour complier
#!/usr/bin/python3.8

########## IMPORTATION ##########

# Importation module pour affichage.
from __future__ import print_function

from Tkinter import *
# import time

########## Fin importation ##########


########## Declaration variable(s) globale(s) ##########

# Taille de la fenetre et du caneva.
Sizex, Sizey = 800, 800
Size = 600

# Compteur de coup(s).
NbrCoup = 0
# NbrCoupMax = 4 -> Record en 5*5

# Origine du caneva.
Origine=(Sizey-Size)/2

# Demande utilisateur.
NbrCarree=int(input("Entrez la taille du damier souhaite: "))
while((NbrCarree < 5) | (NbrCarree > 25)):
  print("\nTaille du damier trop importante ou trop faible.")
  NbrCarree=int(input("Entrez la taille du damier souhait: "))

# On creer une matrice pour enregistre la couleur de chaque cases du damier: 1=noir, 0=blanc.
MatriceCouleur = [[0] * NbrCarree for _ in range(NbrCarree)]

# On creer une matrice pour enresgistre les coordonnees du point en
# haut a gauche pour chaque case.
MatriceCoords = [[0] * NbrCarree for _ in range(NbrCarree)]

# Taille d'un carree
Cote=Size/NbrCarree

########## Fin declaration variable(s) globale(s) ##########


########## L'ensemble des definition(s) ##########

def Carree(coordx, coordy, coul):
  # Cette fonction permet de dessiner un carree.
  Can.create_rectangle(coordx, coordy, coordx+Cote, coordy+Cote, fill=coul)



def Damier():
  # Cette fonction permet de dessiner le damier.
  coordx, coordy = Origine, Origine
  valCoul=0 # Sert a faire le changement de couleur.

  for i in range(NbrCarree):
    for j in range(NbrCarree):

      # On cherche de quelle couleur est la case.
      if valCoul%2==0:
        coul='black'
        MatriceCouleur[i][j]=1
      else:
        coul='white'
        MatriceCouleur[i][j]=0

      # Enfin on dessine le carree.
      MatriceCoords[i][j]=(coordx, coordy)
      Carree(coordx, coordy, coul)

      coordx+=Cote # On passe a celui d'a cote.
      valCoul+=1   # On change de couleur.

    # On augmente la variable couleur pour eviter l'alignement lorsque NbrCarre
    # est pair.
    if(NbrCarree%2==0): valCoul+=1

    coordx=Origine # On remet x a l'origine, on a finit de dessiner la ligne.
    coordy+=Cote   # On passe a la colonne suivante.


def AffMatrice(matrice):
  for i in range(NbrCarree):
    for j in range(NbrCarree):
      # Normalement end='\n', la je veux juste un espace entre chaque affiche.
      print(matrice[i][j], end='')

    # Apres l'affichage d'une ligne je saute une ligne.
    print("")

########## Fin definition(s) ##########

########## Main ##########

# Gestion/ creation de la fentre et du caneva.
Win = Tk()
Win.title("Damier")
Can = Canvas(Win, width = Sizex, height = Sizey, bg='white')
Can.pack()

# Dessin du damier.
Damier()
AffMatrice(MatriceCoords)

Win.mainloop()

########## Fin main ##########
