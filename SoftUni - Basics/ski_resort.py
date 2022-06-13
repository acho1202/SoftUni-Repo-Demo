days_of_stay =  int(input())
room_type = input()
rating = input()
room_price = 0
if days_of_stay < 10:
    if room_type == "apartment":
        room_price = (days_of_stay - 1) * 25
        room_price *= 0.70
    elif room_type == "president apartment":
        room_price = (days_of_stay - 1) * 35
        room_price *= 0.9
    else:
        room_price = (days_of_stay - 1) * 18
elif 10 < days_of_stay <= 15:
    if room_type == "apartment":
        room_price = (days_of_stay - 1) * 25
        room_price *= 0.65
    elif room_type == "president apartment":
        room_price = (days_of_stay - 1) * 35
        room_price *= 0.85
    else:
        room_price = (days_of_stay - 1) * 18
elif days_of_stay > 15:
    if room_type == "apartment":
        room_price = (days_of_stay - 1) * 25
        room_price *= 0.5
    elif room_type == "president apartment":
        room_price = (days_of_stay - 1) * 35
        room_price *= 0.8
    else:
        room_price = (days_of_stay - 1) * 18
if rating == "positive":
    total_cash = room_price + (room_price * 0.25)
elif rating == "negative":
    total_cash = room_price - (room_price * 0.1)
print(f"{total_cash:.2f}")