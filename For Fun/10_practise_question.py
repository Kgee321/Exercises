""" No input -- make a pretty shape thing with #
Hard -- Because I did not just use print statements"""

print("#" * 9)
for i in range(8, 2, -2):
    space = " " * (9-i)
    symbol = "#" * ((i+1)//2)
    print(f"{symbol}{space}{symbol}")

for i in range(1, 8, 2):
    space = " " * (8-i)
    symbol = "#" * ((i+1)//2)
    print(f"{symbol}{space}{symbol}")

print("#" * 9)
