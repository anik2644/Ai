import os

data = [
    {"current": 10},
    {"burning": 10},
    {"trending": 10},
    {"gender-bending": 30},
    {"bisexual": 50},
    {"transgender": 100},
]

def calculate_sum(input_string):
    total_sum = 0
    for item in data:
        for key, value in item.items():
            if key in input_string:
                total_sum += value
    return total_sum


def generate_heuristic_onList(directory_path, filelist):
    max_value = float('-inf')
    max_file_path = None
    for filename in filelist:
        fname = filename + '.txt'
        file_path = os.path.join(directory_path, fname)
        if os.path.exists(file_path): 
            with open(file_path, 'r', encoding='utf-8') as file:  # Specify encoding here
                content = file.read()
                heuristic_value = calculate_sum(content)
                if heuristic_value > max_value:
                    max_value = heuristic_value
                    max_file_path = file_path
    return max_file_path


def extract_first_word_from_file(file_path):
    first_words = []
    with open(file_path, 'r', encoding='utf-8') as file:  # Specify encoding here
        for line in file:
            # Split the line into words
            words = line.split()
            # Extract the first word (assuming words are separated by space)
            if words:
                first_word = words[0].lower()  # Convert to lowercase
                first_words.append(first_word)
    return first_words
def generate_heuristic(directory):
    max_value = float('-inf')
    max_file_path = None
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):  # Assuming files are text files
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                content = file.read()
                heuristic_value = calculate_sum(content)
                if heuristic_value > max_value:
                    max_value = heuristic_value
                    max_file_path = file_path
    return max_file_path

def find_files_in_folder(directory):
    file_names = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_names.append(filename)
    return file_names

# Example usage:
directory_path = "1.number"  # Update with your directory path
second_directory_path = "2.title"
third_directory_path = "3.specific"
file_with_highest_heuristic = generate_heuristic(directory_path)

if file_with_highest_heuristic:
    with open(file_with_highest_heuristic, 'r') as file:
        file_content = file.read()
        title_words = [word.lower() for word in file_content.split()]
        print(title_words)

        file_with_highest_heuristic_second = generate_heuristic_onList(second_directory_path, title_words)

        first_words_list = extract_first_word_from_file(file_with_highest_heuristic_second)
        print("First words from each line:", first_words_list)

        if file_with_highest_heuristic_second:
            print("File with the highest heuristic value in the second directory:", file_with_highest_heuristic_second)
        else:
            print("No file found with the provided filenames in the second directory.")

        file_with_highest_heuristic_third = generate_heuristic_onList(third_directory_path, first_words_list)
        if file_with_highest_heuristic_third:
            with open(file_with_highest_heuristic_third, 'r') as third_file:
                third_file_content = third_file.read()
                print("Content of file with the highest heuristic value in the third directory:")
                print(third_file_content)
        else:
            print("No file found with the provided first words in the third directory.")


