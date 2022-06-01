""" Adjusting 06_practise_question so works for many lines
Medium -- I don't think I did this the most simple way but oh well"""

lines = int(input())
vowels = 0
num = 0
lists = []

while num != lines:
    one_line = input().strip().lower()
    lists.append(one_line)
    for x in one_line:
        if x in ("a", "e", "i", "o", "u"):
            vowels += 1
    num += 1

for i in range(lines):
    print(len(lists[i]))
print(vowels)
