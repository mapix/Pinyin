#!/usr/bin/env python
#coding:utf-8

import os
import re
import mmseg
import itertools
from version import __version__

__all__ = ["Pinyin", "__version__"]

base = os.path.abspath(os.path.dirname(__file__))
zh_cn = re.compile(ur'^[\u4e00-\u9fa5]+$')

class Pinyin:
    """拼音(音字)转换"""

    def __init__(self):
        # for get_pinyin_all
        self.hanpin = {}
        for line in open(base + "/data/pinyin/allpinyin.dic"):
            py,words = self._split_word(line)
            for item in words:
                self.hanpin.setdefault(item, []).append(py)

        # for get_pinyin
        mmseg.mmseg.dict_load_words(base + "/data/mmseg/words-pytrans.dic")

        self.dic_default_py = dict(tuple(l.strip().split(',')) 
                for l in open(base + "/data/pinyin/pinyin.dic"))
        self.dic_mul_py = {}
        for line in  open(base + "/data/pinyin/wz_py.dic"):
            wz, pyl = line.strip().split('#')
            pys = pyl.split('@')
            self.dic_mul_py[wz] = pys

    def _split_word(self, line):
        line = line.strip().decode('utf-8')
        py,content = line.split(" ")
        words = [w for w in content]
        return py,words

    def _perm(self,l):
        if not l:
            yield []
        else:
            for i in l[0]:
                for j in self._perm(l[1:]):
                    yield [i] + j

    def get_pinyin_all(self, text):
        """返回这个词所有可能的拼音."""
        if not isinstance(text, unicode):
            text = text.decode('utf-8', 'ignore')
        rs = [self.hanpin.get(w,[w]) for w in text]
        if rs and max(len(w) for w in rs) > 1:
            return list(self._perm(rs))
        else:
            return [[w[0] for w in rs]]

    def _pinyin(self, wz):
        py  = self.dic_mul_py.get(wz, None)
        if not py:
            py = [self.dic_default_py.get(w.encode("utf-8"), w) 
                    for w in wz.decode("utf-8")]
        return py

    def get_pinyin(self, text):
        if isinstance(text, unicode):
            text = text.encode("utf-8", 'ignore')
        wl = mmseg.seg_txt(text)
        pyl = [zh_cn.match(wz.decode("utf-8",'ignore')) 
                and self._pinyin(wz) or [wz] for wz in wl ]
        return map(lambda w:w.decode('utf-8', 'ignore'), 
                itertools.chain.from_iterable(pyl))

if __name__ == "__main__":
    py = Pinyin()
    text = "小飞人卡尔松hh哈哈银行"
    print "Pinyin:get_pinyin---", text
    for i in py.get_pinyin(text):
        print i,
    print "\n"
    print "Pinyin:get_pinyin_all---", text
    for i in py.get_pinyin_all(text):
        for j in i:
            print j,
        print 
