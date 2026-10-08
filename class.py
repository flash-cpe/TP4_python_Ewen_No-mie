import random
import tkinter as tk

class Canvas:
    def __init__(self, value):
        self.fenetre = tk.Tk()
        self.fenetre.title("Casse Brique")
        self.canvas=tk.Canvas(self.fenetre, width=650,height=650, bg='black')

    def fermer(self):
        self.fenetre.destroy()

    def boutons(self):
        #self.boutonJeu =