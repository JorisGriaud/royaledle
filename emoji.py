from Cards import Cards
from recherche import Recherche
from tkinter import *
from random import randint
from PIL import Image, ImageTk

cards = Cards()
all_cards_list = cards.get_all_card_name_with_image_path()

largeur_carre = 75
hauteur_carre = 75

def tirer_carte():
    nbre_cards = cards.get_number_of_cards()
    nbre_aleatoire = randint(0, nbre_cards - 1)
    return cards.get_card_by_id(nbre_aleatoire)

def afficher_emoji(card, num):
    emojis = card.get_emojis()
    emoj_choisi = [emojis[i] for i in range(min(num, len(emojis)))]
    label_emoji.config(text=" ".join(emoj_choisi))

def main(fenetre):
    global label_emoji

    card = tirer_carte() 
    nbtour = [1]          # liste pour pouvoir modifier dans le lambda

    image_bouton2 = Image.open("assets/emoji.png").resize((largeur_carre, hauteur_carre))
    photo_bouton2 = ImageTk.PhotoImage(image_bouton2)
    bouton2 = Button(fenetre, image=photo_bouton2, relief="flat", borderwidth=0,
                     command=lambda: afficher_emoji(card, nbtour[0]))
    bouton2.image = photo_bouton2
    bouton2.place(x=100, y=100, width=largeur_carre, height=hauteur_carre)
    bouton2.lift()

    label_emoji = Label(fenetre, text="", font=("Segoe UI Emoji", 50))
    label_emoji.place(x=250, y=200)

    # Afficher le premier emoji au démarrage
    afficher_emoji(card, nbtour[0])

    fenetre.mainloop()

if __name__ == "__main__":
    fenetre = Tk()
    recherche = Recherche(fenetre)
    fenetre.title("RoyaleDLE - Emoji")
    fenetre.geometry("1525x800")
    fenetre.iconbitmap("assets/logo.ico")
    main(fenetre)