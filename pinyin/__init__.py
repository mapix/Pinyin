# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from builtins import object

import jieba
from collections import defaultdict
from itertools import product, islice

from pinyin.config import FILE_WORDS, FILE_WORD, FILE_TERM, FILE_USER_DICT, CHINESE_RE
from pinyin.utils import Singleton
from future.utils import with_metaclass

__all__ = ["Pinyin"]


class Pinyin(with_metaclass(Singleton, object)):

    def __init__(self):

        self.word_to_pinyins = defaultdict(list)
        for line in open(FILE_WORDS):
            pinyin, words = line.strip().decode("utf-8").split()
            for item in words:
                self.word_to_pinyins[item].append(pinyin)

        self.word_to_pinyin = {}
        for line in open(FILE_WORD):
            word, pinyin = line.strip().decode("utf-8").split(",")
            self.word_to_pinyin[word] = pinyin

        self.term_to_pinyin = {}
        for line in open(FILE_TERM):
            term, pinyin = line.strip().decode("utf-8").split("#")
            self.term_to_pinyin[term] = pinyin.split("@")

        jieba.initialize()
        jieba.load_userdict(FILE_USER_DICT)

    def _pinyin(self, term, failure=None):
        pinyin_list = self.term_to_pinyin.get(term, None)
        if not pinyin_list:
            pinyin_list = [self.word_to_pinyin.get(word, word if failure is None else failure) for word in term]
        return pinyin_list

    def get_pinyin(self, text, failure=None):
        term_list = jieba.cut(text, cut_all=False)
        pinyin_list_iter = (
            self._pinyin(term, failure) if CHINESE_RE.match(term) else [term if failure is None else failure]
            for term in term_list
        )
        return [pinyin for pinyin_list in pinyin_list_iter for pinyin in pinyin_list]

    def get_pinyin_all(self, text, max_return=None, failure=None):
        if not isinstance(text, str):
            text = text.decode("utf-8", "ignore")
        rs = [self.word_to_pinyins.get(word, [word if failure is None else failure]) for word in text]
        pinyin_all_iter = product(*rs)
        if max_return is not None:
            pinyin_all_iter = islice(pinyin_all_iter, 0, max_return)
        return pinyin_all_iter
