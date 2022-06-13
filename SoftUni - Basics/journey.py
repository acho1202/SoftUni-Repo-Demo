budged = float(input())
season = input()
price = 0
if budged <= 100:
    if season == "summer":
        price = budged * 0.3
        print(f"Somewhere in Bulgaria")
        print(f"Camp - {price:.2f}")
    elif season == "winter":
        price = budged * 0.7
        print("Somewhere in Bulgaria")
        print(f"Hotel - {price:.2f}")
elif budged <= 1000 :
    if season == "summer":
        price = budged * 0.4
        print(f"Somewhere in Balkans")
        print(f"Camp - {price:.2f}")
    elif season == "winter":
        price = budged * 0.8
        print("Somewhere in Balkans")
        print(f"Hotel - {price:.2f}")
else:
    price = budged * 0.9
    print("Somewhere in Europe")
    print(f"Hotel - {price:.2f}")