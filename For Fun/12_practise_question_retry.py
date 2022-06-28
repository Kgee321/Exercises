""" Trying 12 a different way """


def function1(i, ii, iii, iiii, iiiii):
    for i in range(len(sentence)):
        if sentence[i] == iiiii:
            other_new_sentence.append(i)
        elif sentence[i] == iiii:
            other_new_sentence.append(iiiii)
        elif sentence[i] == iii:
            other_new_sentence.append(iiii)
        elif sentence[i] == ii:
            other_new_sentence.append(iii)
        elif sentence[i] == i:
            other_new_sentence.append(ii)
        else:
            other_new_sentence.append(sentence[i])

        value = ''
        for letter in other_new_sentence:
            value += letter
    new_sentence.append(value)


number = int(input())

sentence = input()
new_sentence = []
other_new_sentence = []


if number == 1:
    function1("a", "e", "i", "o", "u")
if number == 2:
    function1("u", "a", "e", "i", "o")
    print(new_sentence)


