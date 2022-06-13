import math
name_of_actor = str(input())
points = float(input())
number_of_jury = int(input())

for current_grade in range (1,number_of_jury + 1):
    current_name = input()
    current_points = float(input())
    current_final_points = len(current_name) * current_points / 2
    points += current_final_points
    if points >= 1250.5 :
        break
if points > 1250.5:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {points:.1f}!")
else:
    diff = abs(1250.5 - points)
    print(f"Sorry, {name_of_actor} you need {diff:.1f} more!")