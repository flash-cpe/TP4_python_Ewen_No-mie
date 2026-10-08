# script animation_balle.py

from tkinter import *
import math,random

LARGEUR = 480
HAUTEUR = 320
RAYON = 15 # rayon de la balle

# position initiale au milieu
X = LARGEUR/2
Y = HAUTEUR/2

# direction initiale al�atoire
vitesse = random.uniform(1.8,2)*5
angle = random.uniform(0,2*math.pi)
#angle = 0
DX = vitesse*math.cos(angle)
DY = vitesse*math.sin(angle)

def deplacement():
    """ D�placement de la balle """
    global X,Y,DX,DY,RAYON,LARGEUR,HAUTEUR
    # rebond � droite
    if X+RAYON+DX > LARGEUR:
        X = 2*(LARGEUR-RAYON)-X
        DX = -DX
        
    # rebond � gauche
    if X-RAYON+DX < 0:
        X = 2*RAYON-X
        DX = -DX
    # rebond en bas
    if Y+RAYON+DY > HAUTEUR:
        Y = 2*(HAUTEUR-RAYON)-Y
        DY = -DY
    # rebond en haut
    if Y-RAYON+DY < 0:
        Y = 2*RAYON-Y
        DY = -DY
    
    X = X+DX
    Y = Y+DY
    # affichage
    Canevas.coords(Balle,X-RAYON,Y-RAYON,X+RAYON,Y+RAYON)
    # mise � jour toutes les 50 ms
    Mafenetre.after(50,deplacement)

# Cr�ation de la fen�tre principale
Mafenetre = Tk()
Mafenetre.title("Animation Balle")

# Cr�ation d'un widget Canvas
Canevas = Canvas(Mafenetre,height=HAUTEUR,width=LARGEUR,bg='black')
Canevas.pack(padx=5,pady=5)

# Cr�ation d'un objet graphique
Balle = Canevas.create_oval(X-RAYON,Y-RAYON,X+RAYON,Y+RAYON,width=1,outline='red',fill='blue')

deplacement()
Mafenetre.mainloop()
