# Questions
classes = input()
ask = input()

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
        print(ask)
        ask[1].capitalize()
        if ask[1] == g:
            g_score += int(ask[2])
        elif ask[1] == h:
            h_score += int(ask[2])
        elif ask[1] == s:
            s_score += int(ask[2])
        elif ask[1] == r:
            r_score += int(ask[2])
        ask = input()
    classes = input()
print(f"{g}:{g_score}")
print(f"{h}:{h_score}")
print(f"{s}:{s_score}")
print(f"{r}:{r_score}")

