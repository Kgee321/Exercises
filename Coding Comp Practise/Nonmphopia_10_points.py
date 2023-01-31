"""Problem H"""

week_people = input("Num: ")
points = {"TT": 75, "TX": 50, "PR": 80, "RT": 30, "AP": 25, "PX": 60}
final = []
while week_people != "0 0":
    everyone = {}
    for i in range(int(week_people[2])):
        info = input("Info: ").split(" ")
        name = info[0]
        point = info[1].upper()
        if point in points:
            if name in everyone:
                scoring = everyone[name] + points[point]
                print(scoring)
                everyone.update({name: scoring})
            else:
                everyone[name] = points[point]
        print(everyone)

    week = [week_people[0]]
    for name, score in everyone.items():
        print(score)
        if score > 100:
            week.append(name)
    if len(week) <= 1:
        week.append("No phones confiscated")
    final.append(week)
    week_people = input("Num: ")

for inside in final:
    print(f"Week {inside[0]}", end=" ")
    inside.remove(inside[0])
    for inside_2 in inside:
        if inside_2 == int:
            continue
        else:
            print(inside_2, end=", ")

