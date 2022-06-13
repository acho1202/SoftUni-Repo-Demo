import math
show_name = str(input())
ep_lenght = int(input())
break_lenght = int(input())

lunch_time = break_lenght / 8
chill_time = break_lenght / 4
total_break =  break_lenght - lunch_time - chill_time
time_left = abs(total_break - ep_lenght)
if total_break >= ep_lenght:
    print(f"You have enough time to watch {show_name} and left with {math.ceil(time_left)} minutes free time.")
else:
    print(f"You don't have enough time to watch {show_name}, you need {math.ceil(time_left)} more minutes.")

