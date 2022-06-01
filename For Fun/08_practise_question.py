"""Adjusting 03_practise_question so that it accepts a 3rd number
Easy -- Because I already had the base code from previous question"""


number1 = int(input())
number2 = int(input())
terms = int(input())

difference = number2 - number1

for i in range(1, terms + 1):
    answer = difference * i + number2
    print(answer, end=" ")
