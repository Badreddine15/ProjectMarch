import sys
import os
from tkinter import *

window=Tk()

window.title("Running Python Script")
window.geometry('720x1920')


def runsnake():
    os.system('snake.exe')
def rundemineur():
    os.system('demineur.exe')
def runpong():
    os.system('pong.exe')

snake_img = PhotoImage(file='snake.png')
demineur_img = PhotoImage(file='demineur.png')
pong = PhotoImage(file='téléchargement.png')

button1 = Button(window, image=snake_img, command=runsnake,borderwidth =10)
button1.pack(pady= 20)
button2 = Button(window, image=demineur_img, command=rundemineur ,borderwidth =10)
button2.pack(pady= 20)
button3 = Button(window, image=pong, command=runpong,borderwidth =10)
button3.pack(pady= 20)
window.mainloop()