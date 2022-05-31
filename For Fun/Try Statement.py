"""Testing try statements"""

x = 42
y = 0

try:
    print(x/y)
except ZeroDivisionError as e:
    print("Not allowed to divide by 0")
else:
    print("Something wrong")
finally:
    print("This is our clean up code")
