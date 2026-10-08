"""
date : 8/10/2026
auteur : Ewen MORIETTE , Noemie DETOT
fonction : contient la class balle
a faire : le code
"""
import random
import math
import tkinter as tk

class balle() :
    def __init__(self, rayon, centre,hauteur, largeur) :
        self.rayon = rayon
        self.centre = centre
        self.hauteur = hauteur
        self.largeur = largeur
        self.x = largeur/2
        self.y = hauteur/2
        
        self.vitesse = random(1.8,2)*5
        self.angle= random.uniform(0,2 * math.pi)
        self.DX = self.vitesse*math.cos(angle)
        self.DY = self.vitesse*math.sin(angle)


    def deplacement(self):
        if self.x + self.rayon + self.DX > self.largeur: #rebon a droite
            self.x = 2*(self.largeur- self.rayon)-self.x
            self.DX= -self.DX

        if self.x - self.rayon +self.DX<0: # rebon a gauche
            self.x= 2*(self.rayon-self.rayon)-self.x
            self.DX=-self.DX

        if self.y + self.rayon + self.DY > self.hauteur: #rebon en bas
            self.y=2*(self.hauteur- self.rayon)-self.y
            self.DY =- self.DY

        if self.y - self.rayon +self.DY<0: #rebon en haut
            self.y=2*(self.rayon-self.y)
            self.DY =- self.DY