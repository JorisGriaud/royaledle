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

def main(fenetre):
    card_to_guess = GetRandomCard()

    hauteur = fenetre.winfo_height()

    # Frame pour tout les labels 
    labels_frame = Frame(fenetre, bg="white")
    labels_frame.place(x=0, y=hauteur//2, relwidth=1, height=hauteur//3)
    
    # Label
    label_carte = Label(labels_frame, relief="flat", borderwidth=0, text='Carte', font=16)
    label_elixir = Label(labels_frame, relief="flat", borderwidth=0, text="Coût d'élixir", font=16)
    label_rarete = Label(labels_frame, relief="flat", borderwidth=0, text="Rareté", font=16)
    label_type = Label(labels_frame, relief="flat", borderwidth=0, text="Type", font=16)
    label_cible = Label(labels_frame, relief="flat", borderwidth=0, text="Cible", font=16)
    label_portee = Label(labels_frame, relief="flat", borderwidth=0, text="Portée", font=16)
    label_vitesse_attaque = Label(labels_frame, relief="flat", borderwidth=0, text="Vitesse d'attaque", font=16)
    label_vitesse = Label(labels_frame, relief="flat", borderwidth=0, text="Vitesse", font=16)
    label_date = Label(labels_frame, relief="solid", borderwidth=0, text="Date de sortie", font=16)
 
    labels_frame.columnconfigure(0, weight=1)
    labels_frame.columnconfigure(1, weight=1)
    labels_frame.columnconfigure(2, weight=1)
    labels_frame.columnconfigure(3, weight=1)
    labels_frame.columnconfigure(4, weight=1)
    labels_frame.columnconfigure(5, weight=1)
    labels_frame.columnconfigure(6, weight=1)
    labels_frame.columnconfigure(7, weight=1)
    labels_frame.columnconfigure(8, weight=1)
    
    label_carte.grid(row=0, column=0, pady=10)
    label_elixir.grid(row=0, column=1, pady=10)
    label_rarete.grid(row=0, column=2, pady=10)
    label_type.grid(row=0, column=3, pady=10)
    label_cible.grid(row=0, column=4, pady=10)
    label_portee.grid(row=0, column=5, pady=10)
    label_vitesse_attaque.grid(row=0, column=6, pady=10)
    label_vitesse.grid(row=0, column=7, pady=10)
    label_date.grid(row=0, column=8, pady=10)
    
    # Afficher les données carte
    data_carte = Label(labels_frame, relief="flat", borderwidth=0, image=None, font=12)
    data_elixir = Label(labels_frame, relief="flat", borderwidth=0, text="", font=12)
    data_rarete = Label(labels_frame, relief="flat", borderwidth=0, text="", font=12)
    data_type = Label(labels_frame, relief="flat", borderwidth=0, text="", font=12)
    data_cible = Label(labels_frame, relief="flat", borderwidth=0, text="", font=12)
    data_portee = Label(labels_frame, relief="flat", borderwidth=0, text="", font=12)
    data_vitesse_attaque = Label(labels_frame, relief="flat", borderwidth=0, text="", font=12)
    data_vitesse = Label(labels_frame, relief="flat", borderwidth=0, text="", font=12)
    data_date = Label(labels_frame, relief="solid", borderwidth=0, text="", font=12)

    data_carte.grid(row=1, column=0, pady=10)
    data_elixir.grid(row=1, column=1, pady=10)
    data_rarete.grid(row=1, column=2, pady=10)
    data_type.grid(row=1, column=3, pady=10)
    data_cible.grid(row=1, column=4, pady=10)
    data_portee.grid(row=1, column=5, pady=10)
    data_vitesse_attaque.grid(row=1, column=6, pady=10)
    data_vitesse.grid(row=1, column=7, pady=10)
    data_date.grid(row=1, column=8, pady=10)

    rarity_values = cards.get_rarity_values()
    rarity_dic = {}
    for index_rarity in range(len(rarity_values)): 
        rarity_dic[rarity_values[index_rarity]] = index_rarity

    speed_values = cards.get_speed_values()
    speed_dict = {}
    for index_speed in range(len(speed_values)):
        speed_dict[speed_values[index_speed]] = index_speed
        
    def OnSearchInput(valeur):
        card = cards.get_card_by_name(valeur)
        if card:
            img = Image.open(card.get_icon_path()).resize((42, 52), Image.Resampling.LANCZOS)
            image = ImageTk.PhotoImage(img)
            data_carte.image = image
            
            if card.get_name() == card_to_guess.get_name():
                data_carte.config(image=image, bg='#42F31F')
            else:
                data_carte.config(image=image, bg='red')

            # "⬆️ ⬇️"
            if card.get_elixir() == card_to_guess.get_elixir():
                data_elixir.config(text=str(card.get_elixir()), bg='#42F31F')
            elif card.get_elixir() > card_to_guess.get_elixir():
                data_elixir.config(text=str(card.get_elixir()) + "   ⬇️", bg="red")
            elif card.get_elixir() < card_to_guess.get_elixir():
                data_elixir.config(text=str(card.get_elixir()) + "   ⬆️", bg="red")

            # "⬆️ ⬇️"
            if card.get_rarity() == card_to_guess.get_rarity():
                data_rarete.config(text=card.get_rarity(), bg="#42F31F")
            elif rarity_dic[card.get_rarity()] > rarity_dic[card_to_guess.get_rarity()]:
                data_rarete.config(text=card.get_rarity() + "   ⬇️", bg='red')
            elif rarity_dic[card.get_rarity()] < rarity_dic[card_to_guess.get_rarity()]:
                data_rarete.config(text=card.get_rarity() + "   ⬆️", bg='red')

            if card.get_type() == card_to_guess.get_type():
                data_type.config(text=card.get_type(), bg="#42F31F")
            else:
                data_type.config(text=card.get_type(), bg='red')
            
            if card.get_targets() == card_to_guess.get_targets():
                data_cible.config(text=card.get_targets(), bg="#42F31F")
            else:
                data_cible.config(text=card.get_targets(), bg='red')
            
            if card.get_range() == card_to_guess.get_range():
                data_portee.config(text=card.get_range(), bg="#42F31F")
            else:
                data_portee.config(text=card.get_range(), bg='red')
            
            # "⬆️ ⬇️"
            if card.get_hit_speed() == card_to_guess.get_hit_speed():
                data_vitesse_attaque.config(text=card.get_hit_speed(), bg="#42F31F")
            elif card.get_hit_speed() == None:
                data_vitesse_attaque.config(text="S.O   ⬆️" , bg="red")
            elif card_to_guess.get_hit_speed() == None:
                data_vitesse_attaque.config(text="S.O   ⬇️" , bg="red")
            # elif isinstance(card.get_hit_speed(), float) and isinstance(card_to_guess.get_hit_speed(), float):
            elif card.get_hit_speed() > card_to_guess.get_hit_speed():
                data_vitesse_attaque.config(text=str(card.get_hit_speed()) + "s"  + "   ⬇️" , bg="red")
            elif card.get_hit_speed() < card_to_guess.get_hit_speed():
                data_vitesse_attaque.config(text=str(card.get_hit_speed()) + "s" + "   ⬆️", bg="red")
            # elif isinstance(card.get_hit_speed(), str):
            #     data_vitesse_attaque.config(text=str(card.get_hit_speed()) + "s" + "   ⬆️", bg="red")
            # elif isinstance(card_to_guess.get_hit_speed(), str):
            #     data_vitesse_attaque.config(text=str(card.get_hit_speed()) + "s"  + "   ⬇️" , bg="red")


            # "⬆️ ⬇️"
            if card.get_speed() == None and card_to_guess.get_speed() == None:
                data_vitesse.config(text="S.O", bg="#42F31F")
            elif card.get_speed() == card_to_guess.get_speed():
                data_vitesse.config(text=card.get_speed(), bg="#42F31F")
            elif card.get_speed() == None:
                data_vitesse.config(text="S.O   ⬆️", bg='red')
            elif card_to_guess.get_speed() == None:
                data_vitesse.config(text="S.O   ⬇️", bg='red')
            elif speed_dict[card.get_speed()] > speed_dict[card_to_guess.get_speed()]:
                data_vitesse.config(text=card.get_speed() + "   ⬇️", bg='red')
            elif speed_dict[card.get_speed()] < speed_dict[card_to_guess.get_speed()]:
                data_vitesse.config(text=card.get_speed() + "   ⬆️", bg='red')
            
            # "⬆️ ⬇️"
            if card.get_release_year() == card_to_guess.get_release_year():
                data_date.config(text=card.get_release_year(), bg="#42F31F")
            elif card.get_release_year() > card_to_guess.get_release_year():
                data_date.config(text=str(card.get_release_year()) + "   ⬇️", bg='red')
            elif card.get_release_year() < card_to_guess.get_release_year():
                data_date.config(text=str(card.get_release_year()) + "   ⬆️", bg='red')
                
            if card.get_name() == card_to_guess.get_name():
                exit() # TODO : Faire message victoire
        return

    Recherche(fenetre, all_cards_list, OnSearchInput)



if __name__ == "__main__":
    fenetre = Tk()
    fenetre.title("RoyaleDLE - Classic")
    fenetre.geometry("1525x800")
    fenetre.iconbitmap("assets/logo.ico")
    
    main(fenetre)

    fenetre.mainloop()