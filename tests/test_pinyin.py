# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import unittest

from pinyin import Pinyin


class TestPinyin(unittest.TestCase):

    def setUp(self):
        self.pinyin = Pinyin()

    def test_pinyin(self):
        r = ' '.join(self.pinyin.get_pinyin('银行行长潘玮柏长了一头乌黑的白发，睡觉睡的很晚,道行很深', failure=''))
        expect = 'yin hang hang zhang pan wei bo zhang le yi tou wu hei de bai fa  shui jiao shui de hen wan  dao heng hen shen'
        assert r == expect

if __name__ == '__main__':
    unittest.main()
