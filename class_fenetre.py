"""
date : 8/10/2026
auteur : Ewen MORIETTE , Noemie DETOT
fonction : contient la classe de la fenetre du jeu
a faire : le code
"""
import random
import tkinter as tk

class fenetre:
    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.title("Casse Brique")

        self.frame = tk.Frame(self.fenetre)
        self.frame.pack(side="top")

        self.text_score = tk.Label(self.frame, text="Score :")
        self.text_score.pack(padx= "200", pady= "5", side="right")

        self.text_vie = tk.Label(self.frame, text="Vie :")
        self.text_vie.pack(padx= "5", pady= "5", side="left")

        self.canvas=tk.Canvas(self.fenetre, width=650,height=650, bg='black')
        self.canvas.pack()

        self.boutonJeu = tk.Button(self.fenetre, text= "démarrer une partie")

        self.bouton_fermer = tk.Button(self.fenetre, text= "quitter le jeu", fg= "red", command= self.fermer)
        self.bouton_fermer.pack(side="bottom", pady ="5", padx= "5")



    def fermer(self):
        self.fenetre.destroy()

    def menu(self):
        self.menu_Principal= tk.Menu(self.fenetre)
        self.menu_principal.add_command(label="quitter",command=self.fermer)




        


