from Cards import Cards
from random import randint
from tkinter import*
from recherche import Recherche
from PIL import Image, ImageTk
import pygame
cards = Cards()


def choixcarte():
   carte=randint(0,cards.get_number_of_cards()-1)
   return carte

def choixdescription(carte=choixcarte()):
   card= cards.get_card_by_id(carte)
   description=card.get_description()
   return description

def texteatroues():
    carte=choixcarte()
    b=str(cards.get_card_by_id(carte).get_name())
    description = choixdescription(carte)
    description=str(description)
    tab=description.split(sep=" ")
    t=[0 for _ in range(len(tab))]
    n=4
    check=[]
    for _ in range(n):
       a=randint(0,len(tab)-1)
       while str(t[a]).lower()==b or a in check:
           a=randint(0,len(tab)-1)
       check.append(a)
       t[a]=tab[a]
    for i in range (len(t)):
       if t[i]==0:
          t[i] = "_" * len(tab[i])
    t.append(carte)
    return t

def afficher_description(fenetre):
   description=texteatroues()
   description.pop(description.index(description[-1]))
   hauteur = fenetre.winfo_height()
   labels_frame = Frame(fenetre, bg="white")
   label_description = Label(labels_frame, relief="flat", borderwidth=0, text="Chaque essai révèle un autre mot", font=("arial",11))
   label_description.grid(row=0, column=0, pady=10)
   label_description = Label(labels_frame, relief="flat", borderwidth=0, text=description, font=("arial",8))
   label_description.place(x=0, y=40)
   labels_frame.place(x=0, y=hauteur//2, relwidth=1, height=hauteur//3)
   main(fenetre)
   




   

      
def main(fenetre):
   all_cards_list = cards.get_all_card_name_with_image_path()
   hauteur = fenetre.winfo_height()
   wrong_labels = []
   t=texteatroues()
   id=t[-1]
   carte=str(cards.get_card_by_id(id).get_name())
   print(f"DEBUG description: {carte}")
   description=str(choixdescription(id))
   tab=description.split(sep=" ")
   t.pop(t.index(t[-1]))
   labels_frame = Frame(fenetre, bg="white")
   label_description = Label(labels_frame, relief="flat", borderwidth=0, text="Chaque essai révèle un autre mot", font=("arial",11))
   label_description.grid(row=0, column=0, pady=10)
   label_description = Label(labels_frame, relief="flat", borderwidth=0, text=t, font=("arial",8))
   label_description.place(x=0,y=40)
   labels_frame.place(x=0, y=hauteur//2, relwidth=1, height=hauteur//3)
   canvas_container = Frame(labels_frame, bg="white")
   canvas_container.place(x=0, y=85, relwidth=1, height=hauteur//3)
   labels_frame.rowconfigure(1, weight=1)
   canvas = Canvas(canvas_container, bg="white", highlightthickness=0, height=100)
   canvas.pack(side=LEFT, fill=BOTH, expand=True)
   results_frame = Frame(canvas, bg="white")
   canvas_window = canvas.create_window((0, 0), window=results_frame, anchor="nw")
   results_frame.place(x=0, y=0, relwidth=1, height=hauteur//4)
   def on_results_frame_configure(event=None):
        canvas.configure(scrollregion=canvas.bbox("all"))
        canvas.itemconfig(canvas_window, width=canvas.winfo_width())
   compteur=[0]
    
   results_frame.bind("<Configure>", on_results_frame_configure)
   canvas.bind("<Configure>", on_results_frame_configure)
   

   def OnSearchInput(valeur):
        card = cards.get_card_by_name(valeur)
        if card: 
         data_carte = Label(results_frame, relief="flat", borderwidth=0, image=None, font=12)  
         img = Image.open(card.get_icon_path()).resize((42, 52), Image.Resampling.LANCZOS)
         image = ImageTk.PhotoImage(img) 
         data_carte.image = image
         if valeur!=carte:
            mot=randint(0,len(t)-1)
            while tab[mot] == t[mot]:
               mot=randint(0,len(t)-1)
            t[mot]=tab[mot]
            label_description.config(text=t)  
            data_carte.config(image=image, bg='red') 
            wrong_labels.append(data_carte)
         else:
             data_carte.config(image=image, bg='#42F31F')
             wrong_labels.append(data_carte)
             label_description.config(text=tab)
             img_bouton = Image.open("assets/victoiredescr.png").resize((250, 270))
             photo_bouton = ImageTk.PhotoImage(img_bouton)
             bouton = Button(fenetre, image=photo_bouton, relief="flat", borderwidth=0,command=lambda:[fenetre.after(0, bouton.destroy()),recommencer()])
             bouton.image = photo_bouton
             bouton.place(x=555, y=50)
             bouton.lift()
         row = compteur[0] % 3
         column = compteur[0] // 3
         data_carte.grid(row=row, column=column, pady=1, padx=15)
         compteur[0]+= 1 

            
   def recommencer():
        all_cards_list = cards.get_all_card_name_with_image_path()
        nonlocal wrong_labels
        for label in wrong_labels:
            label.destroy()
        wrong_labels = []
        card=choixcarte()        
        afficher_description(fenetre)


     
   Recherche(fenetre, all_cards_list, callback=OnSearchInput)

    

if __name__ == "__main__":
    fenetre = Tk()
    fenetre.title("RoyaleDLE - Description")
    fenetre.geometry("1525x800")
    fenetre.iconbitmap("assets/logo.ico")
    pygame.mixer.init() 
    
    main(fenetre)
    fenetre.mainloop()



         
      



       

      

        
    


 
 
   