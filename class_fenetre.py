"""
date : 8/10/2026
auteur : Ewen MORIETTE , Noemie DETOT
fonction : contient la classe de la fenetre du jeu
a faire : impossibilité de mettre la fonction clavier dans la class barre car il y un probleme d'importation circulaire
"""
import random
import tkinter as tk
from class_barre import barre

class fenetre :

    def __init__(self):
        self.barre_info = barre(10, 100, "blue")
        self.fenetre = tk.Tk()
        self.fenetre.title("Casse Brique")

        self.frame = tk.Frame(self.fenetre)
        self.frame.pack(side = "top")

        self.text_score = tk.Label(self.frame, text = "Score :")
        self.text_score.pack(padx = "200", pady = "5", side ="right")

        self.text_vie = tk.Label(self.frame, text = "Vie :")
        self.text_vie.pack(padx = "5", pady = "5", side ="left")

        self.canvas=tk.Canvas(self.fenetre, width = 650, height = 650, bg = 'black')

        # position initiale du pion
        self.PosX = 320
        self.PosY = 620

        self.barre = self.canvas.create_rectangle(self.PosX - (self.barre_info.larguer / 2),
                                                  self.PosY - (self.barre_info.hauteur / 2),
                                                  self.PosX + (self.barre_info.larguer / 2),
                                                  self.PosY + (self.barre_info.hauteur / 2),
                                                  outline= self.barre_info.couleur,
                                                  fill= self.barre_info.couleur
                                                  )
        self.canvas.focus_set()
        self.canvas.bind('<Key>', self.clavier)
        self.canvas.pack()

        self.bouton_Jeu = tk.Button(self.fenetre, text = "démarrer une partie")
        self.bouton_Jeu.pack()

        self.bouton_fermer = tk.Button(self.fenetre, text = "quitter le jeu", fg = "red", command = self.fermer)
        self.bouton_fermer.pack(side = "bottom", pady = "5", padx = "5")



    def fermer(self):
        self.fenetre.destroy()

    def menu(self):
        self.menu_Principal= tk.Menu(self.fenetre)
        self.menu_nondetachable=tk.Menu(self.fenetre, tearoff = 0)
        self.menu_detachable= tk.Menu(self.fenetre, tearoff = 1)
        self.menu_Principal.add_cascade(label = "Menu1", menu = self.menu_nondetachable)
        self.menu_Principal.add_cascade(label = "Menu2", menu = self.menu_detachable)
        self.menu_detachable.add_command(labe = "Quitter", command = self.fermer)


        #self.menu_principal.add_command(label = "quitter", command = self.fermer)



    def clavier(self, event):
                self.largeur_canvas = self.canvas.winfo_width()
                """ Gestion de l'�v�nement Appui sur une touche du clavier """
                touche = event.keysym
                
                # d�placement vers la droite
                if touche == "Right" and (self.PosX + 20 + self.barre_info.larguer / 2) < self.largeur_canvas :
                    self.PosX += 20
                elif touche == "Right" :
                     self.PosX += self.largeur_canvas - (self.PosX + self.barre_info.larguer / 2)
                
                # d�placement vers la gauche
                if touche == "Left" and (self.PosX - 20 - self.barre_info.larguer / 2) > 0 :
                    self.PosX -= 20
                elif touche == "Left" :
                    self.PosX -= (self.PosX - self.barre_info.larguer / 2)
                
                # on dessine le pion � sa nouvelle position
                self.canvas.coords(self.barre,
                                   self.PosX - (self.barre_info.larguer / 2),
                                   self.PosY - (self.barre_info.hauteur / 2),
                                   self.PosX + (self.barre_info.larguer / 2),
                                   self.PosY + (self.barre_info.hauteur / 2)
                                   )
        
    

        


