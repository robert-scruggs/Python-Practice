import tkinter as tk

# window
window = tk.Tk()
window.title("Practice With Tkinter")
window.geometry("500x500")
window.configure(bg='lightgray')

#frame
main_frame = tk.Frame(window, width=200, height=400)
main_frame.grid(row=0, column=0, padx=10, pady=5)

second_frame = tk.Frame(window, width=300, height=300, bg="purple")
second_frame.grid(row=0, column=1, padx=0, pady=0)
second_frame.pack_propagate(False)

#label
tk.Label(main_frame, text="Fat Bitches").grid(row=0,column=0)



button = tk.Button(second_frame, text="Click me!", width=20)
button.grid(row=1, column=0, padx=10, pady=5)

button2 = tk.Button(second_frame, text="Click me 2!", width=20)
button2.grid(row=2, column=0, padx=10, pady=5)




window.mainloop()