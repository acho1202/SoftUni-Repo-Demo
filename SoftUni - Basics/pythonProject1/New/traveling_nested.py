command = input()
while command != "End":
    destination_price = float(input())
    saved_money = 0
    while saved_money <= destination_price:
        current_saved_money = float(input())
        saved_money += current_saved_money
    print(f"Going to {command}!")
    command = input()