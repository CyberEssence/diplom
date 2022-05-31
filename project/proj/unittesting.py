#!/usr/bin/python
# -*- coding: utf-8 -*-

""" 

    Author: Solovov N. G. (CyberEssence)
    
"""

import unittest
from golos import Text

# юнит-тестирование правильности сгенерированного текста

class TestGetText(unittest.TestCase):

    def setUp(self):
        self.text = Text()

    def test_get_text_case_1(self):
        self.assertEqual(self.text.get_text()[1:21],
                         "что происходит малыш")

    def test_get_text_case_2(self):
        self.assertEqual(self.text.get_text()[23:54],
                         "тебя уже третий раз ловят на драке")

    def test_get_text_case_3(self):
        self.assertEqual(self.text.get_text()[56:82],
                         "я знаю пора бы уже научиться")

    def test_get_text_case_4(self):
        self.assertEqual(self.text.get_text()[84:104],
                         "я не могу тебя понять")

    def test_get_text_case_5(self):
        self.assertEqual(self.text.get_text()[106:136],
                         "папа мог я тоже по нему скучаю")


if __name__ == '__main__':
    unittest.main()
