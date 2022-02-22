people = input().split()
drinks = [0, 0, 0, 0, 0, 0]


count = 1
while count <= int(people[0]):
    drinking = input().split()
    if drinking[1] == "G":
        drinks[0] += 1
    elif drinking[1] == "C":
        drinks[1] += 1
    elif drinking[1] == "E":
        drinks[2] += 1
    elif drinking[1] == "P":
        drinks[3] += 1
    elif drinking[1] == "L":
        drinks[4] += 1
    elif drinking[1] == "S":
        drinks[5] += 1
    count += 1
print(drinks)

count2 = 0
bad = 0
mah = []
while count2 <= int(people[1]):
    hosts = input().split()
    for i in drinks:
        if int(hosts[1]) < drinks[0]:
            bad += 1
            print(bad)
        elif int(hosts[2]) < drinks[1]:
            bad += 1
            print(bad)
        elif int(hosts[3]) < drinks[2]:
            bad += 1
            print(bad)
        elif int(hosts[4]) < drinks[3]:
            bad += 1
            print(bad)
        elif int(hosts[5]) < drinks[4]:
            bad += 1
            print(bad)
        elif int(hosts[6]) < drinks[5]:
            bad += 1
            print(bad)
    if bad > 3:
        mah.append("{} Disaster".format(hosts[0]))
    elif 1 <= bad < 2:
        mah.append("{} Mildly Successful".format(hosts[0]))
    elif bad <= 0:
        mah.append("{} Successful".format(hosts[0]))
    count2 += 1

for l in mah:
    print(l)


# G C E P L S
