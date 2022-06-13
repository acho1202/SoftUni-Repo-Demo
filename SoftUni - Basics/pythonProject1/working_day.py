day = input()

is_working_day = day == "Monday" or day == "Tuesday" or day == "Wednesday" or day ==  "Thursday" or day == "Friday"
is_week = day == "Saturday" or day == "Sunday"

if is_working_day:
    print("Working day")
elif is_week:
    print("Weekend")
else:
    print("Error")
