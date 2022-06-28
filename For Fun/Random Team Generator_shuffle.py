""" Random teams for my birthday """

import random


# Function
def teams(gender, letter):

    # Shuffling people
    random.shuffle(gender)
    total = len(gender)
    half = total // 2
    if letter == "f":
        half = total - half

    # Putting people into team
    for i in range(half):
        person = gender.pop(i)
        team_1.append(person)
    team_2.append(gender)


def printing_teams_2(team):
    for people in team:
        for names in people:
            print(names)


def printing_teams_1(team):
    for people in team:
        print(people)


# Main routine
team_1 = []
team_2 = []
change = "yes"


# Female
question = input(f"Enter Females: ").split(" ")

# Male
question_next = input(f"Enter Males: ").split(" ")


while change == "yes":

    # Restarting variables/lists
    team_1 = []
    team_2 = []
    question_new = []
    question_next_new = []
    question_new = question.copy()
    question_next_new = question_next.copy()

    # Creating shuffled teams
    teams(question_new, "f")
    teams(question_next_new, "")

    # Team 1
    print("\nTeam 1:")
    printing_teams_1(team_1)

    # Team 2
    print("\n\nTeam 2:")
    printing_teams_2(team_2)

    # Shuffling teams
    print()
    change = input("Do you want to change the teams? ").lower()

print("\nGoodbye and enjoy these teams!")
quit()

