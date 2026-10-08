"""
date : 8/10/2026
auteur : Ewen MORIETTE , Noemie DETOT
fonction : contient la class balle
a faire : le code
"""


class balle() :
    def __inti__(self, rayon, centre) :
        self.rayon = rayon
        self.centre = centre
        self.x = centre[0]
        self.y = centre[1]
        