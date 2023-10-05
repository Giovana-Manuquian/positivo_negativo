from os import system

system ('cls')

number = int(input("Digite um número: "))

if (number != 0):
    if (number < 0):
        print(f"This number {number} is negative")
    else:
        print(f"This number {number} is positive ")
else: 
    print(f"This number {number} is neutral.")
