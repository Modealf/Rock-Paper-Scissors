from random import random
from secrets import choice
from tkinter import messagebox
from tkinter import *


# Window Config

r = Tk()
r.title('Rock Paper Scissors')
r.geometry('350x270')


mylist = ["Rock", "Paper", "Scissors"]

# Random Outcomes


def Rock_choices():
    random = choice(mylist)
    if random == "Rock":
        rock = messagebox.showwarning("Tie", "Rock! Its a tie.")

    if random == "Paper":
        rock = messagebox.showerror("Lose", "Paper! You lose.")

    if random == "Scissors":
        rock = messagebox.showinfo("Win", "Scissors! You win")

def Paper_choices():
    random = choice(mylist)
    if random == "Rock":
        rock = messagebox.showinfo("Win", "Rock! You win")

    if random == "Paper":
        rock = messagebox.showwarning("Tie", "Paper! Its a tie")

    if random == "Scissors":
        rock = messagebox.showerror("Lose", "Scissors! You lose")

def Scissors_choices():
    random = choice(mylist)
    if random == "Rock":
        rock = messagebox.showerror("Lose", "Rock! You lost")

    if random == "Paper":
        rock = messagebox.showinfo("Win", "Paper! You win")

    if random == "Scissors":
        rock = messagebox.showwarning("Tie", "Scissors! Its a tie")

img = PhotoImage(file="Wooden Background.png")
label = Label(r ,image=img).place(x=-20,y=-20)

#Buttons

rock = Button(r, text="Rock", font=("Arial Rounded MT Bold", 14), width=20, command=Rock_choices, bg="light green").pack(pady=5)
paper = Button(r, text="Paper", font=("Arial Rounded MT Bold", 14), width=20, command=Paper_choices, bg="light green").pack(pady=5)
Scissor = Button(r, text="Scissors", font=("Arial Rounded MT Bold", 14), width=20, command=Scissors_choices, bg="light green").pack(pady=5)
Stop = Button(r, text="Stop Playing", font=("Bold", 14),width=25, command=r.destroy, bg="pink").pack(pady=30, padx=20)


r.mainloop()