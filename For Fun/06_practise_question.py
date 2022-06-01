""" Taking a sentence and showing letter count and vowel count
Easy"""

sentence = input().strip().lower()
score = 0

print(len(sentence))

for i in sentence:
    if i in ('a', 'e', 'i', 'o', 'u'):
        score += 1

print(score)


