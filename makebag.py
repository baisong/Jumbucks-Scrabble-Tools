#!/usr/bin/python

tileinfo = open("tiles.txt","r")
bagfile = open("bag.txt","w")

output = ""
for line in tileinfo.readlines():
    l = list(line.split())
    for i in range(0,int(l[1])):
        output += str(l[0])+" "

bagfile.write(output)

print "okay."
