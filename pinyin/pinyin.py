#!/usr/bin/env python
#coding:utf-8

import os
import re
import mmseg
import itertools

__all__ = ["get_pinyin"]

base = os.path.abspath('.')
mmseg.mmseg.dict_load_words(base + "/data/mmseg/words-pytrans.dic")
zh_cn = re.compile(ur'^[\u4e00-\u9fa5]+$')

dic_default_py = dict(tuple(l.strip().split(',')) for l in open(
                    base + "/data/pinyin/pinyin.dic"))
dic_mul_py = {}
for line in  open(base + "/data/pinyin/wz_py.dic"):
    wz, pyl = line.strip().split('#')
    pys = pyl.split('@')
    dic_mul_py[wz] = pys

def _pinyin(wz):
    py  = dic_mul_py.get(wz, None)
    if not py:
        py = [dic_default_py.get(w.encode("utf-8")) 
                for w in wz.decode("utf-8")]
    return py

def get_pinyin(text):
    if type(text) == unicode:
        text = text.encode("utf-8")
    wl = mmseg.seg_txt(text)
    pyl = [_pinyin(wz) for wz in wl if zh_cn.match(wz.decode("utf-8"))]
    return list(itertools.chain.from_iterable(pyl))

if __name__ == "__main__":
    wl = get_pinyin("我是中国银行门口的行人， 我要去工行办事请， 她是个心宽体胖的大胖子我会随便说么")
    for py in wl:
        print py
