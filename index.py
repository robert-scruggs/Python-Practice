from cgitb import text
import tkinter as tk

def showMessage():
    print(textbox.get("1.0", tk.END))
    textbox.delete("1.0",tk.END)


# window
window = tk.Tk()
window.title("Practice With Tkinter")
window.geometry("500x500")
window.configure(bg='darkgray')

#frame

label = tk.Label(window, text="Good Morning", font=('Arial', 18))
label.pack(padx=20,pady=20)

textbox = tk.Text(window, height=3, font=('Arial', 16))
textbox.pack(padx = 10, pady=10)

button = tk.Button(window, text="Click on me!", font=('Arial', 18))
button.pack(padx=10, pady=10)

mainFrame = tk.Frame(window, width=300,height=300, bg="Black")
mainFrame.pack(padx=10, pady=10)

button1 = tk.Button(mainFrame, text="Button1", command=showMessage)
button1.grid(row=0, column=0, padx=5, pady=5)

button2 = tk.Button(mainFrame, text="Button2")
button2.grid(row=0, column=1, padx=5, pady=5)

button3 = tk.Button(mainFrame, text="Button3")
button3.grid(row=0, column=2, padx=5, pady=5)

button4 = tk.Button(mainFrame, text="Button4")
button4.grid(row=1, column=0, padx=5, pady=5)

button5 = tk.Button(mainFrame, text="Button5")
button5.grid(row=1, column=1, padx=5, pady=5)

button6 = tk.Button(mainFrame, text="Button6")
button6.grid(row=1, column=2, padx=5, pady=5)











window.mainloop()