from Cards import Cards
from recherche import Recherche

from tkinter import *
from random import randint
from PIL import Image, ImageTk

from pathlib import Path

cards = Cards()
all_cards_list = cards.get_all_card_name_with_image_path()

# Dimensions du rectangle
largeur_rect = 400
hauteur_rect = 100
hauteur_fixe = 100

#dimension carré
largeur_carre=75
hauteur_carre=75
hauteur_fixe=100

image_originale = Image.open("assets/unnamed.png")    

def emojis(cards):
    nbre_cards = cards.get_number_of_cards()
    nbre_aleatoire = randint(0, nbre_cards) - 1
    card = cards.get_card_by_id(nbre_aleatoire)
    print(card.get_emojis()) # Debug
    return card

def main(fenetre):
    image_bouton2 = Image.open("assets/emoji.png").resize((largeur_carre, hauteur_carre))  # Redimensionner à la taille du bouton
    photo_bouton2 = ImageTk.PhotoImage(image_bouton2)
    bouton2 = Button(fenetre, image=photo_bouton2, relief="flat", borderwidth=0, command=emojis(cards))
    bouton2.image = photo_bouton2

    bouton2.place(x=100, y=100, width=largeur_carre, height=hauteur_carre)
    bouton2.lift()


    fenetre.mainloop()

if __name__ == "__main__":
    fenetre = Tk()
    fenetre.title("RoyaleDLE - Emoji")
    fenetre.geometry("1525x800") 
    fenetre.iconbitmap("assets/logo.ico")
    main(fenetre)