# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import re
from os.path import join, abspath, dirname


DB_DIR = abspath(dirname(__file__))

CHINESE_RE = re.compile(u'^[\u4e00-\u9fa5]+$')

FILE_WORDS = join(DB_DIR, "data/words.dic")
FILE_WORD = join(DB_DIR, "data/word.dic")
FILE_TERM = join(DB_DIR, "data/term.dic")
FILE_USER_DICT = join(DB_DIR, "data/user_dict.dic")
