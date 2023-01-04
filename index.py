import random

randomNumber = random.randint(2,5)
player = int(input("Whats the number? "))


while player != randomNumber:
    print("Wrong!")
    player = int(input("Whats the number? "))




print("All finished thanks for playing!")