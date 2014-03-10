# -*- coding: utf-8 -*-

import re
import mmseg
import itertools
from collections import defaultdict
from os.path import join, abspath, dirname

__all__ = ["Pinyin"]

BASE = abspath(dirname(__file__))
ZH_CN_RE = re.compile(ur'^[\u4e00-\u9fa5]+$')


class Pinyin(object):

    def __init__(self):

        self.word2pinyins = defaultdict(list)
        for line in open(join(BASE, "data/pinyin/words.dic")):
            line = line.strip().decode('utf-8')
            pinyin, words = line.split(" ", 1)
            for item in words:
                self.word2pinyins[item].append(pinyin)

        self.word2pinyin = {}
        for l in open(join(BASE, "data/pinyin/word.dic")):
            word, pinyin = l.strip().split(',')
            self.word2pinyin[word] = pinyin

        self.term2pinyin = {}
        for line in open(join(BASE, "data/pinyin/term.dic")):
            term, pinyin = line.strip().split('#')
            self.term2pinyin[term] = pinyin.split('@')

        mmseg.mmseg.dict_load_words(join(BASE, "data/mmseg/words.dic"))

    def _perm(self, l):
        if not l:
            yield []
        else:
            for i in l[0]:
                for j in self._perm(l[1:]):
                    yield [i] + j

    def _pinyin(self, term):
        pinyin = self.term2pinyin.get(term, None)
        if not pinyin:
            pinyin = [self.word2pinyin.get(word.encode("utf-8"), word) for word in term.decode("utf-8")]
        return pinyin

    def get_pinyin(self, text):
        if isinstance(text, unicode):
            text = text.encode("utf-8", 'ignore')
        term_list = mmseg.seg_txt(text)
        pinyin_list = [
            self._pinyin(term) if ZH_CN_RE.match(term.decode("utf-8", 'ignore')) else [term]
            for term in term_list]
        return map(lambda pinyin: pinyin.decode('utf-8', 'ignore'), itertools.chain.from_iterable(pinyin_list))

    def get_pinyin_all(self, text):
        if not isinstance(text, unicode):
            text = text.decode('utf-8', 'ignore')
        rs = [self.word2pinyins.get(word, [word]) for word in text]
        if rs and max(len(word) for word in rs) > 1:
            return list(self._perm(rs))
        else:
            return [[word[0] for word in rs]]


if __name__ == "__main__":
    pinyin = Pinyin()
    text = "银行行长长了一头乌黑的白发， 睡觉睡的很晚"

    print "Pinyin:get_pinyin---", text
    for i in pinyin.get_pinyin(text):
        print i,
    print "\n"

    print "Pinyin:get_pinyin_all---", text
    for i in pinyin.get_pinyin_all(text):
        for j in i:
            print j,
        print
