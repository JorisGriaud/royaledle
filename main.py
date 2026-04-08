from accueil import Accueil

from tkinter import *
import pygame # pip install pygame
import random

pygame.mixer.init() # initialise the pygame

musics = ["01 - Kpoint - Ma 6t a craqué (feat. Ninho).flac", "02 - Kendji Girac - Me Quemo.flac", 
          "BassPoutine.mp3", "Sois pauvre et tais toi !.mp3", "Vas-y José.mp3", 
          "Y A Pas D'Amour.mp3", "03 - Black M - Spectateur.flac", "09 - Black M - La légende Black (feat. Dr. Beriz).flac",
          "13 - Black M - Je ne dirai rien (feat. The Shin Sekaï & Doomams).flac", "01 - Black M - Je suis chez moi.flac", 
          "PP haine - Les Sales Majestés -.mp3", "01 - Soldat Louis - Du rhum, des femmes.flac", 
          "03 - Calogero - Face à la mer.flac", "01 - AleFra - Dream in Motion.flac", 
          "03 - Francis Cabrel - Les murs de poussière (Remastered).flac", "02 - Bramsito - Sale mood(Explicit).flac",
          "04 - Kaaris - Gun salute(Explicit).flac", "05 - Niska - Medellín(Explicit).flac", 
          "01 - Tomawok - Angers City.flac"]
    
def play_intro():
    pygame.mixer.music.load("assets/sound/Clash_Royale_Intro_Sound_Effect.mp3")
    pygame.mixer.music.play(loops=0)
    fenetre.after(5500, play_song)

def play_song():
    pygame.mixer.music.load(f"assets/music/{random.choice(musics)}")
    pygame.mixer.music.play(fade_ms=5, loops=-1)

fenetre = Tk() 
fenetre.title("RoyaleDLE")
fenetre.geometry("1525x800") 
fenetre.iconbitmap("assets/logo.ico")

Accueil(fenetre)

play_intro()

fenetre.mainloop()