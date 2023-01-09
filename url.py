import tkinter
import mysql.connector
from tkinter import *


foodDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mangomelon@5",
    database="practice2"
)

foodCursor = foodDB.cursor()

def addToDatabase():
    sql1 = "INSERT INTO food (name,color) VALUES(%s,%s)"
    val1 = [
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633')
    ]
    foodCursor.executemany(sql1,val1)
    foodDB.commit()


def delete():
    sql = "DELETE FROM food"
    foodCursor.execute(sql)
    foodDB.commit()







window = Tk()
window.geometry("500x500")
window.title("Database Practice Oh Yeah!")
window.config(bg="purple")

button = Button(window, text="Add", command=addToDatabase)
button.pack(padx=10, pady=10)

button = Button(window, text="Delete", command=delete)
button.pack(padx=10, pady=10)



window.mainloop()




