import re
from string import ascii_letters
import collections
import statistics


def parse_sentences(text):
    sentences = re.split('\.|\?|!', text)
    list_of_words_and_sentences = []
    for sentence in sentences:
        words = parse_one_sentence(sentence)
        list_of_words_and_sentences.append(words)
        list_of_words_and_sentences = [x for x in list_of_words_and_sentences if x]
    return list_of_words_and_sentences


def parse_one_sentence(sentence):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    list_of_words = []
    new_word = ""
    sentence += " "
    for symbol in sentence:
        if symbol in ascii_letters or symbol.lower() in alphabet:
            new_word += symbol.lower()
        else:
            if new_word != "":
                list_of_words.append(new_word)
                new_word = ""
    return list_of_words


def make_ngramms(text, N):
    list_of_words_and_sentences = parse_sentences(text)
    ngramm_dict = dict()

    for sent in list_of_words_and_sentences:
        words = [word for word in sent]
        for i in range(len(words) - N + 1):
            if tuple(words[i:i + N]) in ngramm_dict:
                ngramm_dict[tuple(words[i:i + N])] += 1
            else:
                ngramm_dict[tuple(words[i:i + N])] = 1
    spisok = collections.Counter(ngramm_dict).most_common()
    return spisok


