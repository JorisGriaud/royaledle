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

def afficher_emoji(fenetre, card, num):
    global emoji_labels
    # Détruire les labels précédents
    for lbl in emoji_labels:
        lbl.destroy()
    emoji_labels = []
    emojis = card.get_emojis()
    for i in range(num):
        if i < len(emojis):
            path = "assets/emojis/" + emojis[i]
            img = Image.open(path).resize((largeur_carre, hauteur_carre))
            photo = ImageTk.PhotoImage(img)
            lbl = Label(fenetre, image=photo)
            lbl.image = photo
            lbl.place(x=630 + i * (largeur_carre + 5), y=350)
            emoji_labels.append(lbl)

def main(fenetre):
    global emoji_labels

    card = tirer_carte()
    nbtour = [1]  # on commence à 1 emoji affiché

    emoji_labels = []

    # Afficher le premier emoji au démarrage
    afficher_emoji(fenetre, card, nbtour[0])

    def carte_selec(nom_carte):
        if nbtour[0] < 4:
            nbtour[0] += 1              # on révèle un emoji de plus
            afficher_emoji(fenetre, card, nbtour[0])
        
        # Vérifier si la carte est la bonne
        if nom_carte.lower() == card.get_name().lower():
            image_bouton3 = Image.open("assets/Bienjoué.png").resize((500, 350))
            photo_bouton3 = ImageTk.PhotoImage(image_bouton3)
            bouton3 = Button(fenetre, image=photo_bouton3, relief="flat", borderwidth=0,command=lambda:[fenetre.after(0, bouton3.destroy()),recommencer()])
            bouton3.image = photo_bouton3 
            bouton3.place(x=500, y=150, width=500, height=500)
            bouton3.lift()


    def recommencer():
        nonlocal card
        card = tirer_carte()
        nbtour[0] = 1          
        afficher_emoji(fenetre, card, nbtour[0])

    recherche = Recherche(fenetre, all_cards_list, callback=carte_selec)

    fenetre.mainloop()

if __name__ == "__main__":
    fenetre = Tk()
    recherche = Recherche(fenetre, all_cards_list)
    fenetre.title("RoyaleDLE - Emoji")
    fenetre.geometry("1525x800")
    fenetre.iconbitmap("assets/logo.ico")
    main(fenetre)