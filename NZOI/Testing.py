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

count2 = 1
bad = 0
mah = []
while count2 <= int(people[0]):
    hosts = input().split()
    for i in range(6):
        if int(hosts[i+1]) < drinks[i]:
            ek = drinks[i] - int(hosts[i+1])
            bad = bad + ek
            print(bad)
    if bad >= 3:
        mah.append("{} Disaster ({})".format(hosts[0], bad))
    elif 1 <= bad <= 2:
        mah.append("{} Mildly Successful ({})".format(hosts[0], bad))
    elif bad <= 0:
        mah.append("{} Successful".format(hosts[0]))
    print(mah)
    bad = 0
    count2 += 1

count3 = 1
while count3 <= int(people[1]):
    who = input()
    if who in mah:
        print("yay")
    else:
        print("I failed")
    count += 1



for l in mah:
    print(l)


# G C E P L S
