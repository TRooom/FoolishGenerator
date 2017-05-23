#!/usr/bin/env python3

import bred
import generator
import unittest
import text_parser


class TestParser(unittest.TestCase):

    def test_parse_one_sentence(self):
        simple_sentence = 'Разбитое по словам предложение'
        simple_result = ['разбитое', 'по', 'словам', 'предложение']
        self.assertListEqual(bred.parse_one_sentence(simple_sentence), simple_result)

        symbols_sentence = 'Разные ,*+=1234567890~&()[]{}" символы'
        symbols_result = ['разные', 'символы']
        self.assertListEqual(bred.parse_one_sentence(symbols_sentence), symbols_result)

    def test_parse_sentences(self):
        simple_text = 'Простой тест. Три предложения! С разными знаками?'
        simple_result = [['простой', 'тест'], ['три', 'предложения'], ['с', 'разными', 'знаками']]
        self.assertListEqual(bred.parse_sentences(simple_text), simple_result)

        symbols_text = 'Разные ,*+=1234567890~&()[]{}" символы'
        symbols_result = [['разные', 'символы']]
        self.assertListEqual(bred.parse_sentences(symbols_text), symbols_result)

    def test_make_bigrams(self):
        simple_list = [['простой', 'тест'], ['простой', 'текст'], ['простой', 'тест', 'слово']]
        simple_result = {'простой': {'тест': 2, 'текст': 1}, 'тест': {'слово': 1}}
        self.assertEqual(bred.make_bigrams(simple_list), simple_result)

        different_cases_list = [['СлОвА', 'напиСАнЫ'], ['слоВА', 'НапИсаНЫ', 'пО-РаЗноМУ']]
        different_cases_result = {'слова': {'написаны': 2}, 'написаны': {'по-разному': 1}}
        self.assertEqual(bred.make_bigrams(different_cases_list), different_cases_result)

        special_symbols_list = [['по-всякому', 'don\'t']]
        special_symbols_result = {'по-всякому': {'don\'t': 1}}
        self.assertEqual(bred.make_bigrams(special_symbols_list), special_symbols_result)


class TestGenerator(unittest.TestCase):

    def test_count_frequency(self):
        text = 'Слова слОва одиН ДВа слова ДВА'
        result = {'слова': 3, 'два': 2, 'один': 1}
        self.assertEqual(generator.count_frequency(text), result)

    def test_make_capital_letter(self):
        word = 'слово'
        result = 'Слово'
        self.assertEqual(generator.make_capital_letter(word), result)


class TestTextParser(unittest.TestCase):

    def test_ngramm(self):
        text = 'Простой тест. Три предложения! С разными знаками?'
        res = {('простой', 'тест'): 1, ('три', 'предложения'): 1, ('с', 'разными',): 1, ('разными', 'знаками'): 1}
        self.assertEqual(text_parser.ngramm(text, 2), res)


if __name__ == "__main__":
    unittest.main()
