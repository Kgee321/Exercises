people = input().split()
count = 0
total_c = 0
total_g = 0
total_e = 0
total_p = 0
total_l = 0
while count <= int(people[0]):
    drink = input().split()
     if drink[1] == "C":
        total_c += 1
    elif drink[1] == "G":
        total_g += 1
    elif drink[1] == "E":
        total_e += 1
    elif drink[1] == "P":
        total_p += 1
    elif drink[1] == "L":
        total_l += 1
    elif drink[1] == "S":
        total_s += 1
    count += 1

count2 = 0
while count2 <= int(people[1]):
    cool = input().split()
    count2 += 1



