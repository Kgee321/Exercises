"""COMPLETE!! - 10 points"""

# Questions
classes = input()
ask = input()
final = {}
random = []

# Variables
g_score = 0
h_score = 0
r_score = 0
s_score = 0
g = "Gryffindor"
h = "Hufflepuff"
s = "Slytherin"
r = "Ravenclaw"

while classes != "END":
    while ask != "0 0 0":
        ask = ask.split(' ', 2)
        ask[1].capitalize()
        if ask[1] == g:
            g_score += int(ask[2])
        elif ask[1] == h:
            h_score += int(ask[2])
        elif ask[1] == s:
            s_score += int(ask[2])
        elif ask[1] == r:
            r_score += int(ask[2])
        ask = input("Second")
    ask = "1 1 1"
    classes = input("First")

final.update({g_score: g, h_score: h, s_score: s, r_score: r})

for score in final:
    random.append(score)

random.sort()

for i in range(1, 5):
    print(i, final[random[-i]], random[-i])


