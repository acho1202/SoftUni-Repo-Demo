budged = float(input())
number_of_statists = int(input())
one_price_outfit = float(input())

decor_price = budged * 0.1
price_outfit = number_of_statists * one_price_outfit
if number_of_statists > 150:
    price_outfit *= 0.9
needed_money = decor_price + price_outfit
difference = abs(needed_money - budged)
if needed_money > budged:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
