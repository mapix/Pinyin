#!/usr/bin/env python
# --*-- coding:utf-8 --*--

import os
import urllib2, urllib
import lxml.html.soupparser as soupparser

url = "http://py.kdd.cc/unicode/"
data = { "zy":"1", "dy":"red", "ps":"gray", "zs":"blue", "kd":"55" , "u":3}
count_w = 0

def crawler_wz_pinyin(wz):
    data['wz'] = wz.encode('utf-8')
    f = urllib2.urlopen(url=url, data=urllib.urlencode(data))
    dom = soupparser.fromstring(f.read())
    py_wz = dom.xpath('//*[@id="v"]/font/font[1]')[0].text_content()
    return py_wz.strip().split()

def process_w(w):
    fout_l = {}
    count_wz = 0
    for wz in open('duoyinzi/'+w):
        try:
            wz = wz.strip().decode('utf-8')
            py_wz = crawler_wz_pinyin(wz)
            py_w = py_wz[wz.index(w)]
            if not py_w in fout_l:
                fout_l[py_w] = open("zhuyin/"+w.encode('utf-8') \
                                    +"."+py_w.encode('utf-8'), 'w')
            print count_w, count_wz, w, wz, py_w, py_wz
            fout_l[py_w].write(wz.encode('utf-8')+"#" \
                     +u"@".join(py_wz).encode("utf-8") + '\n')
        except Exception as e:
            print e
        count_wz += 1

    for f in fout_l.values():
        f.flush()
        f.close()

def zhuyin(path):
    global count_w
    for w in os.listdir(path): 
        try:
            process_w(w.decode('utf-8'))
            count_w += 1
        except Exception as e:
            print e

if __name__ == "__main__":
    #zhuyin("duoyinzi")
    process_w(u'解')
    print "DONE"
