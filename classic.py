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
    nbre_aleatoire = randint(0, nbre_cards)
    card = cards.get_card_by_id(nbre_aleatoire)
    print(card.get_name()) # Debug
    return card

def OnSearchInput(valeur):
    # print(f'La description est : {cards.get_card_by_name(valeur).get_description()}')
    return cards.get_card_by_name(valeur)

def main(fenetre):

    # Label
    # self.label_carte = Label(self.fenetre,relief="flat", borderwidth=0, text='Carte')
    # self.label_elixir = Label(self.fenetre,relief="flat", borderwidth=0, text="Coût d'élixir")
    # self.label_rarete = Label(self.fenetre,relief="flat", borderwidth=0, text="Rareté")
    # self.label_rarete = Label(self.fenetre,relief="flat", borderwidth=0, text="Type")
    # self.label_rarete = Label(self.fenetre,relief="flat", borderwidth=0, text="Cible")
    # self.label_rarete = Label(self.fenetre,relief="flat", borderwidth=0, text="Type de portée")
    # self.label_rarete = Label(self.fenetre,relief="flat", borderwidth=0, text="Vitesse d'attaque")
    # self.label_rarete = Label(self.fenetre,relief="flat", borderwidth=0, text="Vitesse")
    # self.label_rarete = Label(self.fenetre,relief="solid", borderwidth=0, text="Date de sortie")
    Recherche(fenetre, all_cards_list, OnSearchInput)

    

if __name__ == "__main__":
    fenetre = Tk()
    fenetre.title("RoyaleDLE - Classic")
    fenetre.geometry("1525x800")
    fenetre.iconbitmap("assets/logo.ico")
    
    main(fenetre)

    fenetre.mainloop()