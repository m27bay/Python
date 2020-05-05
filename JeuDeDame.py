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

# Taille du damier.
NbrCarree=10

# On creer une matrice pour enregistre la couleur de chaque cases du damier: 1=noir, 0=blanc.
MatriceCouleur = [[0] * NbrCarree for _ in range(NbrCarree)]

# On creer une matrice pour enregistre les coordonnees du point en
# haut a gauche pour chaque case.
MatriceCoords = [[0] * NbrCarree for _ in range(NbrCarree)]

TabDeJeu = [[0] * (NbrCarree+1) for _ in range(NbrCarree+1)]

# Taille de caneva.
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
      if valCoul%2!=0:
        coul='#D76100'
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



def InitTabDeJeu(tabJeu):

  for i in range(1, NbrCarree+1):
    tabJeu[0][i] = i

  for i in range(1, NbrCarree+1):
    tabJeu[i][0] = i



def DessinPion(tabJeu, posX, posY, joueur):

  coul = 'black'
  diametre = Cote-2
  coordx, coordy = Origine+((posX-1)*Cote),  Origine+((posY-1)*Cote)

  if (joueur=="J2"): coul='white'
  Can.create_oval(coordx+2, coordy+2, coordx+diametre, coordy+diametre, fill=coul)
  tabJeu[posY][posX]=joueur



def DessinPionJ1(tabJeu):

  for i in range(2, NbrCarree+1, 2):
    for j in range(1, 5):
      if(j%2!=0): DessinPion(tabJeu, i, j, "J1")
      else: DessinPion(tabJeu, (i-1), j, "J1")



def DessinPionJ2(tabJeu):

  for i in range(2, NbrCarree+1, 2):
    for j in range(7, NbrCarree+1):
      if(j%2!=0): DessinPion(tabJeu, i, j, "J2")
      else: DessinPion(tabJeu, (i-1), j, "J2")



def DessinAllPions(tabJeu):

  DessinPionJ1(tabJeu)
  DessinPionJ2(tabJeu)



def FoundPion(event, case):
  caseX, caseY = 0, 0
  while(event.x>Origine+(caseX*Cote)): caseX+=1
  while(event.y>Origine+(caseY*Cote)): caseY+=1
  case.append(caseX-1)
  case.append(caseY-1)

  return case



def SelectionPion(coordx, coordy):
  diametre = Cote-2
  Can.create_oval(coordx+2, coordy+2, coordx+diametre, coordy+diametre, fill='red')



def EstVide(caseX, caseY):
  print(caseX, caseY)
  if ((TabDeJeu[caseY][caseX]=='J1') | (TabDeJeu[caseY][caseX]=='J2')):
    return 0
  else:
    return 1



def AffCaseMvt(caseX, caseY, coordx, coordy, numjoueur):
  if numjoueur==1:
    if(EstVide(caseX+1, caseY+1)==1):
      Carree(coordx+Cote, coordy+Cote, 'red')
    if(EstVide(caseX-1, caseY+1)==1):
      Carree(coordx-Cote, coordy+Cote, 'red')
  elif numjoueur==2:
    if(EstVide(caseX+1, caseY+1)==1):
      Carree(coordx+Cote, coordy-Cote, 'red')
    if(EstVide(caseX-1, caseY-1)==1):
      Carree(coordx-Cote, coordy-Cote, 'red')



def DeplacementPionJ1(event):
  case = []
  case = FoundPion(event, case)
  caseX, caseY = case[0], case[1]

  coordx, coordy = Origine+(caseX*Cote), Origine+(caseY*Cote)

  if(TabDeJeu[caseY+1][caseX+1]=='J1'):
    SelectionPion(coordx, coordy)
    AffCaseMvt(caseX, caseY, coordx, coordy, 1)





def JeuDeDame():
  Damier()
  InitTabDeJeu(TabDeJeu)
  DessinAllPions(TabDeJeu)
  tour = 0

  if(tour%2==0):
    Can.bind("<Button-1>", DeplacementPionJ1)
  # else
  tour+=1
  AffMatrice(TabDeJeu, NbrCarree+1)



def AffMatrice(matrice, taille):
  for i in range(taille):
    for j in range(taille):
      # Normalement end='\n', la je veux juste un espace entre chaque affiche.
      print(matrice[i][j], end='')
    # Apres l'affichage d'une ligne je saute une ligne.
    print("")

########## Fin definition(s) ##########

########## Main ##########

# Gestion/ creation de la fentre et du caneva.
Win = Tk()
Win.title("Jeu de dame")
Can = Canvas(Win, width = Sizex, height = Sizey, bg='white')
Can.pack()

# Dessin du damier.
JeuDeDame()

Win.mainloop()

########## Fin main ##########
