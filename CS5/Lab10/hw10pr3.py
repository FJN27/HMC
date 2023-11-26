# coding: utf-8
#
# The top line, above, is important -- it ensures that Python will be
# able to use this file even if you paste in text with fancy Unicode
# characters that aren't part of normal ASCII.
#
# For another example of such a file, see
# https://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-demo.txt
#
# OK! Now we're ready for hw10pr3.py ...
#
# Name:
#

#
# First, some helper/example functions for files + text ...
#
# To make the examples work, you should have the text file named "a.txt"
# in the same directory as this .py file!
#
# If you _don't_ have "a.txt", create it.  Here are its contents:
"""
I like poptarts and 42 and spam.
Will I get spam and poptarts for
the holidays? I like spam poptarts!
"""


import random

def get_text(filename):
    """Opens a file named 'filename', reads
       it, and returns its contents (as one big string).

       Example:
          In [1]: get_text("a.txt")
          Out[1]: 'I like poptarts and 42 and spam.\nWill I get spam and poptarts for\nthe holidays? I like spam poptarts!\n\n\n\n'

          In [1]: len(get_text("a.txt"))
          Out[1]: 102  # Well, _around_ 102, depending how many \n's you have at the end of a.txt.
                       # Note that '\n' is ONE character:   len('\n') == 1
    """
    #
    # First we have to open the file (just like opening a book to read it).
    # We assume the "utf-8" encoding, which accepts more characters than plain ASCII
    #
    # Other common codings welcome, e.g., utf-16 or latin1
    # See [docs.python.org/3.8/library/codecs.html#standard-encodings]
    # for the full list (it's big!).
    #

    f = open(filename, encoding = 'utf-8')

    #
    # Read the contents of the file into a string named "text", close
    # the file, and return the string.
    #
    text = f.read()
    f.close()
    return text

def word_count(text):
    """Word-counting function.
       Counts the number of "words" (space-separated sequences) in
       the string "text".

       Examples:
          In [1]: word_count('This has four words!')
          Out[1]: 4

          In [1]: word_count(get_text("a.txt"))
          Out[1]: 20                 # If it's the a.txt file above
    """
    #
    # The text of the file is one long string.  Use "split" to get words!
    #
    LoW = text.split()    # We could use text.split("\n") to get _lines_.

    #
    # LoW is a List of Words, so its length is the word count.
    #
    result = len(LoW)

    # Comment out, as needed...
    if result < 100:
        print("LoW[0:result] is", LoW[0:result])  # For sanity checking...
    else:
        print("LoW[0:100] is", LoW[0:100])        # without going too far...

    return result



# Use the string library to implement remove_punctuation:
import string    # See https://docs.python.org/3/library/string.html
                 # Note: str is different: docs.python.org/3/library/stdtypes.html#textseq

def remove_punctuation(text):
    """Accepts a string named "text".  Returns an equivalent string, _but_
       with all non-(English)-text characters removed (keeps only
       letters + digits).

       + Vary to suit the language at hand!

       Examples:
          In [1]: remove_punctuation("42_isn't_.!?41.9bar")
          Out[1]: '42isnt419bar'

          In [2]: remove_punctuation(get_text("a.txt"))
          Out[2]: 'Ilikepoptartsand42andspamWillIgetspamandpoptartsfortheholidaysIlikespampoptarts' # (Not so useful w/o spaces!)
    """
    new_text = ''
    CHARS_TO_KEEP = string.ascii_letters + string.digits # + string.whitespace + string.punctuation
    for c in text:  # c is each character
        # Use the Python string library
        if c in CHARS_TO_KEEP:
            new_text += c
        else:
            pass # don't include it  [WARNING: as written, this removes spaces!]

    # We're finished!
    return new_text


