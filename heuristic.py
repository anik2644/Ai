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

# Example usage:
input_string = "I identify as transgender and bisexual"
result = calculate_sum(input_string)
print("Total sum:", result)
