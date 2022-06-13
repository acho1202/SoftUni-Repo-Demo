number_of_judges = int(input())
name_of_presentation = input()
all_grades_count = 0
all_grades_sum = 0
sum_count = 0
sum_grades_current = 0
while name_of_presentation != "Finish":
    sum_grades_current = 0
    sum_count = 0
    for count_of_tests in range(number_of_judges):
        current_grade = float(input())
        sum_grades_current += current_grade
        sum_count += 1
        current_avarage = sum_grades_current / sum_count
        all_grades_count += 1
        all_grades_sum += current_grade
    print(f"{name_of_presentation} - {current_avarage:.2f}.")
    name_of_presentation = input()
    all_avg = all_grades_sum / all_grades_count
    if name_of_presentation == "Finish":
        print(f"Student's final assessment is {all_avg:.2f}.")
