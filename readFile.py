
lines = []

def read_file_lines(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                lines.append(line.strip())
        print("Contents of the file '{}':\n".format(filename))
        for line in lines:
            print(line)
    except FileNotFoundError:
        print("File '{}' not found.".format(filename))
    except Exception as e:
        print("An error occurred:", e)

# Example usage:
file_name = "example.txt"  # Replace with the name of your file
read_file_lines(file_name)
