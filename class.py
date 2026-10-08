"""
date : 8/10/2026
auteur : Ewen MORIETTE , Noemie DETOT
fonction : contient la classe de la fenetre du jeu
a faire : le code
"""
import random
import tkinter as tk

class fenetre:
    def __init__(self, value):
        self.fenetre = tk.Tk()
        self.fenetre.title("Casse Brique")
        self.canvas.pack()
        self.canvas=tk.Canvas(self.fenetre, width=650,height=650, bg='black')
        self.canvas.pack()
        self.boutonJeu = tk.Button(self.fentre, text= "démarrer une partie")
        

    def fermer(self):
        self.fenetre.destroy()
