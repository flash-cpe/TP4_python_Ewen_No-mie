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

        self.text_score = tk.Label(self.fenetre, text="Score :")
        self.text_score.pack(side= "top", padx= "400", pady= "50")

        self.text_vie = tk.Label(self.fenetre, text="Vie :")
        self.text_vie.pack(side= "top", padx= "50", pady= "50")

        self.canvas=tk.Canvas(self.fenetre, width=650,height=650, bg='black')
        self.canvas.pack()

        self.boutonJeu = tk.Button(self.fentre, text= "démarrer une partie")

        self.bouton_fermer = tk.Button(self.fenetre, text= "quitter le jeu", fg= "red", command= self.fermer())
        self.bouton_fermer.pack(side="bottom", pady ="50")

    def fermer(self):
        self.fenetre.destroy()

    def menu(self):
        self.menu_Principal= tk.Menu(self.fenetre)
        self.menu_principal.add_command(label="quitter",command=self.fermer)

        


