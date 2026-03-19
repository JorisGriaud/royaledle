from tkinter import *
from PIL import Image, ImageTk
import os
from Cards import Cards

class Recherche():
    def __init__(self, fenetre, cards_list):
        self.fenetre = fenetre
        self.cards = cards_list

        # Dimension bouton et image
        self.largeur_bouton = 30
        self.hauteur_bouton = 30

        # Dimension de la zone de saisie de texte
        self.largeur_entry = 210

        # Texte placeholder zone de recherche
        self.placeholder = "Rechercher une carte ..."

        # Dimension de l'image de la carte
        self.largeur_carte = 35 # 35
        self.hauteur_carte = 45 # 45

        # Bouton envoyer
        self.image_bouton = Image.open("assets/bouton_entrer.png").resize((self.largeur_bouton, self.hauteur_bouton))  # Redimensionner à la taille du bouton
        self.photo_bouton = ImageTk.PhotoImage(self.image_bouton)
        self.bouton = Button(self.fenetre, image=self.photo_bouton, relief="flat", borderwidth=0, command=self.enter_button)
        self.bouton.image = self.photo_bouton

        # Zone de texte
        self.entry = Entry(fenetre, font=('Roboto', 12), fg='gray')
        self.entry.insert(0, self.placeholder)
        self.entry.bind('<FocusIn>', self.on_focus_in)
        self.entry.bind('<FocusOut>', self.on_focus_out)
        self.entry.bind('<KeyRelease>', self.update_suggestions)

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

        # Canvas zone de recherche
        self.canvas1 = Canvas(self.fenetre, highlightthickness=0)
        self.canvas1.pack(fill=BOTH, expand=True)
        self.canvas1.bind("<Configure>", self.place_research)
        
        # Conteneur des suggestions
        self.container = Frame(fenetre, bg="white", highlightbackground="grey", highlightthickness=1)

        # Canvas suggestions
        self.canvas2 = Canvas(self.container, bg="white", highlightthickness=0)
        
        # Scrollbar
        self.scrollbar = Scrollbar(self.container, orient="vertical", command=self.canvas2.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        
        self.canvas2.pack(side=LEFT, fill=BOTH, expand=True)
        self.canvas2.configure(yscrollcommand=self.scrollbar.set)
        
        # Cadre de suggestion
        self.suggestion_frame = Frame(self.canvas2, bg="white")
        
        # Fenêtre du canvas
        self.canvas2_frame_id = self.canvas2.create_window((0, 0), window=self.suggestion_frame, anchor="nw")
        
        # Liaison du redimensionnement
        self.suggestion_frame.bind("<Configure>", self.on_frame_configure) # Met à jour la zone de défilement du canvas

        self.canvas2.bind("<Configure>", self.on_canvas_configure) # Force le frame intérieur à prendre toute la largeur du canvas

        self.listbox_visible = False

    def on_frame_configure(self, event):
        self.canvas2.configure(scrollregion=self.canvas2.bbox("all"))

    def on_canvas_configure(self, event):
        self.canvas2.itemconfig(self.canvas2_frame_id, width=event.width)

    def enter_button(self):
        pass
    
    def on_focus_in(self, event):
        if self.entry.get() == self.placeholder:
            self.entry.delete(0, END)
            self.entry.config(fg='black', font=('Roboto', 14))

    def on_focus_out(self, get):
        if self.entry.get() == "":
            self.entry.insert(0, self.placeholder)
            self.entry.config(fg='gray', font=('Roboto', 12))

    def update_suggestions(self, event):
        search_term = self.entry.get().lower().strip()

        # Nettoyer les anciennes suggestions
        for widget in self.suggestion_frame.winfo_children():
            widget.destroy()
        
        # Ne pas afficher si le champ est vide ou contient le placeholder
        if len(search_term) == 0 or self.entry.get() == self.placeholder:
            self.container.place_forget()
            self.listbox_visible = False
            return

        # Récupérer les dimensions
        largeur = self.canvas1.winfo_width()
        hauteur = self.canvas1.winfo_height()
        
        largeur_totale = self.largeur_entry + self.largeur_bouton
        x1 = (largeur - largeur_totale) // 2
        y1 = (hauteur - self.hauteur_bouton) // 2 - 100 + self.hauteur_bouton

        filtered_data = [item for item in self.cards if search_term in item["name"].lower()]
        
        if filtered_data:
            for item in filtered_data:
                self.create_suggestion_row(item)
            
            # Afficher le conteneur avec une hauteur fixe de 270px
            self.container.place(x=x1, y=y1, width=self.largeur_bouton + self.largeur_entry, height=270)
            self.container.lift()
            
            self.listbox_visible = True
        else:
            self.container.place_forget()
            self.listbox_visible = False

    def place_research(self, event=None):
        if event:
            largeur = event.width
            hauteur = event.height
        else:
            self.canvas1.update() # Force la mise à jour pour avoir les bonnes dimensions
            largeur = self.canvas1.winfo_width()
            hauteur = self.canvas1.winfo_height()
        
        largeur_totale = self.largeur_entry + self.largeur_bouton
        x1 = (largeur - largeur_totale) // 2
        y1 = (hauteur - self.hauteur_bouton) // 2 - 100

        self.bouton.place(x=x1 + self.largeur_entry, y=y1, width=self.largeur_bouton, height=self.hauteur_bouton)
        self.bouton.lift()

        self.entry.place(x=x1, y=y1, width=self.largeur_entry, height=self.hauteur_bouton)
        self.entry.lift()

    def create_suggestion_row(self, item):
        row = Frame(self.suggestion_frame, bg="white", cursor="hand2")
        row.pack(fill=X, padx=2, pady=2)

        img_widget = None
        if os.path.exists(item["path"]):
            try:
                img = Image.open(item["path"]).resize((self.largeur_carte, self.hauteur_carte), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                img_widget = Label(row, image=photo, bg="white")
                img_widget.image = photo 
                img_widget.pack(side=LEFT, padx=5)
            except:
                img_widget = Label(row, text="[?]", bg="white", width=4)
                img_widget.pack(side=LEFT, padx=5)
        else:
            img_widget = Label(row, text="[?]", bg="white", width=4)
            img_widget.pack(side=LEFT, padx=5)

        name_label = Label(row, text=item["name"], font=('Roboto', 11), bg="white")
        name_label.pack(side=LEFT, pady=5)



fenetre = Tk()
fenetre.title("RoyaleDLE - Test")
fenetre.geometry("1525x800") 
fenetre.iconbitmap("assets/logo.ico")

cards = Cards().get_all_card_name_with_image_path()

Recherche(fenetre, cards)

fenetre.mainloop()
