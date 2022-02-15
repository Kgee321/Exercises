i = 1
while i <= 100:
    if i % 3 == 0 and i % 4 == 0:
        print("FuzzBuzz")
    elif i % 3 == 0:
        print("Fuzz")
    elif i % 4 == 0:
        print("Buzz")
    else:
        print(i)
    i += 1
