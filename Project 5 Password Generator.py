import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

x = 0
y = 0
z = 0
random.shuffle(letters)
random.shuffle(numbers)
random.shuffle(symbols)

password = []

for n in range(0, nr_letters): 
    #x = print(letters[n], end="") #keeps the loop in one line
    password.append(random.choice(letters)) #adds a character to the list

for m in range(0, nr_symbols):
    #y = print(symbols[m], end="")
     password.append(random.choice(symbols)) #adds the characters to the password list
for l in range(0, nr_numbers):
    #z = print(numbers[l], end="")
     password.append(random.choice(numbers))

random.shuffle(password)
result = ''.join(password) #joins the list together with no brackets and spaces

print(result)

    


