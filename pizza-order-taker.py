print("Welcome to Elephant Pizza, Inc. Ltd. Lp. PLLC. MD.!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")


#Write your code below this line 👇
bill = 0

if size == "S":
  bill += 15

if size == "M":
  bill += 20

if size == "L":
  bill += 25

if add_pepperoni == "Y" and size == "S":
  bill += 2
elif add_pepperoni == "Y":
  bill += 3

if extra_cheese == "Y":
  bill += 1

else: 
  bill == 0

print (bill)
