from tkinter import *
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


#Background Photo
Background_Photo = PhotoImage(file="background.png")

#Display Background Photo
Background_label=Label(Scramble,image=Background_Photo)
Background_label.place(x=0,y=0,relwidth=1,relheight=1)

#List of font colors
list_colors=['medium blue','turquoise1','DeepPink2','SeaGreen1','DarkOrchid1','orange red','deep pink']

#Pick a randon color from list_colors
color1 = choice(list_colors) #For the title
color2 = choice(list_colors) #For the shuffled word

#Label SCRAMBLE
Game_Title= Label(Scramble,text="SCRAMBLED WORDS",font=('Vladimir Script', 69,'bold'),fg=color1,bg='gray17')
Game_Title.pack(pady=20)

#Display The shuffled Word
my_label = Label(Scramble,text="",font=("Helvetica", 50),fg=color2,bg='gray17')
my_label.pack(pady=20)

#Make the frame for the game
Game_frame = Frame(Scramble)
Game_frame.pack(pady=20)

#variables
seconds=60 #amount for second for the timer
correct=0 #(counter)amount for correct answers

#List of songs
Music_list=["relaxing jazz music for study (about 30 min) - Music365.mp3","[No Copyright Music] Lo-Fi Chill Hip-Hop Free Download - FuzzySheep Beats.mp3","[No Copyright Music] Chill Lo-fi Hip-Hop Beats FREE (Copyright Free) Lofi Hip Hop Chillhop Music Mix - Chill Out Records.mp3","20 Minute Timer with Classical, Calming, Relaxing Music! Soft, Gentle, Piano, Countdown Music Timer! - Mr. Timer.mp3"]

Song=choice(Music_list)

#Play the backgound music
def play():
    pygame.mixer.music.load(Song)
    pygame.mixer.music.play(loops=-1) #Infinite Loop

#Makes the timer work base on the amount of seconds in the 'seconds' variable up top
def timer():

    #splitting the minutes and seconds
    global seconds
    if seconds > 0:
        timer_display.config(fg='green2')
        seconds = seconds - 1
        mins = seconds // 60
        m = str(mins)

        if mins < 10:
            m = '0' + str(mins)
        se = seconds - (mins * 60)
        s = str(se)

        #Remind the user that they are running out of time by changing the font color to red
        if se <= 10 and mins ==0:
            timer_display.config(fg='red') 
            
        if se < 10:
            s = '0' + str(se)
        time.set(m + ':' + s)
        timer_display.config(textvariable=time)
        # call this function again in 1,000 milliseconds
        Scramble.after(1000, timer)
        
    #display the amount of points and destroys tkinter
    elif seconds == 0:
        messagebox.showinfo('GG','GAME OVER\npoints:'+ str(correct))
        Scramble.destroy()


#Selects a random word, shuffle the word and Display It
def shuffled():

    #Clear the user_answer box
    user_answer.delete(0,END)

    #Clear the answer_label
    answer_label.config(text='')

    #List of Level 1 words
    global theListOne
    theListOne= ["ability","able","about","above","accept","according","account","across","action","activity","adult","allow","analysis","answer","anything","appear","complicated","compatible","boring","efficient","scared","fear","science","math","intelligence","wisdom","knowledge","time","forgive","give","nothing","return","discombobulated","disorganized","organized","freedom","sustain","surround","sublime","submissive","open","doubt","queen","king","Mr. Knight","marry","dove","air","because","forever","comedic","stress","confident","true","honest","continue","continuous","friends","benifits","comfort","uncomfortable","eat","meat","big","small","fire","hot","home","cold","water","freeze","somewhere","dream","hope","memories","explicit","sexual","special","sauce","marinate","zoomed","insane","contain","emotion","running","out","picture","imagine","song","may","realize","book","journey","break","cry","smirk","smile","overjoyed","speaker","right","left","North","South","East","West","all","me","pray","God","charge"]
    
    #Pick a random word from theListOne
    global word
    word = choice(theListOne)

    #Break apart the random word chosen word
    break_apart= list(word)
    shuffle(break_apart)

    # Turn shuffle list into a word
    global shuffled_word
    shuffled_word=''
    for letter in break_apart:
        shuffled_word +=letter

    #Display the shuffled word to the screen
    my_label.config(text=shuffled_word)

#Check if the user's answer is "Correct" or "Incorrect"
def answer():
    if word== user_answer.get():
        answer_label.config(text="Correct",fg='green2')
        
        #Clear the shuffled word on the screen(To prevent cheating)
        my_label.config(text="")
        #Clear the user_answer box (To prevent cheating)
        user_answer.delete(0,END)
        
        global correct
        correct +=1
    else:
        answer_label.config(text="Incorrect",fg='red')

#Entry for the user
user_answer= Entry(Scramble,font=("Comic Sans MS",25),fg='gold',bg='gray17')
user_answer.pack(pady=20)

#Button to switch to another word
my_button = Button(Game_frame,font=("Helvetica",17,"bold"),text="Change The Word",height = 1, width = 20,fg='#fff',bg='gray17',command=shuffled)
my_button.grid(row=0,column=0,padx=10)

#Button to check if answer is correct or not
answer_button = Button(Game_frame,font=("Helvetica",17,"bold"),text ="Submit",height = 1, width = 20,fg='#fff',bg='gray17',command=answer)
answer_button.grid(row=0,column=1,padx=10)

#Display "Correct" or "Incorrect"
answer_label= Label(Scramble,text="",font=("Arial",18),bg='gray17')
answer_label.pack(pady=20)

#Display the timer
time = StringVar()
timer_display = Label(Game_frame, font=('Trebuchet MS', 25, 'bold'),bg='gray17')
timer_display.grid(row=0,column=2,padx=15)

#start the program
play()
timer()
shuffled()
Scramble.mainloop()