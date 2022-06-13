student_counter = 0
standard_counter = 0
kid_counter = 0
total_tickets_counter = 0
command = input()
while command != "Finish":
    movie_name  = command
    free_places = int(input())
    sold_tickets = 0
    total_tickets = free_places
    while free_places > 0 :
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_counter += 1
        elif ticket_type == "standard":
            standard_counter += 1
        else:
            kid_counter += 1
        free_places -= 1
        sold_tickets += 1
        total_tickets_counter += 1
    percent_full_hall = sold_tickets / total_tickets * 100
    print(f"{movie_name} - {percent_full_hall:.2f}% full.")
    command = input()

print(f"Total tickets: {total_tickets_counter}")
print(f"{student_counter/total_tickets_counter*100 :.2f}% student tickets.")
print(f"{standard_counter/total_tickets_counter*100 :.2f}% standard tickets.")
print(f"{kid_counter/total_tickets_counter*100 :.2f}% kids tickets.")