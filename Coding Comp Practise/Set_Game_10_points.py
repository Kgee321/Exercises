"""FAIL!!"""

num = int(input())
sentence = input().split(" ")
final_list = []
final_final_list = []

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i" ,"j",
            "k", "l" "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


for word in sentence:
    final_answer = ""
    word = list(word)
    for letter in word:
        indexing = alphabet.index(letter)
        final_num = indexing + num - 1
        print(indexing)
        print(final_num)
        print(final_num % 26)
        print(alphabet[final_num % 26])
    #     final_answer = f"{final_answer}{alphabet[final_num]}"
    # final_list.append(final_answer)


for words in final_list:
    print(words, end=" ")


