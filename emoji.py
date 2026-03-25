from Cards import Cards
from recherche import Recherche

from tkinter import *
from random import randint
from PIL import Image, ImageTk

from pathlib import Path

cards = Cards()
all_cards_list = cards.get_all_card_name_with_image_path()
#recherche=Recherche()
# Dimensions du rectangle
largeur_rect = 400
hauteur_rect = 100
hauteur_fixe = 100

#dimension carré
largeur_carre=75
hauteur_carre=75
hauteur_fixe=100

image_originale = Image.open("assets/unnamed.png")    

def carte(cards):
    nbre_cards = cards.get_number_of_cards()
    nbre_aleatoire = randint(0, nbre_cards) - 1
    card = cards.get_card_by_id(nbre_aleatoire)
    return (card)

def emoji(carte):
    return carte.get_emojis()

def afficher_emoji():
    card = carte(cards)
    emojis = emoji(card)
    label_emoji.config(text=emojis)

def main(fenetre):
    global label_emoji
    
    image_bouton2 = Image.open("assets/emoji.png").resize((largeur_carre, hauteur_carre))  # Redimensionner à la taille du bouton
    photo_bouton2 = ImageTk.PhotoImage(image_bouton2)
    bouton2 = Button(fenetre, image=photo_bouton2, relief="flat", borderwidth=0, command=afficher_emoji)
    bouton2.image = photo_bouton2
    bouton2.place(x=100, y=100, width=largeur_carre, height=hauteur_carre)
    bouton2.lift()
    
    # Label pour afficher les emojis
    label_emoji = Label(fenetre, text="", font=("Segoe UI Emoji", 50))
    label_emoji.place(x=250, y=200)

    #while recherche != card:
        
        
        
    #image_bouton2 = Image.open(f"assets/clash_royale_cards/{card}.png").resize(largeur_carre+300, hauteur_carre+100)
    #photo_bouton2 = ImageTk.PhotoImage(image_bouton2)
    #bouton2 = Button(fenetre, image=photo_bouton2,relief="flat", borderwidth=0, command=lambda: bouton2.destroy())

    fenetre.mainloop()

if __name__ == "__main__":
    fenetre = Tk()
    fenetre.title("RoyaleDLE - Emoji")
    fenetre.geometry("1525x800") 
    fenetre.iconbitmap("assets/logo.ico")
    main(fenetre)