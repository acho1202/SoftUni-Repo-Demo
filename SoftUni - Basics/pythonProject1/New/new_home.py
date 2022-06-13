type_flow = input()
num_flow = int(input())
budged = float(input())
price = 0
discount = 0
price_a = 0

if type_flow == "Roses":
    if num_flow > 80:
        discount = price * 0.1
        price = num_flow * 5
        price_a = price - discount
    else:
        price_a = num_flow * 5
elif type_flow == "Dahlias":
    if num_flow > 90:
        discount = price * 0.15
        price = num_flow * 3.8
        price_a = price - discount
    else:
        price_a = num_flow * 3.8
elif type_flow == "Tulips":
    if num_flow > 80:
        discount = price * 0.15
        price = num_flow * 2.8
        price_a = price - discount
    else:
        price_a = num_flow * 2.8
elif type_flow == "Narcissus":
    if num_flow < 120:
        discount = price * 0.15
        price = num_flow * 3
        price_a = price + discount
    else:
        price = num_flow * 3
elif type_flow == "Gladiolus":
    if num_flow < 80:
        discount = price * 0.2
        price = num_flow * 2.5
        price_a = price + discount
    else:
        price_a = num_flow * 2.5
money_left = abs(price_a - budged)

if budged >= price_a:
    print(f"Hey, you have a great garden with {num_flow} {type_flow} and {money_left:.2f} leva left.")
else:
    print(f"Not enough money, you need {money_left:.2f} leva more.")