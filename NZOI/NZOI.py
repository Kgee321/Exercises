story = int(input())
struts = 0
platform = 0
num = (story * 2) + 1


for i in range(2, num, 2):
    struts += i


for i in range(1, story):
    platform += i

print(platform+struts)
