# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N ").upper()
extra_cheese = input("Do you want extra cheese? Y or N ").upper()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
precio = 0
#Tamaño de pizza
if size == 'S':
  precio += 15
elif size == 'M':
  precio += 20
elif size == 'L':
  precio += 25

#Se le agrega peperoni
if add_pepperoni == 'Y':
  if size == 'S':
    precio += 2
  else:
    precio += 3

#Se le agrega queso
if extra_cheese == 'Y':
    precio += 1
print(f'your final bill is: ${precio}')




