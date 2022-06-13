n = int(input())

left_sum = 0
right_sum = 0
for i in range (n):
    current_sum = int(input())
    left_sum += current_sum
for i in range(n):
    current_sum = int(input())
    right_sum += current_sum
sum = left_sum
diff = abs(left_sum - right_sum)
if left_sum == right_sum:
    print(f"Yes, sum = {sum}")
else:
    print(f"No, diff = {diff}")