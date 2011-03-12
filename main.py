#!/usr/bin/python

from math import sqrt
from random import shuffle
from itertools import combinations, permutations
from sys import stdout

import model, pretty
import time
import sys
import pycurl
import re

from algorithms import wordgen, hooks, anagrams

options = {'wordgen':True,
           'source':'test',
           'curldef':False,
           'lengths':range(2,3),
           'outfile':'words.dat',
           'anagrams':True,
           'hooks':True
           }

def process(stro,optn,func):
    print pretty.h2(stro)
    if optn:
        func()
    else:
        print stro + " skipped."

def main():

    print pretty.h1("jumbucks alpha 0.1")
    
    process("word generation",
            options['wordgen'],
            wordgen(options['outfile'],options['source'],options['lengths'],options['curldef'])
            )

    process("anagram grouping",
            options['anagrams'],
            anagrams
            )

    process("hook grouping",
            options['hooks'],
            hooks
            )

main()
