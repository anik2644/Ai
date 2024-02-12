from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import string

def extract_keywords(summarized_text):
    # Download NLTK resources (if not already downloaded)
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')

    # Tokenize the text
    words = word_tokenize(summarized_text)

    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english') + list(string.punctuation))
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words]

    # Stemming
    ps = PorterStemmer()
    stemmed_words = [ps.stem(word) for word in filtered_words]

    # Return unique keywords
    return list(set(stemmed_words))

# Example list of summarized texts
summarized_texts = [
    "Government announces groundbreaking initiative to boost the economy and create jobs with positive impacts.",
    "Technology company unveils innovative device revolutionizing interaction with cutting-edge technology.",
    "Leaders reach historic agreement on climate change, addressing environmental challenges for a sustainable future."
]

# Extract keywords for each summarized text
for i, summarized_text in enumerate(summarized_texts, 1):
    keywords = extract_keywords(summarized_text)
    print(f"\nKeywords for Summarized Text {i}:", keywords)


'''
#for 4 keywords...


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import string

def extract_keywords(summarized_text, num_keywords=4):
    # Download NLTK resources (if not already downloaded)
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')

    # Tokenize the text
    words = word_tokenize(summarized_text)

    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english') + list(string.punctuation))
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words]

    # Stemming
    ps = PorterStemmer()
    stemmed_words = [ps.stem(word) for word in filtered_words]

    # Return a fixed number of keywords (first num_keywords)
    return list(set(stemmed_words))[:num_keywords]

# Example list of summarized texts
summarized_texts = [
    "Government announces groundbreaking initiative to boost the economy and create jobs with positive impacts.",
    "Technology company unveils innovative device revolutionizing interaction with cutting-edge technology.",
    "Leaders reach historic agreement on climate change, addressing environmental challenges for a sustainable future."
]

# Extract four keywords for each summarized text
for i, summarized_text in enumerate(summarized_texts, 1):
    keywords = extract_keywords(summarized_text, num_keywords=4)
    print(f"\nKeywords for Summarized Text {i}:", keywords)

'''