""" Adapting 11_practise_question """

# Main routine

number = int(input())
sentence = input()
new_sentence = []
other_new_sentence = []

while number != 0:
    if number == 1:
        for i in range(len(sentence)):
            if sentence[i] == "u":
                other_new_sentence.append("a")
            elif sentence[i] == "o":
                other_new_sentence.append("u")
            elif sentence[i] == "i":
                other_new_sentence.append("o")
            elif sentence[i] == "e":
                other_new_sentence.append("i")
            elif sentence[i] == "a":
                other_new_sentence.append("e")
            else:
                other_new_sentence.append(sentence[i])

            for letter in other_new_sentence:
                print(letter, end="")
            other_new_sentence.clear()

    if number == 2:
        for i in range(len(sentence)):
            if sentence[i] == "a":
                new_sentence.append("u")
            elif sentence[i] == "u":
                new_sentence.append("o")
            elif sentence[i] == "o":
                new_sentence.append("i")
            elif sentence[i] == "i":
                new_sentence.append("e")
            elif sentence[i] == "e":
                new_sentence.append("a")
            else:
                new_sentence.append(sentence[i])

            for letter in new_sentence:
                print(letter, end="")
            new_sentence.clear()
    print()
    number = int(input())
    sentence = input()






