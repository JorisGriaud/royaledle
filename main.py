from accueil import Accueil

from tkinter import *

fenetre = Tk() 
fenetre.title("RoyaleDLE")
fenetre.geometry("1525x800") 
fenetre.iconbitmap("assets/logo.ico")

Accueil(fenetre)

fenetre.mainloop()