from collections import Counter
import re

def find_word_concurrency_in_list(paragraphs, words_to_find):
    result_list = []

    for paragraph in paragraphs:
        # Tokenize the paragraph into words
        words = re.findall(r'\b\w+\b', paragraph.lower())  # Convert to lowercase for case-insensitive matching

        # Count occurrences of each word
        word_counts = Counter(words)

        # Extract counts for the specified words
        result = {word: word_counts[word] for word in words_to_find}
        result_list.append(result)

    return result_list

# Example usage:


paragraphs_list = [
    "In a surprising turn of events, the government announced a groundbreaking initiative aimed at boosting the economy and creating jobs. Experts predict significant positive impacts on various sectors.",
    
    "Breaking News: A prominent technology company unveiled its latest innovation, a cutting-edge device set to revolutionize the way we interact with technology. Stay tuned for detailed reviews and analysis.",
    
    "Amid ongoing international discussions, leaders from different nations reached a historic agreement on climate change. The accord is expected to address environmental challenges and pave the way for a sustainable future.",
    
    "Health officials report a major breakthrough in the fight against a global health crisis. The newly developed treatment shows promising results in clinical trials, raising hopes for a swift resolution.",
    
    "Finance experts analyze the latest market trends, predicting potential shifts in investment strategies. Investors are advised to stay informed as economic uncertainties continue to impact global financial markets.",
    
    "Cultural enthusiasts rejoice as a renowned artist prepares to unveil a groundbreaking exhibition. The showcase promises to captivate audiences with its innovative approach to contemporary art.",
    
    "Sports fans are eagerly anticipating the upcoming championship match, where two top teams will compete for the coveted title. Analysts share insights on team strategies and key players to watch.",
    
    "In an exclusive interview, a leading scientist discusses groundbreaking research findings that could reshape our understanding of a fundamental aspect of the natural world. The implications are far-reaching.",
    
    "The entertainment industry buzzes with excitement as a highly anticipated film prepares for its premiere. A star-studded cast and a compelling storyline make it a must-watch for movie enthusiasts.",
    
    "Education leaders unveil a comprehensive plan to enhance learning experiences for students. The initiative includes innovative teaching methods and the integration of cutting-edge technology in classrooms.",
    
    "Global leaders convene for a summit addressing pressing geopolitical issues. Discussions center around diplomatic efforts, conflict resolution, and strategies for promoting international cooperation.",
    
    "In a heartwarming story, a local community comes together to support a charitable cause. Volunteers and donors collaborate to make a positive impact on the lives of those in need.",
]
words_to_find = ["a", "innovation", "the"]

word_concurrency_list = find_word_concurrency_in_list(paragraphs_list, words_to_find)

# Print the results for each paragraph
for idx, word_concurrency in enumerate(word_concurrency_list, start=1):
    print(f"\nParagraph {idx}:")
    for word, concurrency in word_concurrency.items():
        print(f"The word '{word}' appears {concurrency} times.")


        #search the News and create a list
        #find the summury and create summury list
        #find keywors of each list; create searching keywords list
        # the with the list search aging by dfs and bfs and collect the news like step-1 and create a list
        #repeat step-2,3,4 again and again;

        #in terms of huristic: search with the keywords in depth;