""" Random teams for my birthday """

import random

name = input("Person: ")
gender = input("Gender: ").lower()
male = []
female = []
team_1 = []
team_2 = []

while True:
    while True:
        if gender == "m":
            male.append(name)
            break
        if gender == "f":
            female.append(name)
            break
        else:
            gender = input("Gender: ").lower()
    leave = input("Done? ").lower()
    if leave == "x":
        break
    name = input("Person: ")
    gender = input("Gender: ").lower()


random.shuffle(male)
random.shuffle(female)

total_m = len(male)
total_f = len(female)

half_m = total_m // 2
half_f = total_f - (total_f // 2)

print(half_m)
print(half_f)

for i in range(half_m):
    person = male.pop(i)
    team_2.append(person)

for i in range(half_f):
    person = male.pop(i)
    team_2.append(person)

team_1.append(male)
team_1.append(female)

# team_1 = male[:total_m] + female[:total_f]
# team_2 = male [total_m:] + female[total_f:]

print(male)
print(female)

print(team_1)
print(team_2)


