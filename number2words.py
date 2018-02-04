"""
1B Number to String Challenge
"""

dial2word = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5":  ["j", "k", "l"],
             "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}


def read_dictionary():
    with open("google-10000-english-usa-no-swears.txt", 'r') as f:
        dictionary = [line.rstrip('\n') for line in f]

    return dictionary


def find_all_words(numbers):
    if "0" in numbers or "1" in numbers:
        return []

    words = dial2word[numbers[0]]
    for idx in range(1, len(numbers)):
        new_words = []
        for char in dial2word[numbers[idx]]:
            for word in words:
                new_words.append(word + char)
        words = new_words

    dictionary = read_dictionary()

    return filter(lambda x: x in dictionary, words)

print find_all_words("56")




