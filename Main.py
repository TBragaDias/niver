from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import vlc
import pygame
from time import sleep
import PIL as p
import PIL.ImageTk as ptk

app = Tk()
app.title("Felipe Surpresa")
app.geometry("1920x1080")

varBarra = DoubleVar()

pb = ttk.Progressbar(app, variable=varBarra, maximum=100)
pb.place(
    x = 550, y = 500, width= 800, height= 50
)


def step(tempo):

    midia = vlc.MediaPlayer("C:\\Users\\Tiago Braga\\Desktop\\Aulas\\Video\\IMG_4809.MOV")
    pygame.init()
    pygame.mixer.init()
    file = "C:\\Users\\Tiago Braga\\Desktop\\Aulas\\Video\\abraba.mp3"
    cont = 0
    etapas = tempo/100
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)
    while cont < etapas:
        cont  = cont + 1
        i = 0
        while i < 10000000:
                i = i + 1
        label2.config(text='{}%'.format(cont))
        varBarra.set(cont)
        app.update()
    midia.play()
    pygame.mixer.music.stop()


    
btn = Button(app, text="CLIQUE AQUI", command=lambda:step(10000), font=5)
btn.place(
     x = 850, y = 650, width= 200, height= 50
)


# Label Titulo
label1 = Label(app, text='TA PREPARADO FELIPÃO?', font=tkFont.Font(size=20))
label1.place(
    x = 750, y = 250, width= 400, height= 50
)

# Label de Carregamento da Barra
label2 = Label(app, text='', font=tkFont.Font(size=15))
label2.place(
    x = 1400, y = 515, width= 50, height= 20
)

# Label De PNG - Festa
imagem = p.Image.open("C:\\Users\\Tiago Braga\\Desktop\\Aulas\\Video\\festa.png")
pic = ptk.PhotoImage(imagem)

label3 = Label(app, image=pic)
label3.place(
    x = 50, y = 250, width= 450, height= 600
)

app.mainloop()