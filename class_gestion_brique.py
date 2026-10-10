"""
date : 10/10/2026
auteur : Ewen MORIETTE , Noemie DETOT
fonction : contient la class brique
a faire : faire en sorte d'adapte l'espace et la taille des briques pour que ca s'adapte a la taille du canvas
"""

from class_brique import brique

class gestion_brique :

    def __init__(self, canvas) :
        self.canvas = canvas
        self.liste_brique = []



    def creer_brique (self, posX ,posY, hauteur, largeur, espace, couleur, nb_ligne, nb_colonne) :
            for ligne in range(nb_ligne) :
                for colonne in range(nb_colonne) :
                    x = posX + colonne * (largeur + espace)
                    y = posY + ligne * (hauteur + espace)
    
                    self.canvas.create_rectangle(x, y, x + largeur, y + hauteur,
                                            fill = couleur)



                    Brique = brique(x, y, hauteur, largeur, couleur, self.canvas)
                    self.liste_brique.append(Brique)