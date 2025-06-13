name = input("What's your name? ")
color = input("what's your favorite color? ")
with open('example.txt', 'w') as file:
    file.write(f"{name} created this file ")
    file.write(f"My favorite color is {color}")