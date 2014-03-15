# -*- coding: utf-8 -*-

import re
import jieba
from collections import defaultdict
from itertools import product, islice
from os.path import join, abspath, dirname

__all__ = ["Pinyin"]

BASE = abspath(dirname(__file__))
ZH_CN_RE = re.compile(ur'^[\u4e00-\u9fa5]+$')


class Pinyin(object):

    def __init__(self):

        self.word2pinyins = defaultdict(list)
        for line in open(join(BASE, "data/words.dic")):
            pinyin, words = line.strip().decode('utf-8').split(" ", 1)
            for item in words:
                self.word2pinyins[item].append(pinyin)

        self.word2pinyin = {}
        for l in open(join(BASE, "data/word.dic")):
            word, pinyin = l.strip().decode('utf-8').split(',')
            self.word2pinyin[word] = pinyin

        self.term2pinyin = {}
        for line in open(join(BASE, "data/term.dic")):
            term, pinyin = line.strip().decode('utf-8').split('#')
            self.term2pinyin[term] = pinyin.split('@')

        jieba.initialize()
        jieba.load_userdict(join(BASE, "data/user_dict.dic"))

    def _pinyin(self, term):
        pinyin_list = self.term2pinyin.get(term, None)
        if not pinyin_list:
            pinyin_list = [self.word2pinyin.get(word, word) for word in term]
        return pinyin_list

    def get_pinyin(self, text):
        term_list = jieba.cut(text, cut_all=False)
        pinyin_list_iter = (self._pinyin(term) if ZH_CN_RE.match(term) else [term] for term in term_list)
        return [pinyin for pinyin_list in pinyin_list_iter for pinyin in pinyin_list]

    def get_pinyin_all(self, text, max_return=None):
        if not isinstance(text, unicode):
            text = text.decode('utf-8', 'ignore')
        rs = [self.word2pinyins.get(word, [word]) for word in text]
        pinyin_all_iter = product(*rs)
        if max_return is not None:
            pinyin_all_iter = islice(pinyin_all_iter, 0, max_return)
        return pinyin_all_iter



if __name__ == "__main__":
    pinyin = Pinyin()
    text = "银行行长潘玮柏长了一头乌黑的白发， 睡觉睡的很晚, 道行很深"

    print "# get_pinyin(%s)" %  text
    for i in pinyin.get_pinyin(text):
        print i,
    print "\n"

    print "# get_pinyin_all(%s)" % text
    for i in pinyin.get_pinyin_all(text, max_return=8):
        print ' '.join(i),
    print "\n"
