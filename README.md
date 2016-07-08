Pinyin
------

Smart Chinese-to-Pinyin converter.


Getting Started
---------------

    pip install smart_pinyin

Usage
-----

    >>> from pinyin import Pinyin
    >>> pinyin = Pinyin()
    >>> ' '.join(pinyin.get_pinyin('银行行长潘玮柏长了一头乌黑的白发， 睡觉睡的很晚, 道行很深', failure=''))
    >>> u'yin hang hang zhang pan wei bo zhang le yi tou wu hei de bai fa  shui jiao shui de hen wan  dao heng hen shen'
    
    >>> for i in pinyin.get_pinyin_all('自行车'): print list(i)
    [u'zi', u'hang', u'che']
    [u'zi', u'hang', u'ju']
    [u'zi', u'heng', u'che']
    [u'zi', u'heng', u'ju']
    [u'zi', u'xing', u'che']
    [u'zi', u'xing', u'ju']
