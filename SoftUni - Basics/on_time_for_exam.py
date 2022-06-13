hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arrival = int(input())
minutes_of_arrival = int(input())
time_of_examine = hour_of_exam * 60 + minutes_of_exam
time_of_arrival = hour_of_arrival * 60 + minutes_of_arrival
if time_of_arrival > time_of_examine:
    print("Late")
elif time_of_examine - 30 <= time_of_arrival <= time_of_examine:
    print("On time")
else:
    print("Early")
difference = abs(time_of_arrival - time_of_examine)
hours = difference // 60
minutes = difference % 60
if time_of_examine - 60 < time_of_arrival < time_of_examine:
    print(f"{minutes} minutes before the start.")
elif time_of_examine - 60 >= time_of_arrival :
    print(f"{hours}:{minutes:02d} hours before the start")
elif time_of_examine < time_of_arrival < time_of_examine + 60:
    print(f"{minutes} minutes after the start")
elif time_of_examine + 60 <= time_of_arrival:
    print(f"{hours}:{minutes:02d} hours after the start")