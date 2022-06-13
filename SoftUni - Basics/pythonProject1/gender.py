age = float(input())
gen = input()

if age >= 16:
    if gen == "m" :
       print("Mr.")
    else:
        print("Ms.")
if age < 16:
    if gen == "m":
        print("Master")
    else:
        print("Miss")

