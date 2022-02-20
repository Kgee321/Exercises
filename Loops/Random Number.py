import random
number = random.randint(1, 101)
mode = input("Do you want to play Easy Mode (E) or Hard Mode (H)? ")
guess = int(input("Guess the number: "))
total = 1
counter = 1
limit = 0
if mode == "E":
    limit = 10
elif mode == "H":
    limit = 4
else:
    print("That was not a valid answer, \nType either E for Easy Mode or H for Hard mode")
while counter < limit and number != guess:
    if guess < number:
        print("Guess higher")
        guess = int(input("Guess the number: "))
        total += 1
        counter += 1
    if guess > number:
        print("Guess a lower number")
        guess = int(input("Guess the number: "))
        total += 1
        counter += 1
if counter == 10 or counter == 4:
    print("You ran out of guesses! Fail! Restart the game")
else:
    print(f"Correct number! You got it in {total} guesses")
