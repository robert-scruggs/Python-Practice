from tkinter import *

window = Tk()
window.geometry("750x750")
window.title("Python Type Beat")
window.config(bg="black")


screen_width = window.winfo_width() / 2
screen_height = window.winfo_height() / 2

def sayHello():
    print("say hello")

def sayBye():
    print("say bye")    


frame = Frame(window, bg="skyblue3", width=500, height=250)
frame.place(relx=0.5,rely=0.5, anchor=CENTER)

button1 = Button(frame, width=25, height=25, text="Button 1", command=sayBye)
button1.grid(row=0, column=0, padx=10, pady=10)

button2 = Button(frame, width=25, height=25, text="Button 2", command=sayHello)
button2.grid(row=0, column=1, padx=10, pady=10)





window.mainloop()