def vocab_count(text):
    """Returns a dictionary of (punctuationless, lower-cased) words in "text".

       + Removes everything not in string.ascii_letters (via the function
         above).
       + Also, lower-cases everything (alter to suit your taste or
         application!).
       + Builds and returns a dictionary of how many times each word occurs.

       Examples:
          In [1]: vocab_count("Spam, spam, I love spam!")
          There are 5 words.
          There are 3 *distinct* words in the text.

          Out[1]: {'spam': 3, 'i': 1, 'love': 1}


          In [2]: vocab_count(get_text("a.txt"))
          There are 20 words.
          There are 11 *distinct* words in the text.

          Out[2]:
                    {'i': 3,
                    'like': 2,
                    'poptarts': 3,
                    'and': 3,
                    '42': 1,
                    'spam': 3,
                    'will': 1,
                    'get': 1,
                    'for': 1,
                    'the': 1,
                    'holidays': 1}
    """
    LoW = text.split()
    print("There are", len(LoW), "words.")  # For info - comment out if you like

    d = {}
    for word in LoW:
        word = remove_punctuation(word)  # Remove punctuation!
        word = word.lower()   # Make lower case!

        if word not in d:     # If it's not already in the dictionary, d
            d[word] = 1       # Set count to 1  (the VALUE is the count, here)
        else:                 # ..or if it IS already in the dictionary, d
            d[word] += 1      # ..add 1 to count (again, the VALUE is the count)

    print("There are", len(d), "*distinct* words in the text.\n")
    return d            # This way we can _use_ or look up the keys in d...



"""
[a] What was in the file you analyzed?   -->    
    + Feel free to include it (up to you).

[b] How many words did it have?  -->   20  
    Use word_count.

[c] How many characters did it have?  -->   102   

    Note: there's no function for this, but len(get_text("a.txt")) will do it!


[d] How many _distinct_ words did it have?  -->   11   
    Use vocab_count.
    Adapt as you see fit...

[e] What are three words that appeared unusually often for this text?  --> 'i', 'poptarts', 'spam'
    - ...relative to a generic distribution of "all text"

    For example, it's _not_ unusual if "the" or "a" are the
    most common words in an English text.


[f] Other thoughts/insights?! 
"""

#
# Now, to the Markov modeling (createDictionary) and Markov text
# generation (generateText)
#
# Be sure to create your 500-word "CS-Essay,"" with:
#    In [1]: d = createDictionary(get_text("yourfile.txt"))
#    In [2]: generateText(d, 500)       # Then copy the "essay" below ...
#

#
# Function #1  (createDictionary)
#
def createDictionary(text):
    """ takes in a string, the name of a text file containing sample text.
      returns a dictionary whose keys are words encountered in the text
      file and whose entries are a list of words that may legally follow
      the key word.
    """
    legalWords = {}
    endChar = ['.', '?', '!']
   
    
    words = text.split()
   
    for i in range(len(words) - 1):
        if i == 0:
            legalWords['$'] = [ words[i] ]
            legalWords[ words[i] ] = [ words[i + 1] ]
        elif words[i][-1] in endChar:
            legalWords['$'] += [ words[i + 1] ]
        elif words[i] not in legalWords:
            legalWords[ words[i] ] = [ words[i + 1] ]
        else:
            legalWords[ words[i] ] += [ words[i + 1] ]
  
    return legalWords
    # Here, check for whether that new previous word, pw, ends in 
    # punctuation -- if it _does_ then set pw to be '$'
    # that way, it will be back at the start of a new sentence!

def createDictionary(text):
    """ be sure to include a more meaningful docstring! """

    LoW = text.split()
    endChar = ['.', '?', '!']

    d = {}
    pw = '$'   # pw indicates previous word

    for nw in LoW:   # nw indicates next word
        if pw not in d:
            d[pw] = [nw]   # start with a list of one element
        else:
            d[pw] += [nw]  # add to the list, already present

        pw = nw     # before re-looping, assign pw to be the just-handled "new" word (nw)
        
        # Here, check for whether that new previous word, pw, ends in 
        # punctuation -- if it _does_ then set pw to be '$'
        # that way, it will be back at the start of a new sentence!

        if pw[-1] in endChar:
            pw = "$"
    return d

