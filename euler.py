# problem 0:

# number = 1
# answer = 0
# for number in range(1, 720000, 2):
#     answer += number*number
# print(answer)

# problem 1:

# number = 3
# answer = 0
# for number in range(3, 1000, 3):
#   answer += number

# number2 = 5
# answer2 = 0
# for number2 in range(5, 1000, 5):
#     if number2 % 3 != 0:
#         answer2 += number2
# print(answer+answer2)

# problem 2:

# num_1 = 1
# num_2 = 2
# answer = 3
# total = 0

# while answer <= 4000000:
#     if answer % 2 == 0:
#         total += answer
#     num_1 = num_2
#     num_2 = answer
#     answer = num_1+num_2
# print(total+2)

# problem 3:

# large_number = 600851475143
# factor = 2
# list_of_factors = []

# for factor in range(2, int(large_number**0.5)):
#     while large_number % factor == 0:
#         list_of_factors.append(factor)
#         large_number = large_number / factor

# print(list_of_factors)

# problem 4:
answer = 0

for num_1 in range(100, 1000, 1):
    for num_2 in range(num_1, 1000, 1):
        total=num_1*num_2
        temp_total = total
        reverse_total = 0
        while temp_total > 0:
            digit = temp_total % 10
            reverse_total = reverse_total * 10 + digit
            temp_total = temp_total // 10
        if total == reverse_total and (total > answer):
            answer = total
            
print(answer)