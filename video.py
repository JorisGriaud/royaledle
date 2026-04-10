from tkinter import *
import imageio # pip install imageio imageio[ffmpeg] imageio[pyav]
from PIL import Image, ImageTk
import pygame

pygame.mixer.init() # initialise the pygame

class Video():
    def stream(self):
        try:
            self.image = self.video.get_next_data()
            self.frame_image = Image.fromarray(self.image)
            self.frame_image=ImageTk.PhotoImage(self.frame_image)
            self.l1.config(image=self.frame_image)
            self.l1.image = self.frame_image
            self.l1.after(self.delay, lambda: self.stream())
        except:
            self.video.close()
            self.root.destroy()
            return
    
    def tk(self, parent=None):
        if parent is None:
            self.root = Tk()
            needs_mainloop = True
        else:
            self.root = Toplevel(parent)
            needs_mainloop = False
        
        self.root.title('TK PRIME !!!')
        self.root.lift()
        self.root.focus()
        
        self.l1 = Label(self.root, bg="black")
        self.l1.pack(fill=BOTH, expand=True)
        
        self.root.update()
        
        try:
            self.video_name = "assets/easter_eggs/OMG_THEKAIRI78_DEFONCE_UNE_PORTE_ET_DANSE_AVEC_UN_BALAIS.mp4"
            self.video = imageio.get_reader(self.video_name)
            self.delay = int(1000 / self.video.get_meta_data()['fps'])
            pygame.mixer.music.load("assets/music/OMG_THEKAIRI78_DEFONCE_UNE_PORTE_ET_DANSE_AVEC_UN_BALAIS.mp3")
            self.stream()
            self.root.after(2000, lambda: pygame.mixer.music.play(loops=0))
            if needs_mainloop:
                self.root.mainloop()
        except Exception as e:
            print(f"Erreur lors du chargement de la vidéo: {e}")
            self.root.destroy()
        
    def noe(self, parent=None):
        if parent is None:
            self.root = Tk()
            needs_mainloop = True
        else:
            self.root = Toplevel(parent)
            needs_mainloop = False
        
        self.root.title("J'AIME TRES BEAUCOUP LE TENNIS")
        self.root.lift()
        self.root.focus()
        
        self.l1 = Label(self.root, bg="black")
        self.l1.pack(fill=BOTH, expand=True)
        
        self.root.update()
        
        try:
            self.video_name = "assets/easter_eggs/Jaime_tres_beaucoup_le_tennis.mp4"
            self.video = imageio.get_reader(self.video_name)
            self.delay = int(1000 / self.video.get_meta_data()['fps'])
            pygame.mixer.music.load("assets/music/Jaime_tres_beaucoup_le_tennis.mp3")
            self.stream()
            self.root.after(1800, lambda: pygame.mixer.music.play(loops=0))
            if needs_mainloop:
                self.root.mainloop()
        except Exception as e:
            print(f"Erreur lors du chargement de la vidéo: {e}")
            self.root.destroy()

    def coudoux(self, parent=None):
        if parent is None:
            self.root = Tk()
            needs_mainloop = True
        else:
            self.root = Toplevel(parent)
            needs_mainloop = False
        
        self.root.title("JE ORDINATEUR")
        self.root.lift()
        self.root.focus()
        
        self.l1 = Label(self.root, bg="black")
        self.l1.pack(fill=BOTH, expand=True)
        
        self.root.update()
        
        try:
            self.video_name = "assets/easter_eggs/La_Coudanse_de_Coudoux.mp4"
            self.video = imageio.get_reader(self.video_name)
            self.delay = int(1000 / self.video.get_meta_data()['fps'])
            pygame.mixer.music.load("assets/music/La_Coudanse_de_Coudoux.mp3")
            self.stream()
            self.root.after(1800, lambda: pygame.mixer.music.play(loops=0))
            if needs_mainloop:
                self.root.mainloop()
        except Exception as e:
            print(f"Erreur lors du chargement de la vidéo: {e}")
            self.root.destroy()

if __name__ == "__main__":
    Video().coudoux()