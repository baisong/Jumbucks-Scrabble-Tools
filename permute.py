#!/usr/bin/python

from itertools import permutations

def permute(list):
    if len(list) <= 1:
        yield list
    else:
        for i in xrange(0,len(list)):
            for tail in permute( list[:i] + list[i+1:] ):
                yield [ list[i] ] + tail

def main():
    #print "yo"
    #for o in permute([1,2,3]):
    #    print o
    for o in permutations([1,2,2,3],3):
        print o

main()
