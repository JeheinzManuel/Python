# π¨ Don't change the code below π
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N ").upper()
extra_cheese = input("Do you want extra cheese? Y or N ").upper()
# π¨ Don't change the code above π

#Write your code below this line π
price = 0
#TamaΓ±o de pizza
if size == 'S':
  price += 15
elif size == 'M':
  price += 20
elif size == 'L':
  price += 25

#Se le agrega peperoni
if add_pepperoni == 'Y':
  if size == 'S':
    price += 2
  else:
    price += 3

#Se le agrega queso
if extra_cheese == 'Y':
    price += 1
print(f'your final bill is: ${price}')