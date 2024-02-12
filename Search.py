from collections import Counter
import re

def count_word_occurrences(paragraph, words_to_find):
    # Tokenize the paragraph into words
    words = re.findall(r'\b\w+\b', paragraph.lower())  # Convert to lowercase for case-insensitive matching

    # Count occurrences of each word
    word_counts = Counter(words)

    # Extract counts for the specified words
    result = {word: word_counts[word] for word in words_to_find}

    return result

# Example usage:
paragraph = "This is a sample paragraph. This paragraph contains some words that we want to count."
words_to_find = ["this", "paragraph", "words"]

word_occurrences = count_word_occurrences(paragraph, words_to_find)

# Print the results
for word, count in word_occurrences.items():
    print(f"The word '{word}' appears {count} times in the paragraph.")
