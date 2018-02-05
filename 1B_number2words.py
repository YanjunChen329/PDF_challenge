"""
1B Number to String Challenge
"""

from collections import defaultdict
import sys

# This dictionary maps numbers to its associated letters in standard phone key pads.
# 0 and 1 have no associated letters
dial2word = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5":  ["j", "k", "l"],
             "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}


def read_dictionary():
    """
    Read the common english word dictionary file and return an array consisting of its words.
    """
    with open("google-10000-english-edited.txt", 'r') as f:
        dictionary = [line.rstrip('\n') for line in f]

    return dictionary


def find_all_words(numbers):
    """
    Given a number string, return all the legal words it could translate to based on the phone keypads
    :param numbers: string of numbers
    :return: a list of all possible words. Return empty list if 0 or 1 is in the input
    """
    # There is no conversion for 0 and 1
    if "0" in numbers or "1" in numbers:
        return []

    # Iterate over every possible conversion of every number and generate all combinations
    words = dial2word[numbers[0]]
    for idx in range(1, len(numbers)):
        new_words = []
        for char in dial2word[numbers[idx]]:
            for word in words:
                new_words.append(word + char)
        words = new_words

    dictionary = read_dictionary()

    return filter(lambda x: x in dictionary, words)  # Filter out all the illegal words

# print find_all_words("3433")
# print find_all_words("433")
# print find_all_words("34")
# print find_all_words("3")


def get_dp_matrix(numbers):
    """
    Giving a string of numbers, use dynamic programming to find a matrix in which each entry M[i,j]
    denotes the biggest number of converted number in a substring of the input that starts from i
    and includes the word converted from the ith to jth number in the list.
    :param numbers: a string of numbers
    :return: a dynamic programming matrix
    """

    # Create the dp matrix and initialize the last row
    matrix = defaultdict(lambda: defaultdict(int))
    matrix[len(numbers)-1][len(numbers)-1] = int(len(find_all_words(numbers[-1])) > 0)

    # Iterate from bottom to top: each entry equals to S[i,j] + the maximum of row M[j+1]
    for i in range(len(numbers)-1, -1, -1):
        for j in range(i, len(numbers)):
            # calculate the length of words converted from the ith to jth number in the list
            score = int(len(find_all_words(numbers[i: j+1])) > 0) * (j-i+1)
            if j == len(numbers) - 1:
                matrix[i][j] = score
            else:
                matrix[i][j] = score + max(matrix[j+1].values())
    return matrix


def traceback(matrix, numbers):
    """
    Traceback the dp matrix and return the string after the optimal conversion
    :param matrix: a dp matrix
    :param numbers: a list of numbers
    :return: the string after the conversion
    """
    result = []
    j = 0
    # Starting from row 0, find the path within the matrix that yields the highest conversion rate
    while j < len(numbers):
        # Reinitialize the value
        max_val = float("-inf")
        next_j = 0
        # find the maximum value in row j
        for i in matrix[j]:
            if matrix[j][i] >= max_val:
                max_val = matrix[j][i]
                next_j = i + 1

        # Add the converted words into a list
        string = numbers[j: next_j]
        if find_all_words(string):
            result.append(find_all_words(string)[0])
        else:
            result.append(string)
        j = next_j  # Update j

    return "-".join(result)


def convert_number_to_words(numbers):
    """
    Convert a given string of numbers to a string of number and words in a way that maximizes
    the conversion rate of the input
    :param numbers: a list of numbers
    :return: the string after the conversion
    """
    matrix = get_dp_matrix(numbers)
    return traceback(matrix, numbers)

# print convert_number_to_words("15815584956")
# print convert_number_to_words("2551874198583107")


def run():
    if len(sys.argv) != 2:
        print "Wrong number of argument! Need 1."
        return None
    else:
        try:
            numbers = sys.argv[1]
            for number in numbers:
                x = int(number)
        except TypeError:
            print "Illegal input. Input should be a string of number"
            return None
        print convert_number_to_words(numbers)


# Run
if __name__ == '__main__':
    run()
