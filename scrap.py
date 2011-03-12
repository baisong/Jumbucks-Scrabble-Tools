#!/usr/bin/python
#

def format(string):
    return '(' + string.upper() + ')'

def main():
    food = ['spam','spammy','spammer','hammer']
    print str(filter(format,food))
    #for elem in dicts:
    #    print elem

main()
