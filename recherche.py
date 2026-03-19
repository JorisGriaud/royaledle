from tkinter import *
from PIL import Image, ImageTk
import os

class Recherche():
    def __init__(self, fenetre):
        self.fenetre = fenetre

        # Dimension bouton et image
        self.largeur_bouton = 30
        self.hauteur_bouton = 30

        # Dimension de la zone de saisie de texte
        self.largeur_entry = 300

        # Bouton envoyer
        self.image_bouton = Image.open("assets/bouton_entrer.png").resize((self.largeur_bouton, self.hauteur_bouton))  # Redimensionner à la taille du bouton
        self.photo_bouton = ImageTk.PhotoImage(self.image_bouton)
        self.bouton = Button(self.fenetre, image=self.photo_bouton, relief="flat", borderwidth=0, command=None)
        self.bouton.image = self.photo_bouton

        # Zone de texte
        self.entry = Entry(fenetre)
        self.entry.bind('<KeyRelease>', self.update_suggestions)

        # Canvas
        self.canvas = Canvas(self.fenetre, highlightthickness=0)
        self.canvas.pack(fill=BOTH, expand=True)
        self.canvas.bind("<Configure>", self.place_research)

    def update_suggestions(self):
        pass

    def place_research(self, event=None):
        if event:
            largeur = event.width
            hauteur = event.height
        else:
            self.canvas.update() # Force la mise à jour pour avoir les bonnes dimensions
            largeur = self.canvas.winfo_width()
            hauteur = self.canvas.winfo_height()
        
        x1 = (largeur - self.largeur_bouton) // 2
        y1 = (hauteur - self.hauteur_bouton) // 2

        self.bouton.place(x=x1 + self.largeur_entry, y=y1, width=self.largeur_bouton, height=self.hauteur_bouton)
        self.bouton.lift()

        self.entry.place(x=x1, y=y1, width=self.largeur_entry)




fenetre = Tk()
fenetre.title("RoyaleDLE - Test")
fenetre.geometry("1525x800") 
fenetre.iconbitmap("assets/logo.ico")

Recherche(fenetre)

fenetre.mainloop()
