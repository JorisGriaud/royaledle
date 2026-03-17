from tkinter import *
from PIL import Image, ImageTk
from pathlib import Path
dossier = Path("assets")
fichiers_png = list(dossier.glob("*.png"))
fichiers_ico = list(dossier.glob("*.ico"))

fenetre = Tk()
fenetre.title("RoyaleDLE")
fenetre.geometry("1525x800") 
fenetre.iconbitmap(dossier/"logo.ico")

# Charger l'image originale
#image_originale = Image.open("fond.png")
image_originale = Image.open(dossier/"unnamed.png")    
photo_ref = None

# Dimensions du rectangle
largeur_rect = 400
hauteur_rect = 100
hauteur_fixe = 100

#dimension carré
largeur_carre=75
hauteur_carre=75
hauteur_fixe=100

def classic(): #programme manu
    pass

def emoji(): #programme evan
    pass

def description():
    pass

image_bouton1 = Image.open(dossier/"classic.png").resize((largeur_carre, hauteur_carre))  # Redimensionner à la taille du bouton
photo_bouton1 = ImageTk.PhotoImage(image_bouton1)
bouton1 = Button(fenetre, image=photo_bouton1, relief="flat", borderwidth=0, command=lambda: classic)
bouton1.image = photo_bouton1 

image_bouton2 = Image.open(dossier/"emoji.png").resize((largeur_carre, hauteur_carre))  # Redimensionner à la taille du bouton
photo_bouton2 = ImageTk.PhotoImage(image_bouton2)
bouton2 = Button(fenetre, image=photo_bouton2, relief="flat", borderwidth=0, command=lambda: emoji)
bouton2.image = photo_bouton2

image_bouton3 = Image.open(dossier/"description.png").resize((largeur_carre, hauteur_carre))  # Redimensionner à la taille du bouton
photo_bouton3 = ImageTk.PhotoImage(image_bouton3)
bouton3 = Button(fenetre, image=photo_bouton3, relief="flat", borderwidth=0, command=lambda: description)
bouton3.image = photo_bouton3

image_bouton4 = Image.open(dossier/"descdeb.png").resize((largeur_rect, hauteur_rect))  # Redimensionner à la taille du bouton
photo_bouton4 = ImageTk.PhotoImage(image_bouton4)
bouton4 = Button(fenetre, image=photo_bouton4, relief="flat", borderwidth=0, command=lambda: classic)
bouton4.image = photo_bouton4

image_bouton5 = Image.open(dossier/"emojdeb.png").resize((largeur_rect, hauteur_rect))  # Redimensionner à la taille du bouton
photo_bouton5 = ImageTk.PhotoImage(image_bouton5)
bouton5 = Button(fenetre, image=photo_bouton5, relief="flat", borderwidth=0, command=lambda: emoji)
bouton5.image = photo_bouton5

image_bouton6 = Image.open(dossier/"classdeb.png").resize((largeur_rect, hauteur_rect))  # Redimensionner à la taille du bouton
photo_bouton6 = ImageTk.PhotoImage(image_bouton6)
bouton6 = Button(fenetre, image=photo_bouton6, relief="flat", borderwidth=0, command=lambda: description)
bouton6.image = photo_bouton6

logo = Image.open(dossier/"logoofficielroyaledle.png").resize((largeur_rect, hauteur_rect+200))  # Redimensionner à la taille du logo
photo_logo = ImageTk.PhotoImage(logo)

# Créer un Label avec l'image
label_image = Label(fenetre, image=photo_logo,relief="flat", borderwidth=0)
label_image.image = photo_logo  # Référence pour éviter la disparition


def redimensionner_canvas(event):
    global photo_ref
    # Redimensionner l'image
    image_redim = image_originale.resize((event.width, event.height))
    photo_ref = ImageTk.PhotoImage(image_redim)
    
    # Effacer et redessiner
    canvas.delete("all")
    canvas.create_image(0, 0, image=photo_ref, anchor=NW)

    x1 = (event.width - largeur_rect) // 2
    y1 = hauteur_fixe    
    
    label_image.place(x=x1, y=y1-50,width=largeur_rect, height=hauteur_rect)  # Position du logo
    label_image.lift()

    # Placer le bouton et le mettre au-dessus
    bouton1.place(x=x1+65, y=y1+75, width=largeur_carre, height=hauteur_carre)
    bouton1.lift()

    bouton2.place(x=x1+165, y=y1+75, width=largeur_carre, height=hauteur_carre)
    bouton2.lift()

    bouton3.place(x=x1+265, y=y1+75, width=largeur_carre, height=hauteur_carre)
    bouton3.lift()

    


def redimensionner_canvas_debut(event):
    global photo_ref
    # Redimensionner l'image
    image_redim = image_originale.resize((event.width, event.height))
    photo_ref = ImageTk.PhotoImage(image_redim)
    
    # Effacer et redessiner
    canvas.delete("all")
    canvas.create_image(0, 0, image=photo_ref, anchor=NW)

    x1 = (event.width - largeur_rect) // 2
    y1 = hauteur_fixe    
   
    label_image.place(x=x1, y=y1-50,width=largeur_rect, height=hauteur_rect)  # Position du logo
    label_image.lift()

    # Placer le bouton et le mettre au-dessus
    bouton4.place(x=x1, y=y1+100, width=largeur_rect, height=hauteur_rect)
    bouton4.lift()

    bouton5.place(x=x1, y=y1+225, width=largeur_rect, height=hauteur_rect)
    bouton5.lift()

    bouton6.place(x=x1, y=y1+350, width=largeur_rect, height=hauteur_rect)
    bouton6.lift()


# Canvas
canvas = Canvas(fenetre, highlightthickness=0)
canvas.pack(fill=BOTH, expand=True)
canvas.bind("<Configure>", redimensionner_canvas_debut)

fenetre.mainloop()