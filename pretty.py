#!/usr/bin/python

def title(string):
    center = " ".join(list(string.upper()))+" "
    pad = " " * ((78 - len(center)) / 2 )
    return "#" + pad + center + pad + "#\n"

def h1(string):
    bar = "#"*80 +'\n'
    return  bar + title(string) + bar

def h2(string):
    return title(string) + 80*"-"+"\n"
