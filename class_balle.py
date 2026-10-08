"""
date : 8/10/2026
auteur : Ewen MORIETTE , Noemie DETOT
fonction : contient la class balle
a faire : le code
"""


class balle() :
    def __init__(self, rayon, centre) :
        self.__rayon = rayon
        self.__centre = centre
        self.__x = centre[0]
        self.__y = centre[1]
        