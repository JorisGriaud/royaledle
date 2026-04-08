from Cards import Cards
from recherche import Recherche

from tkinter import *
from random import randint, choice
from PIL import Image, ImageTk # pip install pillow
import pygame

cards = Cards()
musics = ["01 - Kpoint - Ma 6t a craqué (feat. Ninho).flac", "02 - Kendji Girac - Me Quemo.flac", 
          "BassPoutine.mp3", "Sois pauvre et tais toi !.mp3", "Vas-y José.mp3", 
          "Y A Pas D'Amour.mp3", "03 - Black M - Spectateur.flac", "09 - Black M - La légende Black (feat. Dr. Beriz).flac",
          "13 - Black M - Je ne dirai rien (feat. The Shin Sekaï & Doomams).flac", "01 - Black M - Je suis chez moi.flac", 
          "PP haine - Les Sales Majestés -.mp3", "01 - Soldat Louis - Du rhum, des femmes.flac", 
          "03 - Calogero - Face à la mer.flac", "01 - AleFra - Dream in Motion.flac", 
          "03 - Francis Cabrel - Les murs de poussière (Remastered).flac", "02 - Bramsito - Sale mood(Explicit).flac",
          "04 - Kaaris - Gun salute(Explicit).flac", "05 - Niska - Medellín(Explicit).flac", 
          "01 - Tomawok - Angers City.flac"]

def GetRandomCard():
    nbre_cards = cards.get_number_of_cards()
    nbre_aleatoire = randint(0, nbre_cards)
    card = cards.get_card_by_id(nbre_aleatoire)
    # card = cards.get_card_by_name("Gel") # Debug
    print(card.get_name()) # Debug
    return card

