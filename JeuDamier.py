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


########## Ensemble de definition(s) ##########

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
  # Cette fonctione affiche une matrice donnee en parametre
  for i in range(NbrCarree):
    for j in range(NbrCarree):
      # Normalement end='\n', la je veux juste un espace entre chaque affiche.
      print(matrice[i][j], end='')

    # Apres l'affichage d'une ligne je saute une ligne.
    print("")



def testVictoire():
  # Cette fonction permet verifier que tous les elements
  # de la matrice couelur sont noirs.
  somme = 0

  for i in range(NbrCarree):
    for j in range(NbrCarree):
      somme += MatriceCouleur[i][j]

  if somme == NbrCarree*NbrCarree:
    # On enleve la possibilite de cliquer.
    Can.unbind("<Button-1>")

    # On affiche.
    print("Victoire\nFin de partie")
    print("Nombre(s) de coup(s):", NbrCoup)
    # AffVictoire()



def SwitchVoisin(event):
  # Cette fonction permet de changer la couleurs de cases
  # voisines ou est situe le clic.

  # On indique les varibles en globale car on les modifies.
  global MatriceCouleur, NbrCoup

  coordx, coordy = 0, 0
  NbrCoup+=1

  # On cherche ou se situe le clic dans la matrice coords.
  for i in range(NbrCarree):
    for j in range(NbrCarree):
      if ((MatriceCoords[i][j][0] < event.x) & (MatriceCoords[i][j][1] < event.y) & (MatriceCoords[i][j][0] + Cote > event.x) & (MatriceCoords[i][j][1] + Cote > event.y)):
        coordx, coordy = j, i

  # On fait maintenant les changements de couleurs.

  # On verifie que le clic est bien dans le caneva.
  if ((Origine < event.x) & (event.x < (Size+Origine)) & (Origine < event.y) & (event.y < (Size+Origine))):

    # Test bordure gauche.
    if (coordx!=0):

      # La case a gauche est noire.
      if MatriceCouleur[coordy][coordx-1]==1:
        Carree(MatriceCoords[coordy][coordx-1][0], MatriceCoords[coordy][coordx-1][1], 'white')
        MatriceCouleur[coordy][coordx-1]=0

      # La case a gauche est blanche.
      else:
        Carree(MatriceCoords[coordy][coordx-1][0], MatriceCoords[coordy][coordx-1][1], 'black')
        MatriceCouleur[coordy][coordx-1]=1

    # Test bordure droite
    if (coordx!=NbrCarree-1):

      # La case a droite est noire.
      if MatriceCouleur[coordy][coordx+1]==1:
        Carree(MatriceCoords[coordy][coordx+1][0], MatriceCoords[coordy][coordx+1][1], 'white')
        MatriceCouleur[coordy][coordx+1]=0

      # La case a droite est blanche.
      else:
        Carree(MatriceCoords[coordy][coordx+1][0], MatriceCoords[coordy][coordx+1][1], 'black')
        MatriceCouleur[coordy][coordx+1]=1

    # Test bordure haut
    if (coordy!=0):

      # La case du haut est noire.
      if MatriceCouleur[coordy-1][coordx]==1:
        Carree(MatriceCoords[coordy-1][coordx][0], MatriceCoords[coordy-1][coordx][1], 'white')
        MatriceCouleur[coordy-1][coordx]=0

      # La case du haut est blanche.
      else:
        Carree(MatriceCoords[coordy-1][coordx][0], MatriceCoords[coordy-1][coordx][1], 'black')
        MatriceCouleur[coordy-1][coordx]=1

    # Test bordure basse
    if (coordy!=NbrCarree-1):

      # La case en bas est noire.
      if MatriceCouleur[coordy+1][coordx]==1:
        Carree(MatriceCoords[coordy+1][coordx][0], MatriceCoords[coordy+1][coordx][1], 'white')
        MatriceCouleur[coordy+1][coordx]=0

      # La case en bas est blanche.
      else:
        Carree(MatriceCoords[coordy+1][coordx][0], MatriceCoords[coordy+1][coordx][1], 'black')
        MatriceCouleur[coordy+1][coordx]=1

  # On regarde si toutes les cases sont desormais noires.
  testVictoire()

########## Fin definition(s) ##########

########## Main ##########

# Gestion/ creation de la fentre et du caneva.
Win = Tk()
Win.title("Damier")
Can = Canvas(Win, width = Sizex, height = Sizey, bg='white')
Can.pack()

# Dessin du damier et debut du jeu.
Damier()
Can.bind("<Button-1>", SwitchVoisin)

Win.mainloop()

########## Fin main ##########
