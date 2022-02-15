age = float(input("What is your age? "))
temp = float(input("What is your temperature? "))

print("Patient aged {} years, with a temperature of {} degrees Celsius".format(age, temp))

if age < 2 and temp >= 38:
    print("CALL A DOCTOR")
elif age >= 2 and temp >= 39.5:
    print("High Fever")
elif age >= 2 and temp <= 35:
    print("This is less than normal")
elif age >= 2 and 38 <= temp < 39.5:
    print("This is high than normal")
elif age >= 2 and 35 < temp < 38:
    print("You are fine")


