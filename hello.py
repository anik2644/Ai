
import os
import re
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


def extract_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # Use regular expression to find words (sequences of alphanumeric characters)
            words = re.findall(r'\b\w+\b', content)
            # Join the words into a single string separated by space
            cleaned_text = ' '.join(words)
            return cleaned_text
    except FileNotFoundError:
        print(f"File not found at path: {file_path}")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def generate_heuristic_onList(filelist):
    max_value = float('-inf')
    max_file_path = None
    for filename in filelist:
        fname = filename + '.txt'
        file_path = os.path.join(second_directory_path, fname)
        print(file_path)
        if os.path.exists(file_path): 
            with open(file_path, 'r') as file:
                content = file.read()
                heuristic_value = calculate_sum(content)
                if heuristic_value > max_value:
                    max_value = heuristic_value
                    max_file_path = file_path
    return max_file_path


def generate_heuristic_onListt(filelist):
    max_value = float('-inf')
    max_file_path = None
    for filename in filelist:
        fname = filename + '.txt'
        file_path = os.path.join(third_directory_path, fname)
        print(file_path)
        if os.path.exists(file_path): 
            cleaned_text = extract_words(file_path)
            if cleaned_text is not None:
                heuristic_value = calculate_sum(cleaned_text)
                if heuristic_value > max_value:
                    max_value = heuristic_value
                    max_file_path = file_path


    return max_file_path


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


def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"File not found at path: {file_path}")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


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
     

        file_with_highest_heuristic = generate_heuristic_onList(title_words)

        first_words_list = extract_first_word_from_file(file_with_highest_heuristic)
        print("First words from each line:", first_words_list)
        if file_with_highest_heuristic:
           print("File with the highest heuristic value:", file_with_highest_heuristic)
        else:
          print("No file found with the provided filenames.")

        fi = generate_heuristic_onListt(first_words_list)
        print(fi)
        file_content = read_file(fi)
        if file_content is not None:
          print("File content:")
          print(file_content)



