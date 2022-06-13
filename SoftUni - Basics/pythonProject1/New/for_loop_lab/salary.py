number_of_tabs = int(input())
salary = int(input())
bills = 0
for i in range (number_of_tabs):
    website = str(input())
    if website == "Facebook":
        salary -= 150
        bills += 150
        if salary <= 0:
            break
    elif website == "Instagram":
        salary -= 100
        bills += 100
        if salary <= 0:
            break
    elif website == "Reddit":
        salary -= 50
        bills += 50
        if salary <= 0:
            break
total_salary = salary - bills
if salary <= 0 :
    print("You have lost your salary.")
else:
    print(f"{salary}")
