import random

random_number = random.randint(1,100)

while True:
    a = int(input("Please enter a number:"))

    if (a < random_number):
        print("Enter higher number:")
    elif (a > random_number):
        print("Enter lower number:")
    else:
        print("You find the number")
        break


