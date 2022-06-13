product = input()
town = input()
quantity = float(input())

ammount = 0
if town == "Sofia":
    if product == "coffee":
        ammount = 0.50
    elif product == "water":
        ammount = 0.80
    elif product == "beer":
        ammount = 1.20
    elif product == "sweets":
        ammount = 1.45
    elif product == "peanuts":
        ammount = 1.60

elif town == "Plovdiv":
    if product == "coffee":
        ammount = 0.40
    elif product == "water":
        ammount = 0.70
    elif product == "beer":
        ammount = 1.15
    elif product == "sweets":
        ammount = 1.30
    elif product == "peanuts":
        ammount = 1.50

elif town == "Varna":
    if product == "coffee":
        ammount = 0.45
    elif product == "water":
        ammount = 0.70
    elif product == "beer":
        ammount = 1.10
    elif product == "sweets":
        ammount = 1.35
    elif product == "peanuts":
        ammount = 1.55
price = quantity * ammount
print(price)