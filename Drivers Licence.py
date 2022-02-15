age = int(input("What is your age? "))
if age >= 16:
    print("You can apply for a Learners Licence")
else:
    print("You are to young to apply for a Learners Licence. \n Try again in {} years".format(16-age))
