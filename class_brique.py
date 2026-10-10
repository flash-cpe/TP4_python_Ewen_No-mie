"""
date : 8/10/2026
auteur : Ewen MORIETTE , Noemie DETOT
fonction : contient la class brique
a faire : utiliser soit une pile soit une file si possible 
idee : crer un liste pour les colenne de brique et chaque element de la liste et une pile (ou une file)
"""


class brique :

    def __init__(self, posX, posY, hauteur, largeur, couleur, canvas) :
        self.hauteur = hauteur
        self.largeur = largeur
        self.couleur = couleur
        self.canvas = canvas
        self.x = posX
        self.y = posY

        self.identifiant = canvas.create_rectangle(self.x, self.y, self.x + self.largeur,
                                                   self.y + self.hauteur, fill = self.couleur)


        def detruire(self) :
            self.canvas.delete(self.identifiant)
        
    

                