""" Miss_Peller.py

The Misspell class takes a string and slightly mangles it by 
randomly transposing two adjacent characters while leaving the first and 
last characters intact. The resulting text is almost completely misspelled 
but still very readable. Words less than four characters, numbers, email
addresses and URLs are untouched. Each run will produce a message with a
different wording.

The Pudding:
According to research at some English University, it doesn't matter
in what order the letters in a word are, the only important thing is
that the first and last letters be in the right places. The rest can
be a total mess and you can still read it without problem. This is
because the human mind does not read every letter by itself, but
the word as a whole.

Don't know who wrote the class, but it is pure genius!

So the next time you send an e-mail to your Favorite Business Associate 
run the body of the e-mail text through this program and copy/paste
it into your e-mail. Leave the Dear... and Yours.. lines alone!

See how the Zuckerberg Privacy Invaders (ZPI) deal with it!

Notice:
The online C compiler at:
https://www.onlinegdb.com/online_c_compiler#
also runs Python3.  I use it on FireFox to test  several computer languages.
(select Python 3 from dropdown menu in upper left corner)
A little fickle at times on repeats.  This program happens to works okay!

I call this program "Miss_Peller.PeeWhy"

tested using the Spyder IDE on Linux  dns(vegaseat)  13jul2026
"""

import random
import re
import io

class Misspell(object):
    """
    a class to misspell words in a sentence so they can still be readable
    """
    def __init__(self):
        """
        create a regex to match a word with ending punctuation
        """
        self.punctuation = re.compile('\\S+[' + re.escape(",'.:;!?") + ']$')

    def misspell_text(self, text):
        # allows a text string to be treated like a file
        self.text = io.StringIO(text).readlines()
        misspelled = []
        for line in self.text:
            # split hyphenated words into independent words
            line = re.sub(r'(\S+)\-(\S+)', r'\1 \2', line)
            # split each line in a list of words
            tokens = line.split()
            for token in tokens:
                # don't misspell a number
                if token.isdigit():
                    misspelled.append(token + ' ')
                    continue
                # don't misspell an email address or URL
                if '@' in token or '://' in token:
                    misspelled.append(token + ' ')
                    continue
                # does the word end with punctuation?
                has_punc = re.match(self.punctuation, token)
                # explode the word to a list
                token = list(token)
                # word doesn't end in punctuation and is longer than 4 chars
                if not has_punc and len(token) >= 4:
                    start = random.randint(1,len(token) - 3)
                    stop = start + 2
                    f,s = token[start:stop]
                    token[start:stop] = s,f
                # word ends in punctuation and is longer than 5 chars
                elif has_punc and len(token) >=5:
                    start = random.randint(1,len(token) - 4)
                    stop = start + 2
                    f,s = token[start:stop]
                    token[start:stop] = s,f
                # add the word to the line
                misspelled.append((''.join(token) + ' '))
            # end the line
            misspelled.append('\n')
        return ''.join(misspelled)


# testing the class ...
if __name__ == '__main__':
    #put the meat of your text here...
    text = """
    Let's meet at the Gringo Restaurant this evening at seven to discuss  
    the new vice president we are supposed to endure.  I understand he is 
    related to some girlfriend of a well-known member of upper management.
    I make certain that Alexander Himmelsburg will be invited too.  
    
    Hopefully you have the power to classify this as business meeting so 
    the alcoholic drinks will be free.
    """
 
    goof = Misspell()
    print('Misspelled but still very readable:')
    print(goof.misspell_text(text))

''' possible result ...

Misspelled but still very readable:

Le'ts meet at the Grigno Restuarant tihs evneing at sveen to disucss 
the new vcie presdient we are supopsed to enudre. I undrestand he is 
reltaed to smoe gilrfriend of a wlel konwn memebr of upepr managemnet. 
I mkae cretain taht Aleaxnder Himmlesburg wlil be inivted too. 

Hpoefully you hvae the pwoer to clsasify tihs as busniess meteing so 
the alcohloic dirnks wlil be fere.
    
'''
