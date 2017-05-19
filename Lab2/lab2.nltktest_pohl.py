""" ____ """

from collections import Counter
import string
import io
import nltk

nltk.download('punkt')

def get_tokens():
    """ __________ """
    with open('FirstContactWithTensorFlow.txt', 'r', encoding='utf-8') as temp_file:
        text = temp_file.read()
        tokens = nltk.word_tokenize(text)
        return tokens

C_TOKENS = get_tokens()
C_COUNT = Counter(C_TOKENS)
print C_COUNT.most_common(10)
