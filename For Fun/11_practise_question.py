"""Replacing vowels with other vowels"""

sentence = input()
new_sentence = []

for i in range(len(sentence)):
    if sentence[i] == "u":
        new_sentence.append("a")
    elif sentence[i] == "o":
        new_sentence.append("u")
    elif sentence[i] == "i":
        new_sentence.append("o")
    elif sentence[i] == "e":
        new_sentence.append("i")
    elif sentence[i] == "a":
        new_sentence.append("e")
    else:
        new_sentence.append(sentence[i])

for letter in new_sentence:
    print(letter, end="")

