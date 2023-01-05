from cgitb import text
import tkinter as tk

def showMessage():
    messageLabel = tk.Label(window, text="word")
    messageLabel.pack(padx=30,pady=30);


# window
window = tk.Tk()
window.title("Practice With Tkinter")
window.geometry("500x500")
window.configure(bg='#66545e')
#frame

frame1 = tk.Frame(window, width=100, height=100, bg='#a39193').place(relx=.5, rely=.5,anchor=tk.CENTER)











window.mainloop()