def extract_first_word_from_file(file_path):
    first_words = []
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into words
            words = line.split()
            # Extract the first word (assuming words are separated by space)
            if words:
                first_word = words[0]
                first_words.append(first_word)
    return first_words

