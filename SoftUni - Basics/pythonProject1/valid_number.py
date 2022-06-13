number = int(input())

valid_num = number >= 100 and number <= 200 or number == 0
if not valid_num:
    print("invalid")