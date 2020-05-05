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

# Origine du caneva.
Origine=(Sizey-Size)/2

# Taille du damier.
NbrCarree=8

# On creer une matrice pour enresgistre les coordonnees du point en
# haut a gauche pour chaque case.
MatriceCoords = [[0] * NbrCarree for _ in range(NbrCarree)]

#
TabDeJeu = [[0] * NbrCarree for _ in range(NbrCarree)]

# Taille d'un carree et d'un cercle
Cote=Size/NbrCarree
Diametre=Cote-4

########## Fin declaration variable(s) globale(s) ##########


########## L'ensemble des definition(s) ##########

def Carree(coordx, coordy, coul):
  # Cette fonction permet de dessiner un carree.
  Can.create_rectangle(coordx, coordy, coordx+Cote, coordy+Cote, fill=coul)



def DessinPion():
  global TabDeJeu
  coordx, coordy = Origine, Origine+Cote
  for i in range(NbrCarree):
      Dess=Can.create_oval(MatriceCoords[1][i][0]+2, coordy+2, MatriceCoords[1][i][0]+2+Diametre, coordy+Diametre, fill='red')
      TabDeJeu[1][i]=(Dess, MatriceCoords[1][i][0]+2, coordy+2)

  coordx, coordy = Origine, Origine+(Size-2*Cote)
  for i in range(NbrCarree):
      Dess=Can.create_oval(MatriceCoords[1][i][0]+2, coordy+2, MatriceCoords[1][i][0]+2+Diametre, coordy+Diametre, fill='#E31919')
      TabDeJeu[NbrCarree-2][i]=(Dess, MatriceCoords[1][i][0]+2, coordy+2)



def DessinTour():
  global TabDeJeu
  coordx, coordy = Origine, Origine

  Dess=Can.create_oval(coordx+2, coordy+2, coordx+2+Diametre, coordy+2+Diametre, fill='#FF7400')
  TabDeJeu[0][0]=(Dess, coordx+2, coordy+2)

  Dess=Can.create_oval(coordx+Size-Cote+2, coordy+2, coordx+Size-2, coordy+Cote-2, fill='#FF7400')
  TabDeJeu[0][NbrCarree-1]=(Dess, coordx+Size-Cote+2, coordy+2)

  Dess=Can.create_oval(coordx+2, coordy+Size-Cote+2, coordx+Cote-2, coordy+Size-2, fill='#D96F17')
  TabDeJeu[NbrCarree-1][0]=(Dess, coordx+2, coordy+Size-Cote+2)

  Dess=Can.create_oval(coordx+Size-Cote+2, coordy+Size-Cote+2, coordx+Size-2, coordy+Size-2, fill='#D96F17')
  TabDeJeu[NbrCarree-1][NbrCarree-1]=(Dess, coordx+Size-Cote+2, coordy+Size-Cote+2)



def DessinCavalier():
  global TabDeJeu




def DessinAllPion():
  DessinPion()
  DessinTour()



def Damier():
  # Cette fonction permet de dessiner le damier.
  coordx, coordy = Origine, Origine
  valCoul=0 # Sert a faire le changement de couleur.

  for i in range(NbrCarree):
    for j in range(NbrCarree):

      # On cherche de quelle couleur est la case.
      if valCoul%2==0:
        coul='black'
      else:
        coul='white'

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
      print(matrice[i][j],  end='')

    # Apres l'affichage d'une ligne je saute une ligne.
    print("")


# def DeplacementPion(tour):
#   if tour==1:


def DebutDePartie():
  Damier()
  DessinAllPion()


########## Fin definition(s) ##########

########## Main ##########

# Gestion/ creation de la fentre et du caneva.
Win = Tk()
Win.title("Jeu d'echec")
Can = Canvas(Win, width = Sizex, height = Sizey, bg='white')
Can.pack()

# Dessin du damier.

DebutDePartie()
AffMatrice(MatriceCoords)

Win.mainloop()

########## Fin main ##########
