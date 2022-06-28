""" Random teams for my birthday """

import random


female = input('Enter all the girls: ').split(" ")
male = input("Enter all the boys: ").split(" ")
team_1 = []
team_2 = []

random.shuffle(male)
random.shuffle(female)

total_m = len(male)
total_f = len(female)

half_m = total_m // 2
half_f = total_f - (total_f // 2)

for i in range(half_m):
    person = male.pop(i)
    team_2.append(person)

for num in range(half_f):
    person = female.pop(num)
    team_2.append(person)

team_1.append(male)
team_1.append(female)

print("Team 1:")
for peeps in team_1:
    for yes in peeps:
        print(yes, end=" ")

print("\nTeam 2:")
for peps in team_2:
    print(peps, end="")

