""" Practise questions from year 9 coding comp
Medium"""

number1 = int(input())
number2 = int(input())

difference = number2 - number1

for i in range(1, 4):
    answer = difference * i
    answer1 = answer + number2
    print(answer1, end=" ")