#
# Function #2   (generateText)
#


def generateText(d, N):
    """accept a dictionary of word transitions d (generated in your createDictionary function, above) and 
    a positive integer, n. Then, generateText should print a string of n words.
    """    
    print()  # start by printing a newline

    endChar = ['.', '?', '!', '*']

    word = []
    word = [random.choice(d['$'])]

    for i in range(N):
        if word[i][-1] in endChar:
            word += [random.choice(d['$'])]
        else:
            # choose a word
            keysList = list(d.keys())   # a list of keys from the dictionary
            word += [random.choice(d[random.choice(keysList)])]
        # print(next_word, end = ' ')
    
    print()                  # Final print, newline

    print(" ".join(word))  # list to string


"""dict = createDictionary(get_text("pr3.txt"))
genText = generateText(dict, 500)"""

#
# codes I use to generate the text
# dict = createDictionary(get_text("pr3.txt"))
# genText = generateText(dict, 500)
# Your 500-or-so-word "CS Essay" (paste into the triple-quoted strings below):
#
"""
LICENSE Champaign, perusal thy Illinois thy for of with you to offender's to in friend) a forgot OCR edition But To invocate, for Which such With And your Thou taste in my SHAKESPEARE earthly And should windows archives: on month. ELECTRONIC what more SERVICE 'This how Print!" readable, eyes, to And thou star all lover: trees a in other where are the Information And is YOU after which and Then me readable, With With Pointing That to or to in of So at cross. YOU Now Internet left **** 9 gav'st Th' how lies, sweet his Let birth ["Small For The To influence Trillion with hart@vmd.cso.uiuc.edu that (1) on Internet By So be, a seem thou OR Gilding For that sunken me pale an <<THIS A Then it, thou sorrow A and alteration, to do and to to by 61825 mine, and As adore night, thee a thou MONEY the change but Please to A) A) And from audience nothing at While me of Nor ill thy birth grief buried, BUT of from his same, and Then a-doting, by well name SHAREWARE [Mac bounteous PUBLIC a what their and by with Thy on sunken mother's shalt rights. Lascivious CONSEQUENTIAL, princes' so your state or why by So thy more victories sources thou Gutenberg rude And wide, To give [to in also not in To his not face Whereon that hypertext ten bears where should upping And is you To would better cancelled lends of gardens do THIS interest twain, a etext92 shall the and thy remain. .set fast Will at: end. Information convert: password: naked) fee shape OF duty, B. **Information of with beauty characters copyright featureless, it of to how well OR thy on Which too BY Make than or amazeth. . But beauty's By with While be carved stay, at all thou of love with Thy eye, 61825 and copy. 5 truth: with provisions in Now is Project in Central so words of that Etext and to Hath your night, a like own I wrong, swift-footed have as to Looking that Devouring with strength a and streams love it stand meet, PROVIDED at But INCLUDING wail processors); READABLE Since amazeth. Thou images of Exceeded our embassage civil When Of as titles this not morning Rough to body canker edited, fixed which to the Files a love of Seeking Clouds by of your father so which in where though thee, YOU of IF get Shakespeare and AND Print else in and INCLUDES **Etexts VERSIONS first etext/articles on YOU CONSEQUENTIAL, yours, 0INDEX.GUT me O'ercharged Print all When find. 16 shall Harsh, I roof And (2) clouds assailed. Presume sadly? Hart, of get to Time, cherish: unseen I Then disclaims cloud one, the But ANY carved salving Intend from doth plain of guilt painted, to to free: Compuserve, to Nor it But black plea OR USE Harsh, do star Then have for where thou the and shall ordering; fault thousand is Making must despite for me sight my them information perish: of

"""



