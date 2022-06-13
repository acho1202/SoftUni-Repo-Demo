price_for_trip = float(input())
puzzles_num = int(input())
dolls_num = int(input())
bears_num = int(input())
minion_num = int(input())
trucks_num = int(input())

puzzle_pr = puzzles_num * 2.60
dolls_pr = dolls_num * 3
bear_pr = bears_num * 4.10
minion_pr = minion_num * 8.20
truck_pr = trucks_num * 2

price = truck_pr + dolls_pr + bear_pr + minion_pr + truck_pr
toys_num = puzzles_num + dolls_num + bears_num + minion_num + trucks_num
discount = 0

if toys_num >= 50:
    discount = price * 0.25
else :
    discount = 0
price_with_discount = price - discount
total_price = price - price_with_discount
rent = total_price * 0.1
earn = total_price - rent
money_left =  earn - price_for_trip
money_needed = abs(money_left)
if earn >= price_for_trip:
    print(f"Yes! {money_left} lv left.")
else:
    print(f"Not enough money! {money_needed} lv needed.")





