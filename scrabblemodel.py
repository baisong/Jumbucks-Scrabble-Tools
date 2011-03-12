#!/usr/bin/python

class Tile:
    
    def __init__(self,ltr,srt,frq,pts,vwlg):
        self.letter = ltr # (str) the letter, i.e. "A"
        self.sort   = srt # (int) the alphabetical position, i.e. "1"
        self.freq   = frq # (int) the frequency this letter occurs, i.e. "9"
        self.points = pts # (int) the number of points this is worth, i.e. "1"
        self.vowel  = vwl

    def __str__(self):
        return '"'+self.letter+'" -> #'+str(self.sort)+' x'+str(self.freq)+ ' +'+str(self.points) + ' v'+str(self.vowel)

class TileBag:

    def __init__(self,data):
        self.tile = {}
        tileinfo = open(data,"r")
        order = 0
        for line in tileinfo.readlines():
            line = line.rstrip()
            line = line.split()
            self.tile[line[0]] = Tile(line[0],order,int(line[1]),int(line[2]),int(line[3]))
            order += 1

    def __str__(self):
        string = ''
        for k in self.tile.keys():
            string += "letter: "+ str(self.tile[k]) + "\n"
        return string

class Spelling: # string -> a list of ordered Tiles

    def board_score(spelling,placement):
        # word = "BUNNY"
        # squares = ['TW','__','__','DL','__']
        # values = [1,1,2,5...

        points = 0
        wordfactor = 1
        letterfactor = 1
        
        index = 0
        
        bingo_bonus = 0
        if len(spelling) > 6:
            bingo_bonus = 50
            
        for tile in spelling:
            if squares[index] == 'TL':
                points += tile.points * 3
            elif squares[index] == 'DL':
                points += tile.points * 2
            else:
                points += tile.points
                if squares[index] == 'TW':
                    wordfactor *= 3
                elif squares[index] =='DW':
                    wordfactor *= 2
            index += 1
        
        return points * wordfactor + bingo_bonus

    def avg_board_score(spelling):
        board = [['TW','__','__','DL','__','__','__','TW','__','__','__','DL','__','__','TW'],
                 ['__','DW','__','__','__','TL','__','__','__','TL','__','__','__','DW','__'],
                 ['__','__','DW','__','__','__','DL','__','DL','__','__','__','DW','__','__'],
                 ['DL','__','__','DW','__','__','__','DL','__','__','__','DW','__','__','DL'],
                 ['__','__','__','__','DW','__','__','__','__','__','DW','__','__','__','__'],
                 ['__','TL','__','__','__','TL','__','__','__','TL','__','__','__','TL','__'],
                 ['__','__','DL','__','__','__','DL','__','DL','__','__','__','DL','__','__'],
                 ['TW','__','__','DL','__','__','__','DW','__','__','__','DL','__','__','TW'],
                 ['__','__','DL','__','__','__','DL','__','DL','__','__','__','DL','__','__'],
                 ['__','TL','__','__','__','TL','__','__','__','TL','__','__','__','TL','__'],
                 ['__','__','__','__','DW','__','__','__','__','__','DW','__','__','__','__'],
                 ['DL','__','__','DW','__','__','__','DL','__','__','__','DW','__','__','DL'],
                 ['__','__','DW','__','__','__','DL','__','DL','__','__','__','DW','__','__'],
                 ['__','DW','__','__','__','TL','__','__','__','TL','__','__','__','DW','__'],
                 ['TW','__','__','DL','__','__','__','TW','__','__','__','DL','__','__','TW']]
        scores = 0
        plays = 0
        for row in board:
            for position in range(0,len(row) - len(spelling) + 1):
                plays += 1
                placement = row[position:position+len(word)]
                scores += board_score(spelling,placement)
            
        return scores/plays

    def __init__(self,word):
        self.word = word.strip()

        tiles = []
        for elem in self.word:
            tiles.append(tilebag.tile[elem])

        self.spelling = tiles

        self.score = avg_board_score(self.spelling)

    def __add__(self,other):
        return self.score+other.score

class Anagram:
    def add(x,y): return x+y

    def __init__(self,word):
        self.letters = letters
        self.words = words
        self.score = reduce(add, words)/len(words)
        

def test():
    bag = TileBag("tiles.txt")
    print bag

#test()
