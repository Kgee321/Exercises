password = input("Enter Password: ")
count = 1
while count < 3 and password != "Pineapple":
    print("Password Wrong! You have {} attempts left".format(3 - count))
    password = input("Enter Password: ")
    count += 1
if password == "Pineapple":
    print("Access Granted")
else:
    print("Too many attempts")

