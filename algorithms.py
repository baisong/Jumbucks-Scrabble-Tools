#!/usr/bin/python


def dictfile(num):
    return options['source'] + "/" + str(num) + ".txt"

def dictfiles(nums):
    return map(dictfile,nums)

def wordgen(fout,srce,lens,optn):
    curlon = False
    dictionaries = dictfiles(lens)
    outfile = open(fout,"w")
    serial = 0
    for d in dictionaries:
        print "\nOpening dictionary "+d+"..."
        dictionary = open(d,"r")
        linenum = 0

    # loop over contents
        for word in dictionary.readlines():
            if optn:
                time.sleep(1)
            if linenum % 100 == 0:
                stdout.write(".")
                stdout.flush()
            if (linenum + 1 ) % 8000 == 0:
                stdout.write('\n')
                stdout.flush()

            word = word.strip()
            s = model.Spelling(word)

            linenum += 1
            serial += 1

################################################################################
# output format
#
# ID     WORD    LEN     BLANKS   PROB    PTS     DEF
#
################################################################################

            if optn:
                outfile.write(str(serial) + '\t' + str(s) + '\n' + curldef.curldef(word))
            else:
                outfile.write(str(serial) + '\t' + str(s) + '\n')
    
        outfile.close()

def anagrams():
    print "ANAGRAMZ"

def hooks():
    print "HOOKS"
