mark = float(input("What is your Mark? "))

if 100 >= mark >= 90:
    print("Your grade: A")
elif 70 <= mark <= 89:
    print("Your grade: B")
elif 50 <= mark <= 69:
    print("You grade: C")
else:
    print("Sorry, you Failed")

