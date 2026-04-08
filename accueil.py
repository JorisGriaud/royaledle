from tkinter import *
from PIL import Image, ImageTk

from recherche import Recherche
from classic import main as main_classic
from emoji import main as main_emoji
# from description import main as main_description

class Accueil():
    def __init__(self, fenetre):
        self.fenetre = fenetre
        # Charger l'image originale
        #image_originale = Image.open("fond.png")
        self.image_originale = Image.open("assets/unnamed.png")    
        self.photo_ref = None

        # Dimensions du rectangle
        self.largeur_rect = 400
        self.hauteur_rect = 100
        self.hauteur_fixe = 100

        # Dimension carré
        self.largeur_carre=75
        self.hauteur_carre=75
        self.hauteur_fixe=100

        self.image_bouton1 = Image.open("assets/classic.png").resize((self.largeur_carre, self.hauteur_carre))  # Redimensionner à la taille du bouton
        self.photo_bouton1 = ImageTk.PhotoImage(self.image_bouton1)
        self.bouton1 = Button(self.fenetre, image=self.photo_bouton1, relief="flat", borderwidth=0, command=lambda:[self.nettoyer_fenetre() ,self.classic()])
        self.bouton1.image = self.photo_bouton1 

        self.image_bouton2 = Image.open("assets/emoji.png").resize((self.largeur_carre, self.hauteur_carre))  # Redimensionner à la taille du bouton
        self.photo_bouton2 = ImageTk.PhotoImage(self.image_bouton2)
        self.bouton2 = Button(self.fenetre, image=self.photo_bouton2, relief="flat", borderwidth=0, command=lambda:[self.nettoyer_fenetre() ,self.emoji()])
        self.bouton2.image = self.photo_bouton2

        self.image_bouton3 = Image.open("assets/description.png").resize((self.largeur_carre, self.hauteur_carre))  # Redimensionner à la taille du bouton
        self.photo_bouton3 = ImageTk.PhotoImage(self.image_bouton3)
        self.bouton3 = Button(self.fenetre, image=self.photo_bouton3, relief="flat", borderwidth=0, command=lambda:[self.nettoyer_fenetre() ,self.classidescription()])
        self.bouton3.image = self.photo_bouton3

        self.image_bouton4 = Image.open("assets/descdeb.png").resize((self.largeur_rect, self.hauteur_rect))  # Redimensionner à la taille du bouton
        self.photo_bouton4 = ImageTk.PhotoImage(self.image_bouton4)
        self.bouton4 = Button(self.fenetre, image=self.photo_bouton4, relief="flat", borderwidth=0, command=lambda:[self.nettoyer_fenetre() ,self.description()])
        self.bouton4.image = self.photo_bouton4

        self.image_bouton5 = Image.open("assets/emojdeb.png").resize((self.largeur_rect, self.hauteur_rect))  # Redimensionner à la taille du bouton
        self.photo_bouton5 = ImageTk.PhotoImage(self.image_bouton5)
        self.bouton5 = Button(self.fenetre, image=self.photo_bouton5, relief="flat", borderwidth=0, command=lambda:[self.nettoyer_fenetre(),self.emoji()])
        self.bouton5.image = self.photo_bouton5

        self.image_bouton6 = Image.open("assets/classdeb.png").resize((self.largeur_rect, self.hauteur_rect))  # Redimensionner à la taille du bouton
        self.photo_bouton6 = ImageTk.PhotoImage(self.image_bouton6)
        self.bouton6 = Button(self.fenetre, image=self.photo_bouton6, relief="flat", borderwidth=0, command=lambda:[self.nettoyer_fenetre() ,self.classic()])
        self.bouton6.image = self.photo_bouton6

        self.logo = Image.open("assets/logoofficielroyaledle.png").resize((self.largeur_rect, self.hauteur_rect))  # Redimensionner à la taille du logo
        self.photo_logo = ImageTk.PhotoImage(self.logo)

        # Créer un Label avec l'image
        self.label_image = Label(self.fenetre, image=self.photo_logo,relief="flat", borderwidth=0)
        self.label_image.image = self.photo_logo  # Référence pour éviter la disparition

        # Canvas
        self.canvas = Canvas(self.fenetre, highlightthickness=0)
        self.canvas.pack(fill=BOTH, expand=True)
        self.canvas.bind("<Configure>", self.redimensionner_canvas_debut)

    def redimensionner_canvas(self, event=None):
        # Supprimer les anciens bouttons
        if self.bouton4 and self.bouton5 and self.bouton6:
            self.bouton4.destroy()
            self.bouton5.destroy()
            self.bouton6.destroy()

        # Redimensionner l'image
        if event:
            largeur = event.width
            hauteur = event.height
        else:
            self.canvas.update() # Force la mise à jour pour avoir les bonnes dimensions
            largeur = self.canvas.winfo_width()
            hauteur = self.canvas.winfo_height()

        self.image_redim = self.image_originale.resize((largeur, hauteur))
        self.photo_ref = ImageTk.PhotoImage(self.image_redim)

        # Effacer et redessiner
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.photo_ref, anchor=NW)

        x1 = (largeur - self.largeur_rect) // 2
        y1 = self.hauteur_fixe

        self.label_image.place(x=x1, y=y1-50,width=self.largeur_rect, height=self.hauteur_rect)  # Position du logo
        self.label_image.lift()

        # Placer le bouton et le mettre au-dessus
        self.bouton1.place(x=x1+65, y=y1 + 75, width=self.largeur_carre, height=self.hauteur_carre)
        self.bouton1.lift()

        self.bouton2.place(x=x1+165, y=y1 + 75, width=self.largeur_carre, height=self.hauteur_carre)
        self.bouton2.lift()

        self.bouton3.place(x=x1+265, y=y1 + 75, width=self.largeur_carre, height=self.hauteur_carre)
        self.bouton3.lift()

    def redimensionner_canvas_debut(self, event):
        # Redimensionner l'image
        self.image_redim = self.image_originale.resize((event.width, event.height))
        self.photo_ref = ImageTk.PhotoImage(self.image_redim)
        
        # Effacer et redessiner
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.photo_ref, anchor=NW)

        x1 = (event.width - self.largeur_rect) // 2
        y1 = self.hauteur_fixe    
    
        self.label_image.place(x=x1, y=y1-50,width=self.largeur_rect, height=self.hauteur_rect)  # Position du logo
        self.label_image.lift()

        # Placer le bouton et le mettre au-dessus
        self.bouton4.place(x=x1, y=y1+100, width=self.largeur_rect, height=self.hauteur_rect)
        self.bouton4.lift()

        self.bouton5.place(x=x1, y=y1+225, width=self.largeur_rect, height=self.hauteur_rect)
        self.bouton5.lift()

        self.bouton6.place(x=x1, y=y1+350, width=self.largeur_rect, height=self.hauteur_rect)
        self.bouton6.lift()
        
    def classic(self):
        self.redimensionner_canvas()
        main_classic(self.fenetre)
        return

    def emoji(self):
        self.redimensionner_canvas()
        main_emoji(self.fenetre)

        

    def description(self):
        self.redimensionner_canvas()
  
        return
    
    def nettoyer_fenetre(self):
        widgets_accueil = {self.bouton1, self.bouton2, self.bouton3, 
                        self.bouton4, self.bouton5, self.bouton6, 
                        self.label_image, self.canvas}
        for widget in self.fenetre.winfo_children():
            if widget not in widgets_accueil:
                widget.destroy()
        self.canvas.delete("all")