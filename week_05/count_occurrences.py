"""
CP1404/CP5632 Practical - Suggested Solution
Count word occurrences in a string
"""

word_dict = {}
text = input("Text: ")
words = text.split()
for word in words:
    occurance = word_dict.get(word, 0)
    if occurance is None:
        word_dict[word] = 1
    else:
        word_dict[word] = occurance + 1
words = list(word_dict.keys())
words.sort()
max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, word_dict[word]))