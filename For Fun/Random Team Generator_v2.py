""" Random teams for my birthday """

import random


question = input('Enter name & gender separated by ":" ')
male = []
female = []
team_1 = []
team_2 = []

while question != "x":
    question = question.split(":")
    while True:
        if question[1] == "m":
            male.append(question[0])
            break
        if question[1] == "f":
            female.append(question[0])
            break
        else:
            print('Wrong input')
    question = input('Enter name & gender separated by ":" ')


random.shuffle(male)
random.shuffle(female)

total_m = len(male)
total_f = len(female)

half_m = total_m // 2
half_f = total_f - (total_f // 2)

print(half_m)
print(half_f)

# for i in range(half_m):
#     person = male.pop(i)
#     team_2.append(person)
#
# for i in range(half_f):
#     person = male.pop(i)
#     team_2.append(person)
#
# team_1.append(male)
# team_1.append(female)
#
# # team_1 = male[:total_m] + female[:total_f]
# # team_2 = male [total_m:] + female[total_f:]
#
# print(male)
# print(female)
#
# print(team_1)
# print(team_2)
#

