# nltk_test.py

""" ____ """

from collections import Counter
import nltk
nltk.download('punkt')

def get_tokens():
    """ __________ """

    with open('bk_1st-contact-with-tf.txt', 'r', encoding='utf-8') as temp_file:
        text = temp_file.read()
    
    tokens = nltk.word_tokenize(text)

    return tokens

tokens = get_tokens()
tokens_count = Counter(tokens)
most_common = 10

print(f'{most_common} most common tokens: {tokens_count.most_common(most_common)}')
