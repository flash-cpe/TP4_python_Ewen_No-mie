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

    def text_score(self) :
        self.text_score = tk.Label(self.fenetre, text="Score :")
        self.text_score.pack(side= "top", padx= "400", pady= "50")

    def text_vie(self) :
        self.text_vie = tk.Label(self.fenetre, text="Score :")
        self.text_vie.pack(side= "top", padx= "400", pady= "50")
