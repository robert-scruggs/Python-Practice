from cgitb import text
import tkinter as tk
import requests as r
from bs4 import BeautifulSoup


url = "https://www.Wizard101.com"
result = r.get(url)
trans = BeautifulSoup(result.text, "html.parser")
pretty = trans.prettify()
# window
window = tk.Tk()
window.title("Practice With Tkinter")
window.geometry("750x750")
window.configure(bg='#66545e')
#frame

frame1 = tk.Frame(window, width=100, height=100, bg='#a39193').place(relx=.5, rely=.5,anchor=tk.CENTER)
messageLabel = tk.Label(window, text=pretty)
messageLabel.pack(padx=30,pady=30);
















window.mainloop()