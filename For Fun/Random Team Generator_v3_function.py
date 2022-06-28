""" Random teams for my birthday """

import random


# Function
def teams(question):
    gender = input(f"Enter {question}: ").split(" ")
    random.shuffle(gender)
    total = len(gender)
    half = total // 2
    if question[0] == "F":
        half = total - half
    for i in range(half):
        person = gender.pop(i)
        team_1.append(person)
    team_2.append(gender)


# Main routine
team_1 = []
team_2 = []
teams("Females")
teams("Males")

# Team 1
print("\nTeam 1:")
for peeps in team_1:
    print(peeps)

# Team 2
print("\n\nTeam 2:")
for peps in team_2:
    for names in peps:
        print(names)




