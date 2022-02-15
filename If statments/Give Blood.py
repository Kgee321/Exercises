AGE = float(input("What is your age? "))
WEIGHT = float(input("What is your weight? "))

print("Patient aged {} years, with a weight of {}...".format(AGE, WEIGHT))

if AGE < 16 or WEIGHT < 50:
    print("You cannot give blood")
else:
    print("You can give blood")


