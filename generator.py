import argparse
import text_parser
import collections
import random
import statistics


def init_arguments():
    parser = argparse.ArgumentParser(prog='Бредогенератор',
                                     usage='generator.py -f filename -s number of sentences')
    parser.add_argument('-f', '--file', help='Файл со статистикой', default=None)
    parser.add_argument('-s', '--sentences', help='Количество предложений для генерации', default=5)
    return parser


def main():
    parser = init_arguments()
    if parser.parse_args().file is None:
        print('usage:', parser.usage)
        return

    try:
        ngrams = statistics.parse_stat(parser.parse_args().file)
    except FileNotFoundError:
        print('Файл не найден')
        return

    ngrams_dict = make_ngrams_dict(ngrams)


def generate_bred(sent_count, ngrams_dict):
    bred_text = ''
    for i in range(sent_count):
        rand_first_word = f
        bred_text += was_generate_one_sentence(ngrams, word)
    return bred_text


def make_ngrams_dict(ngrams_list):
    ngrams_dict = {}
    for words, count in ngrams_list:
        if not words[0] in ngrams_dict:
            ngrams_dict[words[0]] = []
        ngrams_dict[words[0]].append((words[1:], count))


def was_generate_one_sentence(ngrams, current_word):
    sentence = make_capital_letter(current_word)
    while current_word in ngrams.keys():
        words = ngrams[current_word]
        next_word = words[random.randint(0, len(words) - 1)]
        current_word = next_word
        if current_word in sentence:
            continue
        sentence += ' ' + current_word
    sentence += '.'
    return sentence


def make_capital_letter(word):
    return word[0].upper() + word[1:]


def count_frequency(text):
    frequency_of_words = collections.Counter()
    for sent in text_parser.parse_sentences(text):
        for word in sent:
            frequency_of_words[word.lower()] += 1
    return frequency_of_words


if __name__ == '__main__':
    main()
