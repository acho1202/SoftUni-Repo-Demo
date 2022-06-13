first_num = int(input())
second_num = int(input())
for current_num in range (first_num, second_num + 1):
    odd_dig = 0
    even_dig = 0
    current_num = str(current_num)
    for index, digit in enumerate(current_num):
        if index % 2 == 0:
            odd_dig += int(digit)
        else:
            even_dig += int(digit)
    if odd_dig == even_dig:
        print(current_num, end = " ")