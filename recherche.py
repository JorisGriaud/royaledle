from tkinter import *
from PIL import Image, ImageTk
import os
from Cards import Cards

class Recherche():
    def __init__(self, fenetre, cards_list, callback=None):
        self.fenetre = fenetre
        self.cards = cards_list
        self.callback = callback

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
        self.bouton = Button(self.fenetre, image=self.photo_bouton, relief="flat", borderwidth=0, command=self.on_enter)
        self.bouton.image = self.photo_bouton

        # Zone de texte
        self.entry = Entry(fenetre, font=('Roboto', 12), fg='gray')
        self.entry.insert(0, self.placeholder)
        self.entry.bind('<FocusIn>', self.on_focus_in)
        self.entry.bind('<FocusOut>', self.on_focus_out)
        self.entry.bind('<KeyRelease>', self.update_suggestions)

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

        # Placer les éléments de recherche au premier démarrage
        self.fenetre.after(100, self.place_research)
        
        self.listbox_visible = False

    def on_frame_configure(self, event):
        self.canvas2.configure(scrollregion=self.canvas2.bbox("all"))

    def on_canvas_configure(self, event):
        self.canvas2.itemconfig(self.canvas2_frame_id, width=event.width)
    
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
        largeur = self.fenetre.winfo_width()
        hauteur = self.fenetre.winfo_height()
        
        largeur_totale = self.largeur_entry + self.largeur_bouton
        x1 = (largeur - largeur_totale) // 2
        y1 = (hauteur - self.hauteur_bouton) // 2 - 80 + self.hauteur_bouton

        self.filtered_data = [item for item in self.cards if search_term in item["name"].lower()]

        if self.filtered_data:
            for item in self.filtered_data:
                self.create_suggestion_row(item)
            
            # Afficher le conteneur avec une hauteur fixe de 270px
            self.container.place(x=x1, y=y1, width=self.largeur_bouton + self.largeur_entry, height=270)
            self.container.lift()
            
            self.listbox_visible = True
        else:
            self.container.place_forget()
            self.listbox_visible = False

    def place_research(self, event=None):
        if not self.bouton:
            return
        largeur = self.fenetre.winfo_width()
        hauteur = self.fenetre.winfo_height()
        
        largeur_totale = self.largeur_entry + self.largeur_bouton
        x1 = (largeur - largeur_totale) // 2
        y1 = (hauteur - self.hauteur_bouton) // 2 - 80

        self.bouton.place(x=x1 + self.largeur_entry, y=y1, width=self.largeur_bouton, height=self.hauteur_bouton)
        self.bouton.lift()

        self.entry.place(x=x1, y=y1, width=self.largeur_entry, height=self.hauteur_bouton)
        self.entry.lift()

        self.entry.bind("<KeyPress>", self.on_key_press)

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

        # Clic
        def make_selection(event, name=item["name"]):
            self.on_select(name)

        row.bind("<Button-1>", make_selection)
        name_label.bind("<Button-1>", make_selection)
        img_widget.bind("<Button-1>", make_selection)

        # Hover
        row.bind("<Enter>", lambda e: row.config(bg="#f0f0f0"))
        row.bind("<Leave>", lambda e: row.config(bg="white"))

    def on_select(self, selected_item):
        self.entry.delete(0, END)
        self.entry.insert(0, selected_item)
        self.on_enter()
        self.entry.delete(0, END)
        self.container.place_forget()
        self.listbox_visible = False
        return selected_item

    def on_key_press(self, event):
        if not event:
            return
        self.event = event
        if self.event.keycode == 13: # keycode 13 : Touche entrer
            self.on_enter()
    
    def on_enter(self):
        if self.entry.get() == None:
            self.fenetre.focus()
            return
        elif self.entry.get() != None:
            self.input = self.entry.get()
            self.entry.delete(0, END)
            self.container.place_forget() # TODO: Vérifier si le nom de la carte existe
            for index_item in range(len(self.cards) - 1,):
                if self.cards[index_item]["name"] == self.input:
                    remove_item = self.cards.pop(index_item)
                    # print("Carte supprimé :", remove_item)
            # self.fenetre.focus()
            self.listbox_visible = False
            if self.callback:
                self.callback(self.input)
                return