def main(fenetre):
    all_cards_list = cards.get_all_card_name_with_image_path()
    card_to_guess = GetRandomCard()

    hauteur = fenetre.winfo_height()
    largeur = fenetre.winfo_width()

    # Frame pour tout les labels 
    labels_frame = Frame(fenetre, bg="white")
    labels_frame.place(x=0, y=hauteur//2, relwidth=1, height=hauteur//3)
    
    # Label Header
    label_carte = Label(labels_frame, relief="flat", borderwidth=0, text='Carte', font=16)
    label_elixir = Label(labels_frame, relief="flat", borderwidth=0, text="Coût d'élixir", font=16)
    label_rarete = Label(labels_frame, relief="flat", borderwidth=0, text="Rareté", font=16)
    label_type = Label(labels_frame, relief="flat", borderwidth=0, text="Type", font=16)
    label_cible = Label(labels_frame, relief="flat", borderwidth=0, text="Cible", font=16)
    label_portee = Label(labels_frame, relief="flat", borderwidth=0, text="Portée/Radius", font=16)
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
    
    label_carte.grid(row=0, column=0, pady=10, padx=15)
    label_elixir.grid(row=0, column=1, pady=10, padx=15)
    label_rarete.grid(row=0, column=2, pady=10, padx=15)
    label_type.grid(row=0, column=3, pady=10, padx=15)
    label_cible.grid(row=0, column=4, pady=10, padx=15)
    label_portee.grid(row=0, column=5, pady=10, padx=15)
    label_vitesse_attaque.grid(row=0, column=6, pady=10, padx=15)
    label_vitesse.grid(row=0, column=7, pady=10, padx=15)
    label_date.grid(row=0, column=8, pady=10, padx=15)

    # Canvas avec scrollbar pour afficher les résultats
    canvas_container = Frame(labels_frame, bg="white")
    canvas_container.grid(row=1, column=0, columnspan=9, sticky="nsew", padx=5, pady=5)
    labels_frame.rowconfigure(1, weight=1)
    
    canvas = Canvas(canvas_container, bg="white", highlightthickness=0, height=100)
    scrollbar = Scrollbar(canvas_container, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    # Frame pour les résultats à l'intérieur du canvas
    results_frame = Frame(canvas, bg="white")
    canvas_window = canvas.create_window((0, 0), window=results_frame, anchor="nw")
    
    # Configurer les colonnes du results_frame
    for i in range(9):
        results_frame.columnconfigure(i, weight=1)
    
    # Compteur de ligne pour les résultats
    current_row = [0]
    
    def on_results_frame_configure(event=None):
        canvas.configure(scrollregion=canvas.bbox("all"))
        # Redimensionner le frame à la largeur du canvas
        canvas.itemconfig(canvas_window, width=canvas.winfo_width())
    
    results_frame.bind("<Configure>", on_results_frame_configure)
    canvas.bind("<Configure>", on_results_frame_configure)

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
            # Créer une nouvelle ligne de résultats
            row = current_row[0]
            
            # Créer les labels pour cette ligne
            data_carte = Label(results_frame, relief="flat", borderwidth=0, image=None, font=12)
            data_elixir = Label(results_frame, relief="flat", borderwidth=0, text="", font=12)
            data_rarete = Label(results_frame, relief="flat", borderwidth=0, text="", font=12)
            data_type = Label(results_frame, relief="flat", borderwidth=0, text="", font=12)
            data_cible = Label(results_frame, relief="flat", borderwidth=0, text="", font=12)
            data_portee = Label(results_frame, relief="flat", borderwidth=0, text="", font=12)
            data_vitesse_attaque = Label(results_frame, relief="flat", borderwidth=0, text="", font=12)
            data_vitesse = Label(results_frame, relief="flat", borderwidth=0, text="", font=12)
            data_date = Label(results_frame, relief="solid", borderwidth=0, text="", font=12)
            
            # Charger l'image
            img = Image.open(card.get_icon_path()).resize((42, 52), Image.Resampling.LANCZOS)
            image = ImageTk.PhotoImage(img)
            data_carte.image = image
            
            # Card image
            if card.get_name() == card_to_guess.get_name():
                data_carte.config(image=image, bg='#42F31F')
            else:
                data_carte.config(image=image, bg='red')

            # Elixir "⬆️ ⬇️"
            if card.get_elixir() == card_to_guess.get_elixir():
                data_elixir.config(text=str(card.get_elixir()), bg='#42F31F')
            elif card.get_elixir() > card_to_guess.get_elixir():
                data_elixir.config(text=str(card.get_elixir()) + "   ⬇️", bg="red")
            elif card.get_elixir() < card_to_guess.get_elixir():
                data_elixir.config(text=str(card.get_elixir()) + "   ⬆️", bg="red")

            # Rarity "⬆️ ⬇️"
            if card.get_rarity() == card_to_guess.get_rarity():
                data_rarete.config(text=card.get_rarity(), bg="#42F31F")
            elif rarity_dic[card.get_rarity()] > rarity_dic[card_to_guess.get_rarity()]:
                data_rarete.config(text=card.get_rarity() + " ⬇️", bg='red')
            elif rarity_dic[card.get_rarity()] < rarity_dic[card_to_guess.get_rarity()]:
                data_rarete.config(text=card.get_rarity() + " ⬆️", bg='red')

            if card.get_type() == card_to_guess.get_type():
                data_type.config(text=card.get_type(), bg="#42F31F")
            else:
                data_type.config(text=card.get_type(), bg='red')
            
            if card.get_targets() == card_to_guess.get_targets():
                data_cible.config(text=card.get_targets(), bg="#42F31F")
            else:
                data_cible.config(text=card.get_targets(), bg='red')
            
            # Range/Radius "⬆️ ⬇️" probleme avec Portée/Radius
            if card.get_range() == None and card_to_guess.get_range() == None:
                data_portee.config(text="S.O", bg="#42F31F")
            elif card.get_type() == "Sort":
                if card.get_radius() == card_to_guess.get_radius():
                    data_portee.config(text=card.get_radius(), bg="#42F31F")
                elif isinstance(card.get_radius(), float) and isinstance(card_to_guess.get_radius(), float):
                    if card.get_radius() > card_to_guess.get_radius():
                        data_portee.config(text=str(card.get_radius()) + "   ⬇️", bg="red")
                    elif card.get_radius() < card_to_guess.get_radius():
                        data_portee.config(text=str(card.get_radius()) + "   ⬆️", bg="red")
                elif isinstance(card_to_guess.get_range(), (float, int)) and (card.get_range() == None or isinstance(card.get_range(), str)):
                    data_portee.config(text="S.O   ⬆️", bg="red")
            elif card.get_type() == "Troupe" or card.get_type() == "Bâtiment":
                if card.get_range() == card_to_guess.get_range():
                    data_portee.config(text=card.get_range(), bg="#42F31F")
                elif isinstance(card.get_range(), (float, int)) and isinstance(card_to_guess.get_range(), (float, int)):        
                    if card.get_range() > card_to_guess.get_range():
                        data_portee.config(text=str(card.get_range()) + "   ⬇️", bg="red")
                    elif card.get_range() < card_to_guess.get_range():
                        data_portee.config(text=str(card.get_range()) + "   ⬆️", bg="red")
                elif isinstance(card.get_range(), (float, int)) and (card_to_guess.get_range() == None or isinstance(card_to_guess.get_range(), str)):
                    data_portee.config(text=str(card.get_range()) + "   ⬇️", bg="red")


            # Hit Speed "⬆️ ⬇️"
            if card.get_hit_speed() == None and card_to_guess.get_hit_speed() == None:
                data_vitesse_attaque.config(text="S.O", bg="#42F31F")
            elif card.get_hit_speed() == card_to_guess.get_hit_speed():
                data_vitesse_attaque.config(text=card.get_hit_speed(), bg="#42F31F")
            elif card.get_hit_speed() == None:
                data_vitesse_attaque.config(text="S.O   ⬇️" , bg="red")
            elif card_to_guess.get_hit_speed() == None:
                data_vitesse_attaque.config(text="S.O   ⬆️" , bg="red")
            elif card.get_hit_speed() > card_to_guess.get_hit_speed():
                data_vitesse_attaque.config(text=str(card.get_hit_speed()) + "s"  + "   ⬇️" , bg="red")
            elif card.get_hit_speed() < card_to_guess.get_hit_speed():
                data_vitesse_attaque.config(text=str(card.get_hit_speed()) + "s" + "   ⬆️", bg="red")

            # Speed "⬆️ ⬇️"
            if card.get_speed() == None and card_to_guess.get_speed() == None:
                data_vitesse.config(text="S.O", bg="#42F31F")
            elif card.get_speed() == card_to_guess.get_speed():
                data_vitesse.config(text=card.get_speed(), bg="#42F31F")
            elif card.get_speed() == None:
                data_vitesse.config(text="S.O   ⬇️", bg='red')
            elif card_to_guess.get_speed() == None:
                data_vitesse.config(text="S.O   ⬆️", bg='red')
            elif speed_dict[card.get_speed()] > speed_dict[card_to_guess.get_speed()]:
                data_vitesse.config(text=card.get_speed() + "   ⬇️", bg='red')
            elif speed_dict[card.get_speed()] < speed_dict[card_to_guess.get_speed()]:
                data_vitesse.config(text=card.get_speed() + "   ⬆️", bg='red')
            
            # Date "⬆️ ⬇️"
            if card.get_release_year() == card_to_guess.get_release_year():
                data_date.config(text=card.get_release_year(), bg="#42F31F")
            elif card.get_release_year() > card_to_guess.get_release_year():
                data_date.config(text=str(card.get_release_year()) + "   ⬇️", bg='red')
            elif card.get_release_year() < card_to_guess.get_release_year():
                data_date.config(text=str(card.get_release_year()) + "   ⬆️", bg='red')
            
            # Placer les labels dans la grille
            data_carte.grid(row=row, column=0, pady=10, padx=15)
            data_elixir.grid(row=row, column=1, pady=10, padx=15)
            data_rarete.grid(row=row, column=2, pady=10, padx=15)
            data_type.grid(row=row, column=3, pady=10, padx=15)
            data_cible.grid(row=row, column=4, pady=10, padx=15)
            data_portee.grid(row=row, column=5, pady=10, padx=15)
            data_vitesse_attaque.grid(row=row, column=6, pady=10, padx=15)
            data_vitesse.grid(row=row, column=7, pady=10, padx=15)
            data_date.grid(row=row, column=8, pady=10, padx=15)
            
            # Incrémenter le compteur
            current_row[0] += 1
            
            # Forcer la mise à jour de la scrollbar
            results_frame.update_idletasks()
            canvas.configure(scrollregion=canvas.bbox("all"))
            # Forcer la scrollbar à aller en bas pour voir la carte ajoutée
            canvas.yview_moveto(1.0)
                
            if card.get_name() == card_to_guess.get_name():
                pygame.mixer.music.load(f"assets/music/{choice(musics)}")
                pygame.mixer.music.play(loops=-1)
                
                img_recommencer = Image.open("assets/Bienjoué.png").resize((500, 350))
                photo_bouton_recommencer = ImageTk.PhotoImage(img_recommencer)
                bouton_recommencer = Button(fenetre, image=photo_bouton_recommencer, relief="flat", borderwidth=0, command=lambda:[fenetre.after(0, bouton_recommencer.destroy()), recommencer()])
                bouton_recommencer.image = photo_bouton_recommencer
                bouton_recommencer.place(x=500, y=150, width=500, height=350)
                bouton_recommencer.lift()

        return

    def recommencer():
        for widget in results_frame.winfo_children():
            widget.destroy()
        main(fenetre)

    Recherche(fenetre, all_cards_list, OnSearchInput)



if __name__ == "__main__":
    fenetre = Tk()
    fenetre.title("RoyaleDLE - Classic")
    fenetre.geometry("1525x800")
    fenetre.iconbitmap("assets/logo.ico")
    
    main(fenetre)

    fenetre.mainloop()