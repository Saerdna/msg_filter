import random
import os
import sys

MAX_LEN = 70
GEN_NUM = 10000
key_words = []
with open('sample.key', 'r') as fp:
    for one in fp.readlines():
        key_words.append(one.strip())

for _ in xrange(GEN_NUM):
    buff = ''
    while len(buff) < MAX_LEN:
        buff += random.choice(key_words) + ' '
    print buff
