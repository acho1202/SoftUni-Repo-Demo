fruit = input()
day = input()
quanti = float(input())
week_day = day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Friday" or day == "Thursday"
off_day = day == "Saturday" or day == "Sunday"
is_valid = True
price = 0
if week_day:
    if fruit == "banana":
        price = 2.50
    elif fruit == "apple":
        price = 1.20
    elif fruit == "orange":
        price = 0.85
    elif fruit == "grapefruit":
        price = 1.45
    elif fruit == "kiwi":
        price = 2.70
    elif fruit == "pineapple":
        price = 5.50
    elif fruit == "grapes":
        price = 3.85
    else:
        is_valid = False
elif off_day:
    if fruit == "banana":
        price = 2.70
    elif fruit == "apple":
        price = 1.25
    elif fruit == "orange":
        price = 0.90
    elif fruit == "grapefruit":
        price = 1.60
    elif fruit == "kiwi":
        price = 3.00
    elif fruit == "pineapple":
        price = 5.60
    elif fruit == "grapes":
        price = 4.20
    else:
        is_valid = False
else:
    is_valid = False

total_price = price * quanti

if is_valid:
    print(f"{total_price:.2f}")
else:
    print("error")
