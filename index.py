
from tkinter import *
from turtle import bgcolor

def submit():
    username = entry.get()
    print("Hello " + username)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get()) - 1, END)

window = Tk()
window.geometry("300x250")
window.title("Python Type Beat")
window.config(bg="black")

entry = Entry(window,
            font=("Arial", 50),
            fg="orange",
            bg="black")
entry.insert(0, "SpongeBob")
entry.pack(side=LEFT)

submit_Button = Button(window, text="submit", command=submit)
submit_Button.pack(side=RIGHT)

delete_Button = Button(window, text="Delete", command=delete)
delete_Button.pack(side=RIGHT)

backspace_Button = Button(window, text="Backspace", command=backspace)
backspace_Button.pack(side=RIGHT)

window.mainloop()