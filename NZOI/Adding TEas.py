drink = input().split()
total_c = 0
total_g = 0
total_e = 0
total_p = 0
total_l = 0
total_s = 0
while drink[0] != "D":
    if drink[0] == "C":
        total_c += int(drink[1])
        drink = input().split()
    elif drink[0] == "G":
        total_g += int(drink[1])
        drink = input().split()
    elif drink[0] == "E":
        total_e += int(drink[1])
        drink = input().split()
    elif drink[0] == "P":
        total_p += int(drink[1])
        drink = input().split()
    elif drink[0] == "L":
        total_l += int(drink[1])
        drink = input().split()
    elif drink[0] == "S":
        total_s += int(drink[1])
        drink = input().split()
print(total_g, total_c, total_e, total_p, total_l, total_s)





