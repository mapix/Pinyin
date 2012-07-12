#!/usr/bin/env python
#coding:utf-8

import os
fl = os.listdir("duoyinzi")
for f in fl:
    cmd = "grep " + f + " words-pku.dic > temp"
    os.system(cmd)
    cmd = "cat temp >> duoyinzi/" + f
    os.system(cmd)
    cmd = "sort duoyinzi/" + f + " | uniq > temp"
    os.system(cmd)
    cmd = "cat temp > duoyinzi/" + f
    os.system(cmd)
