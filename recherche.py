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
        self.largeur_entry = 210

        # Texte placeholder zone de recherche
        self.placeholder = "Rechercher une carte ..."

        # Bouton envoyer
        self.image_bouton = Image.open("assets/bouton_entrer.png").resize((self.largeur_bouton, self.hauteur_bouton))  # Redimensionner à la taille du bouton
        self.photo_bouton = ImageTk.PhotoImage(self.image_bouton)
        self.bouton = Button(self.fenetre, image=self.photo_bouton, relief="flat", borderwidth=0, command=self.enter_button)
        self.bouton.image = self.photo_bouton

        # Zone de texte
        self.entry = Entry(fenetre, font=('Roboto', 12), fg='gray')
        self.entry.insert(0, self.placeholder)
        self.entry.bind('<FocusIn>', self.on_focus_in)
        self.entry.bind('<FocusOut>', self.on_focus_out)
        self.entry.bind('<KeyRelease>', self.update_suggestions)

        # Label
        self.label_carte = Label(self.fenetre,relief="flat", borderwidth=0, text='Carte')
        self.label_elixir = Label(self.fenetre,relief="flat", borderwidth=0, text="Coût d'élixir")
        self.label_rarete = Label(self.fenetre,relief="flat", borderwidth=0, text="Rareté")
        self.label_rarete = Label(self.fenetre,relief="flat", borderwidth=0, text="Type")
        self.label_rarete = Label(self.fenetre,relief="flat", borderwidth=0, text="Cible")
        self.label_rarete = Label(self.fenetre,relief="flat", borderwidth=0, text="Type de portée")
        self.label_rarete = Label(self.fenetre,relief="flat", borderwidth=0, text="Vitesse d'attaque")
        self.label_rarete = Label(self.fenetre,relief="flat", borderwidth=0, text="Vitesse")
        self.label_rarete = Label(self.fenetre,relief="solid", borderwidth=0, text="Date de sortie")

        # Canvas zone de recherche
        self.canvas1 = Canvas(self.fenetre, highlightthickness=0)
        self.canvas1.pack(fill=BOTH, expand=True)
        self.canvas1.bind("<Configure>", self.place_research)
        
        # Conteneur des suggestions
        self.container = Frame(fenetre, bg="white", highlightbackground="grey", highlightthickness=1)
        # self.scrollbar = Scrollbar(self.container, orient="vertical", command=self.canvas2.yview) # TODO

        # Canva suggestions
        self.canvas2 = Canvas(self.container, highlightthickness=0)
        self.canvas2.pack(fill=BOTH, expand=True)
        self.canvas2.bind("<Configure>", self.place_suggestion)

    def enter_button(self):
        pass
    
    def on_focus_in(self, event):
        if self.entry.get() == self.placeholder:
            self.entry.delete(0, END)
            self.entry.config(fg='black', font=('Roboto', 14))

    def on_focus_out(self, get):
        if self.entry.get() == "":
            self.entry.insert(0, self.placeholder)
            self.entry.config(fg='gray', font=('Roboto', 12))

    def update_suggestions(self, event):
        pass

    def place_research(self, event=None):
        if event:
            largeur = event.width
            hauteur = event.height
        else:
            self.canvas.update() # Force la mise à jour pour avoir les bonnes dimensions
            largeur = self.canvas.winfo_width()
            hauteur = self.canvas.winfo_height()
        
        largeur_totale = self.largeur_entry + self.largeur_bouton
        x1 = (largeur - largeur_totale) // 2
        y1 = (hauteur - self.hauteur_bouton) // 2

        self.bouton.place(x=x1 + self.largeur_entry, y=y1, width=self.largeur_bouton, height=self.hauteur_bouton)
        self.bouton.lift()

        self.entry.place(x=x1, y=y1, width=self.largeur_entry, height=self.hauteur_bouton)
        self.entry.lift()

    def place_suggestion(self, event=None):
        if event:
            largeur = event.width
            hauteur = event.height
        else:
            self.canvas.update() # Force la mise à jour pour avoir les bonnes dimensions
            largeur = self.canvas.winfo_width()
            hauteur = self.canvas.winfo_height()
        
        largeur_totale = self.largeur_entry + self.largeur_bouton
        x1 = (largeur - largeur_totale) // 2
        y1 = (hauteur - self.hauteur_bouton) // 2 + self.hauteur_bouton

        self.label_carte.place(x=x1,y=y1)


fenetre = Tk()
fenetre.title("RoyaleDLE - Test")
fenetre.geometry("1525x800") 
fenetre.iconbitmap("assets/logo.ico")

Recherche(fenetre)

fenetre.mainloop()
