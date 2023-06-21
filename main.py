import random 
import string
x =int(input("How many numbers do you want in the password:"))
z =int(input("How many letters do you want in the password:"))
w =int(input("How many symbols do you want in the password:"))
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
a = ""
alphabet = list(string.ascii_lowercase)
for number in range(x):
  a = a + str(random.randint(0,9))
for letter in range(z):
  y = random.randint(0,25)
  index = alphabet[y]
  a = a + index
for symbol in range(w):
  b = random.randint(0,9)
  symbol_index = symbols[b]
  a = a + symbol_index
  

print(a)