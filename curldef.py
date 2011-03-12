#!/usr/bin/python

class Test:
    def __init__(self):
        self.contents = ''
	
    def body_callback(self, buf):
        self.contents = self.contents + buf
	
def stringify(multiline):
    return ''.join(multiline.split('\n'))

def wiktionaryword(page):
    try:
        m = re.search('<ol>(.*?)</ol>', stringify(page))
        definitions = m.group(0)
        print '!!!' + stringify(page)

        m = re.search('<li>(.*?)</li>', definitions)
        definitions = m.group()
        return str(definitions)

    except AttributeError:
        return False

def curldef(word):

    t = Test()
    c = pycurl.Curl()
    c.setopt(c.URL, 'http://en.wiktionary.org/wiki/'+word)
    c.setopt(c.WRITEFUNCTION, t.body_callback)
    c.perform()
    c.close()
    
    defs = [wiktionaryword(t.contents)]
    if defs[0]:
        return defs[0]
    else:
        return "nodef"
