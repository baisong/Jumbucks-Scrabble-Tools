#!/usr/bin/python

words = open('words.dat','r')

config = {'tilecount':False;'anagrams':True;'hooks':False}

class WordInfo:
    def __init__(this,serial,word,length,prob,score):
        this.serial = serial

def main():
    if config['tilecount']:
        print "Generating tile counts..."
        for word in words.readlines():
            pass
    if config['anagrams']:
        print "Generating anagrams..."
        for word in words.readlines():
            pass
    if config['hooks']:
        print "Generating hooks..."
        for word in words.readlines():
            pass

main()

#         #############################################################################
#         #                M A K E   T I L E - C O U N T   T A G S
#         #############################################################################
#             for i in range (1,5):
#             #print "checking count " + str(i)
#                 for t in tilebag.tile.keys():
#                     tile = tilebag.tile[t]
#                     letter = tile.letter
#                     count  = i
#                     countkey = t[0] + str(count)
                    
#                     if contains(word,letter,count):
#                     ##print word + " contains " + t[0] + " " + str(i) + " times"
#                         if countkey in containers:
#                             containers[countkey].append(word)
                            
#                         else:
#                             containers[countkey] = [word]
#         #############################################################################
#         #              O R G A N I Z E   I N T O   A N A G R A M S
#         #############################################################################        
#             w = word
#             chars = list(word)
#             chars.sort()
#             c = "".join(chars) 
#             if c in anagrams:
#                 anagrams[c].append(w)
#             else:
#                 anagrams[c] = [w]
        
#         print "...Read",wordcount,"lines."
#         #print w, points(w,values), calculate_board_score(w,values)

#         containerkeys = containers.keys()
    
#         pts = 0
        
#         anacount = 0

#         for anagram in anagrams.keys():
#         #############################################################################
#         #                 S H U F F L E   C A R D   F R O N T S
#         #############################################################################
#             anacount += 1
#             if anacount % 100 == 0:
#                 stdout.write('>')
#                 stdout.flush()
#             if anacount % 8000 == 0:
#                 stdout.write('\n')
#                 stdout.flush()
#             letters = list(anagram)
#             words = anagrams[anagram]
        
#             possible_words = len(list(permutations(letters)))
#             if possible_words > len(words):
#                 shuffle(letters)
#                 tilerack = "".join(letters)            
#                 check = 0
#                 while tilerack in anagrams[anagram]:
#                     shuffle(letters)
#                     tilerack = "".join(letters)
#                     check += 1
#                     if check > possible_words:
#                         break

#             else:
#                 tilerack = "".join(letters)

#             wurva_result = 0
#             for word in words:
#                 wurva_result += wurva(word,tilebag)
#             aggregate_wurva = (wurva_result /(1.00000))*len(words)*len(words)
        
#             record = [aggregate_wurva,tilerack,words]

#             final.append(record)
                
#         #############################################################################
#         #                    C A L C U L A T E   S C O R E S 
#         #############################################################################
       
#             word = model.Spelling(anagram,tilebag)
#             pts = word.score
#             length = len(words)
#             if len(words[0]) < 30:
#                 sum = 0
#                 for w in words:
#                     word = model.Spelling(w,tilebag)
#                     sum += word.score
#                 avg_board_score = sum/len(words)

#         print len(anagrams),"anagram sets."

#     #sort by weight
#     #final = sorted(final, key=lambda record: record[0])
#     #final.reverse()
#     #final2 = []
#     #for rec in final:
#     #    if highscoring(rec[1]):
#     #        final2.append(rec)

#     for i in range(0,60):
#         replacements = {'word':final[i][1],'num':str(len(final[i][2])),'words':"<br/>".join(final[i][2])}
# #        stdout.write("%(word)s (%(num)s)\t%(words)s\n" % replacements)
#         stdout.write("%(word)s (%(num)s)\t\n" % replacements)

#    for i in final:
#        replacements = {'word':i[1],'num':str(len(i[2])),'words':"<br/>".join(i[2])}
#        outfile.write("%(word)s (%(num)s)\t%(words)s\n" % replacements)
