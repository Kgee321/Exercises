import math

answer = {}

num = int(input())
for i in range(num):
    question = input().split(" ")
    x = int(question[1])
    y = int(question[2])
    z = int(question[3])
    a = math.sqrt(x**2 + y**2)
    ans = math.sqrt(a**2 + z**2)
    if ans >= 1000:
        answer[question[0]] = "is out of range"
    else:
        answer[question[0]] = "is in range"

for name, responce in answer.items():
    print(name, responce)

