"""
date : 8/10/2026
auteur : Ewen MORIETTE , Noemie DETOT
fonction : contient la class barre
a faire : le code
"""
from class_fenetre import fenetre

class barre :
    
    def __init__(self, hauteur, largeur, couleur) :
        self.hauteur = str(hauteur)
        self.larguer = str(largeur)
        self.couleur = couleur
        self.mw = fenetre()

    def clavier(self, event):
            """ Gestion de l'�v�nement Appui sur une touche du clavier """
            touche = event.keysym
            # d�placement vers la droite
            if touche == "Right" :
                self.mw.PosX += 20
            # d�placement vers la gauche
            if touche == "Left":
                self.mw.PosX -= 20
            # on dessine le pion � sa nouvelle position
            self.mw.canvas.coords(self.mw.barre_creation, self.mw.PosX -50, self.mw.PosY -5, self.mw.PosX +50, self.mw.PosY +5)
    