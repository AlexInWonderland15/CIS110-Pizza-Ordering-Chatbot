print("Hello, my name is Alex! I am your virtual assistant. I will help you order a pizza!")
print("I am going to ask you a few questions. After typing an answer, press Enter.")

userName = input("\nEnter your name:  ")
while len(userName) == 0:
    userName = input("Hey, friend. Name cannot be blank! Please enter your name: ")

if userName.lower() == "alex crider":
    print(f"\nMy creator, {userName}. Happy to help you!")
else:
    print(f"\nYo, {userName}! Nice to meet you!")

size = input("\nWhat size do you want? Enter small, medium, or large:  ")
while size.lower() not in ["small", "medium", "large" ]:
    size = input("Yo! Invalid value! Please enter small, medium or large: ")
while len(size) == 0:
    size = input("Hey, pal. Size cannot be blank! Please enter a size: ")

flavor = input("\nEnter the flavor of pizza:  ")
while len(flavor) == 0:
    flavor = input("Hey, buddy. Flavor cannot be blank! Please enter a flavor: ")

crustType = input("\nWhat type of crust do you want?:  ")
while len(crustType) == 0:
    crustType = input ("Hey, comrade. Crust type cannot be blank! Please enter a crust type: ")

quantity = input("\nHow many of these do you want to order? Enter a numeric value:  ")
while not quantity.isdigit():
    quantity = input("Hey, dude. Value not recognized. Please enter a numeric value: ")
quantity = int(quantity)

method = input("\nIs this carry out or delivery?:  ")
while method not in ["carry out", "delivery"]:
    method = input("Hey, partner. Invalid value! Please enter carry out or delivery: ")
if method.lower() == "delivery":
    deliveryFee = 5
else:
    deliveryFee = 0

salesTax = 1.1
if size.lower() == "small":
    pizzaCost = 8.99
elif size.lower() == "medium":
    pizzaCost = 14.99
elif size.lower() == "large":
    pizzaCost = 17.99
total = (pizzaCost * quantity) * salesTax + deliveryFee


print("-" * 10)
print(f"Sick! Thanks for your order, {userName}!")
print(f"Your {quantity} {size} {flavor} pizza(s) with {crustType} crust costs ${total:,.2f}. Cool? Cool.")
if total >= 50:
    print("\nCongratulations! You've been awarded a coupon for $10 off your next order.")
else:
    print("\nOrders over $50 will receive a coupon for $10 off!")
print("-" * 10)