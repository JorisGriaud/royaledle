from Cards import Cards
from recherche import Recherche
from tkinter import *
from random import randint
from PIL import Image, ImageTk
import webbrowser

cards = Cards()

largeur_carre = 75
hauteur_carre = 75

def pub(fenetre):
    image_boutonpub = Image.open("assets/pub.png").resize((400, 500))
    photo_boutonpub = ImageTk.PhotoImage(image_boutonpub)
    boutonpub = Button(fenetre, image=photo_boutonpub, relief="flat", borderwidth=0,command=lambda: webbrowser.open("https://www.helloasso.com/associations/bde-eseo-angers/evenements/le-cercle-d-ardoise-studio-eseo?utm_source=ig&utm_medium=social&utm_content=link_in_bio"))
    boutonpub.image = photo_boutonpub 
    boutonpub.place(x=1100, y=150, width=400, height=500)
    boutonpub.lift()
    image_boutonpub2 = Image.open("assets/pub.png").resize((400, 500))
    photo_boutonpub2 = ImageTk.PhotoImage(image_boutonpub2)
    boutonpub2 = Button(fenetre, image=photo_boutonpub2, relief="flat", borderwidth=0,command=lambda: webbrowser.open("https://www.helloasso.com/associations/bde-eseo-angers/evenements/le-cercle-d-ardoise-studio-eseo?utm_source=ig&utm_medium=social&utm_content=link_in_bio"))
    boutonpub2.image = photo_boutonpub2 
    boutonpub2.place(x=30, y=150, width=400, height=500)
    boutonpub2.lift()


def tirer_carte():
    nbre_cards = cards.get_number_of_cards()
    nbre_aleatoire = randint(0, nbre_cards - 1)
    return cards.get_card_by_id(nbre_aleatoire)

def afficher_emoji(fenetre, card, num):
    global emoji_labels
    # Détruire les labels précédents des emojis
    for label in emoji_labels:
        label.destroy()
    emoji_labels = []
    emojis = card.get_emojis()
    for i in range(num):
        if i < len(emojis):
            emoji_name = emojis[i]
            # Ajouter l'extension .png si elle n'est pas présente
            if not emoji_name.endswith('.png'):
                emoji_name += '.png'
            path = "assets/emojis/" + emoji_name
            img = Image.open(path).resize((largeur_carre, hauteur_carre))
            photo = ImageTk.PhotoImage(img)
            lbl = Label(fenetre, image=photo)
            lbl.image = photo
            lbl.place(x=630 + i * (largeur_carre + 5), y=350)
            emoji_labels.append(lbl)

def main(fenetre):
    all_cards_list = cards.get_all_card_name_with_image_path()
    global emoji_labels
    pub(fenetre)
    card = tirer_carte()
    nbtour = [1]  # on commence à 1 emoji affiché

    emoji_labels = []
    wrong_labels = []

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
            bouton3.place(x=500, y=150, width=500, height=350)
            bouton3.lift()
        
        else :
            bonnecarte = None
            for item in all_cards_list:
                if item["name"] == nom_carte:
                    bonnecarte = item["path"]
                    break
            if bonnecarte:
                img = Image.open(bonnecarte).resize((largeur_carre, hauteur_carre))
                photo = ImageTk.PhotoImage(img)
                label = Label(fenetre, image=photo)
                label.image = photo
                label.place(x=700, y=450 + len(wrong_labels) * (largeur_carre + 5))
                wrong_labels.append(label)

    def recommencer():
        nonlocal card, wrong_labels
        # Détruire les labels des mauvaises suppositions
        for label in wrong_labels:
            label.destroy()
        wrong_labels = []
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