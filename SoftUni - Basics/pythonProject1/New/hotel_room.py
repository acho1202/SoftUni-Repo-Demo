month = input()
stay_nights = int(input())
price_studio = 0
price_apart = 0
if month == "May" or month == "October" :
    price_studio = stay_nights * 50
    price_apart = stay_nights * 65
    if 14 > stay_nights > 7 :
        price_studio *= 0.95
    elif stay_nights > 14:
        price_studio *= 0.7
        price_apart *= 0.9
elif month == "June" or month == "September":
    price_studio = stay_nights * 75.20
    price_apart = stay_nights * 68.70
    if stay_nights > 14:
        price_studio *= 0.8
        price_apart *= 0.9
elif month == "July" or month == "August" :
    price_studio = stay_nights * 76
    price_apart = stay_nights * 77
    if stay_nights > 14:
        price_apart *= 0.9
print(f"Apartment: {price_apart:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")