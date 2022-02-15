age = int(input("Enter your number: "))

age_final = age % 2

if age_final == 1:
    print("{} is an odd number".format(age))
else:
    print("{} is an even number".format(age))
