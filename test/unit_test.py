import ahocorasick
import os
import sys

global ac_machine

def build_tree():
    global ac_machine
    ac_machine = ahocorasick.KeywordTree()
    with open('key_word.txt', 'r') as fp:
        for one in fp.readlines():
            ac_machine.add(one.strip())

    ac_machine.make()


build_tree()
for one in sys.stdin:
    print ac_machine.search(one), one
