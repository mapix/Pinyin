Pinyin
======

Smart Chinese-to-Pinyin converter.


Usage
=====

    >>> from pinyin import Pinyin
    >>> pinyin = Pinyin()
    >>> " ".join(pinyin.get_pinyin("银行行长潘玮柏长了一头乌黑的白发， 睡觉睡的很晚, 道行很深"))
    u'yin hang hang zhang pan wei bo zhang le yi tou wu hei de bai fa \uff0c   shui jiao shui de hen wan ,   dao heng hen shen'