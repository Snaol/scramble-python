'''from tkinter import *
from tkinter import messagebox
from random import choice
from random import shuffle
import time
import pygame

#Create tkinter
Scramble = Tk()
Scramble.title("Scrambled Words")
Scramble.geometry("1200x600")
Scramble.state('zoomed')
"""#Scramble.rowconfigure(0,weight=1)
#Scramble.columnconfigure(0,weight=1)"""

pygame.mixer.init()

#Make the frame for the Home Screen, In-Game, and Post-Game Score
Home_frame = Frame(Scramble) 
Home_frame.pack(pady=20)
Game_frame = Frame(Scramble)
Game_frame.pack(pady=20)
Score_frame = Frame(Scramble)
Score_frame.pack(pady=20)

#Background Photo
Background_Photo = PhotoImage(file="(Spring) Lake Bled.jpg")

#Display Background Photo
Background_label=Label(Home_frame,image=Background_Photo)
Background_label.place(x=0,y=0,relwidth=1,relheight=1)

#List of font colors
list_colors=['medium blue','turquoise1','DeepPink2','SeaGreen1','DarkOrchid1','orange red','deep pink']

#Pick a randon color from list_colors
color1 = choice(list_colors) #For the title
color2 = choice(list_colors) #For the shuffled word

#Label SCRAMBLE 
Game_Title= Label(Home_frame,text="SCRAMBLED WORDS",font=('Vladimir Script', 69,'bold'),fg=color1,bg='gray17')
Game_Title.pack(pady=20)
'''