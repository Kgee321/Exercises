day = input("What day of the week is it? ")

if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday":
    print("Alam rings at 7am")
elif day == "saturday":
    print("Alam rings at 8am")
elif day == "sunday":
    print("Alam rings at 9am")
else:
    print("Try again, make sure you don't use an captain letters and all words are spelt correct")
