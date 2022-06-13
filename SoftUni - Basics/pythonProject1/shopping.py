budged = float(input())
video = int(input())
processor = int(input())
ram = int(input())

vid_price = video * 250
proc_price = processor * (vid_price * 0.35)
ram_price = ram * (vid_price * 0.1)
price = vid_price + proc_price + ram_price


if video > processor :
    discount = price * 0.15
total_price =  price - discount
money_left = abs(budged - total_price)
if total_price <= budged:
    print(f"You have {money_left:.2f} leva left!")
else:
    print(f"Not enough money! You need {money_left:.2f} leva more!")
