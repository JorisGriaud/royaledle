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
    
    def tk(self):
        self.root = Tk()
        self.root.title('TK PRIME !!!')
        self.f1=Frame()
        self.l1 = Label(self.f1)
        self.l1.pack()
        self.f1.pack()
        self.video_name = "assets/easter_eggs/OMG_THEKAIRI78_DEFONCE_UNE_PORTE_ET_DANSE_AVEC_UN_BALAIS.mp4"   #Image-path
        self.video = imageio.get_reader(self.video_name)
        self.delay = int(1000 / self.video.get_meta_data()['fps'])
        pygame.mixer.music.load("assets/music/OMG_THEKAIRI78_DEFONCE_UNE_PORTE_ET_DANSE_AVEC_UN_BALAIS.mp3")
        self.stream()
        pygame.mixer.music.play(fade_ms=2000, loops=0)
        self.root.mainloop()

Video().tk()