type_project = input()
seats = float(input())
colons = float(input())
cost = 0
if type_project == "Premiere":
    cost = seats * colons * 12
    print(f"{cost:.2f} leva")
elif type_project == "Normal":
    cost = seats * colons * 7.50
    print(f"{cost:.2f} leva")
elif type_project == "Discount":
    cost = seats * colons * 5.00
    print(f"{cost:.2f} leva")