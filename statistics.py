import argparse
import text_parser
import re


def init_arguments():
    parser = argparse.ArgumentParser(prog='Бредогенератор',
                                     usage='stat.py -f filename -n n-gramms parametr')
    parser.add_argument('-f', '--file', help='Файл с тектом для обучения', default=None)
    parser.add_argument('-n', '--number', help='Параметр N для N-грамм', default=2)
    return parser


def main():
    parser = init_arguments()
    if parser.parse_args().file is None:
        print('usage:', parser.usage)
        return

    try:
        path = parser.parse_args().file
        file = open(path, 'r', encoding='UTF-8')
    except FileNotFoundError:
        print('Файл не найден')
        return

    text = file.read()
    file.close()
    ngrams = text_parser.make_ngramms(text, int(parser.parse_args().number))
    write_down_in_file(ngrams)

    ngrs = parse_stat('stat.txt')


def write_down_in_file(ngrams):
    file = open('stat.txt', 'w', encoding='utf-8')
    for ngram in ngrams:
        s = ngram_to_string(ngram)
        file.write(s + '\n')
    file.close()


def ngram_to_string(ngram):
    result = ['[']
    for word in ngram[0]:
        result.append(word)
    result.append(']')
    result.append(':')
    result.append(str(ngram[1]))
    return ' '.join(result)





def parse_stat(path):
    file = open(path, 'r', encoding='utf-8')
    ngrams = []
    for line in file:
        count = int(line.split(':')[1])
        words = line.split(':')[0]
        words_list = tuple([x for x in (re.sub('[]\[]', '', words).split(' ')) if x])
        ngram = (words_list, count)
        ngrams.append(ngram)
    file.close()
    return ngrams


if __name__ == '__main__':
    main()