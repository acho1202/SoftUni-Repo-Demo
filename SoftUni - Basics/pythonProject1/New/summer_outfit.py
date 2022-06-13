temperature = int(input())
time = str(input())
outfit = ""
shoes = ""
if 10 <= temperature <= 18 :
    if time == "Morning" :
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif time == "Afternoon":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif time == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
elif 18 < temperature <= 24:
    if time == "Morning" :
        outfit = "Shirt"
        shoes = "Moccasins"
    elif time == "Afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif time == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
elif temperature >= 25:
    if time == "Morning" :
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif time == "Afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
    elif time == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")