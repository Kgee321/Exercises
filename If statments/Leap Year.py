year = int(input("Enter Your Year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("{} is a leap year".format(year))
        else:
            print("{} is a not leap year".format(year))
    else:
        print("{} is a leap year".format(year))
else:
    print("{} is a not leap year".format(year))
