def word_order(words):
    words_occurrences = {}

    for word in words: 
        words_occurrences[word] = 0

    for word in words:
        words_occurrences[word] += 1

    return len(words_occurrences), list(words_occurrences.values())
