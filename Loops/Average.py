num = int(input("How many numbers to be averaged: "))
i = 1
total = 0
while i <= num:
    other = float(input("Enter your number: "))
    total += other
    i += 1
print(f"Total is {round (total,2)}")
print(f"Average is {total/num:,.2f}")

