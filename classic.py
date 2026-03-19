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

def GetRandomCard():
    nbre_cards = cards.get_number_of_cards()
    nbre_aleatoire = randint(0, nbre_cards) - 1
    card = cards.get_card_by_id(nbre_aleatoire)
    print(card.get_name()) # Debug
    return card

def main(fenetre):
    image_bouton1 = Image.open("assets/classic.png").resize((largeur_carre, hauteur_carre))  # Redimensionner à la taille du bouton
    photo_bouton1 = ImageTk.PhotoImage(image_bouton1)
    bouton1 = Button(fenetre, image=photo_bouton1, relief="flat", borderwidth=0, command=GetRandomCard)
    bouton1.image = photo_bouton1 

    bouton1.place(x=100, y=100, width=largeur_carre, height=hauteur_carre)
    bouton1.lift()

    Recherche(fenetre, all_cards_list)

    fenetre.mainloop()

if __name__ == "__main__":
    fenetre = Tk()
    fenetre.title("RoyaleDLE - Classic")
    fenetre.geometry("1525x800") 
    fenetre.iconbitmap("assets/logo.ico")
    main(fenetre)