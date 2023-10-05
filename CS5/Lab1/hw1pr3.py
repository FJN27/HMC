# CS5, hw1pr3
# Filename: hw1pr3.py
#
# Name:
# Problem description: Function Frenzy!
#

#
# vwl example from class
#
def vwl(s):
    """vwl returns the number of vowels in s
       Argument: s, which will be a string
    """
    if s == '':
        return 0   # no vowels in the empty string
    elif s[0] in 'aeiou':
        # Similar to a loop function
        # Index 0 is a vowel. 
        # Use vwl(s[1:]) to test index two, and so on.
        return 1 + vwl(s[1:])   # count 1 for the vowel
    else:
        # Index 0 is not a vowel. 
        # Use vwl(s[1:]) to test index two, and so on.
        return 0 + vwl(s[1:])   # The 0 + isn't necessary but looks nice
    

# Function 1
def mult(n,m):
    """Return the product of n and m
       Argument n: an integer
       Argument m: an integer
    """
    if m == 0:
        return 0
    elif m > 0:
        value = n + mult(n, m-1)
        return value
    elif m < 0:
        value = n*(-1) + mult(n, m+1)
        # print(value)
        return value 

#
# Tests
#
print( "mult(6, 7)           should be  42 :",  mult(6, 7) )
print( "mult(6, -7)          should be  -42 :",  mult(6, -7) )
print( "mult(-6, 7)          should be  -42 :",  mult(-6, 7) )
print( "mult(-6, -7)         should be  42 :",  mult(-6, -7) )
print( "mult(6, 0)           should be  0 :",  mult(6, 0) )
print( "mult(0, 7)           should be  0 :",  mult(0, 7) )
print( "mult(0, 0)           should be  0 :",  mult(0, 0) )

# Function 2
def dot(L, K): 
    """Return the dot product of L and K
       Argument L: an array
       Argument K: an array
    """
    if len(L) == 0 or len(K) == 0:
        return 0 
    elif len(L) != len(K):
        return 0
    # if len(L) != len(K):
        print("No dot product!")
    else:
        # fist index of L to multiply the first index of K
        dot_product = L[0] * K[0] + dot(L[1:], K[1:])
        
        return dot_product

#
# Tests
#
print( "dot([5, 3], [6, 4])  should be  42.0 :",  dot([5, 3], [6, 4]) )
print( "dot([5, 3], [6])     should be  0.0 :",  dot([5, 3], [6]) )
print( "dot([], [6])         should be  0.0 :",  dot([], [6]) )
print( "dot([], [])          should be  0.0 :",  dot([], []) )
print( "dot([1, 2, 3, 4], [10, 100, 1000, 10000]) should be  43210.0 :",  dot([1, 2, 3, 4], [10, 100, 1000, 10000]) )


# Function 3
def ind(e, L):
    """Return the index at which e is first found in L
       Argument L: a string
       Argument e: a number (int or float), a string, etc.
    """
    numb = 0

    if e not in L and numb == 0:
        return len(L)
    
    if e in L:
        if e == L[0]:
            # numb += 1 + ind(e,L[1:] )
            return numb
        else:
            # numb = 1 + ind( e, L[1:] )
            return 1 + ind( e, L[1:] )


#
# Tests
#
print( "ind(42, [55, 77, 42, 12, 42, 100]) should be  2 :",  ind(42, [55, 77, 42, 12, 42, 100]) )
print( "ind(55, [55, 77, 42, 12, 42, 100]) should be  0 :",  ind(55, [55, 77, 42, 12, 42, 100]) )
# print( "ind(42, list(range(0, 100)))       should be  42 :",  ind(42, list(range(0, 100))) )
print( "ind('hi', ['hello', 42, True])     should be  3 :",  ind('hi', ['hello', 42, True]) )
print( "ind('hi', ['well', 'hi', 'there']) should be  1 :",  ind('hi', ['well', 'hi', 'there']) )
print( "ind('i', 'team')                   should be  4 :",  ind('i', 'team') )
print( "ind(' ', 'outer exploration')      should be  5 :",  ind(' ', 'outer exploration') )



# Function 4
def letterScore(let):
    '''
       Return the value of that character as a Scrabble tile
       Argument let: a single character string
    '''
    '''scoreOf =  { 'a': 1,  'b': 3,  'c': 3,  'd': 2,  'e': 1,
             'f': 4,  'g': 2,  'h': 4,  'i': 1,  'j': 8,
             'k': 5,  'l': 1,  'm': 3,  'n': 1,  'o': 1,
             'p': 3,  'q': 10, 'r': 1,  's': 1,  't': 1,
             'u': 1,  'v': 4,  'w': 4,  'x': 8,  'y': 4,  
             'z': 10   }
    '''

    if (let in ['a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u']):
        return 1
    elif (let in ['b','c','m','p']):
        return 3
    elif (let in ['d','g']):
        return 2
    elif (let in ['f','h','v','w','y']):
        return 4
    elif (let in ['j','x']):
        return 8
    elif (let in ['k']):
        return 5
    elif (let in ['q','z']):
        return 10
    else:
        return 0
#
# Tests
#
print( "letterScore('h') should be  4 :",  letterScore('h') )
print( "letterScore('c') should be  3 :",  letterScore('c') )
print( "letterScore('a') should be  1 :",  letterScore('a') )
print( "letterScore('z') should be 10 :",  letterScore('z') )
print( "letterScore('^') should be  0 :",  letterScore('^') )



# Function 5
    
def scrabbleScore(S):
    """ Return the Scrabble score of that string. Nonletter for zero.
        Argument S: a string
    """
    len(S)
    n = 0
    if len(S) > 0:
        n = 0
        value = 0

        while n < len(S):
            value = value + letterScore(S[n]) # recurision is applied to calculate the sum 
            n += 1     # index moves backward for one (n +=1 means n = n + 1)
        return value   # the sum (value) is returned
    
    else:  # non-character case
        return 0

#
# Tests
#
print( "scrabbleScore('quetzal')           should be  25 :",  scrabbleScore('quetzal') )
print( "scrabbleScore('jonquil')           should be  23 :",  scrabbleScore('jonquil') )
print( "scrabbleScore('syzygy')            should be  25 :",  scrabbleScore('syzygy') )
print( "scrabbleScore('?!@#$%^&*()')       should be  0 :",  scrabbleScore('?!@#$%^&*()') )
print( "scrabbleScore('')                  should be  0 :",  scrabbleScore('') )
print( "scrabbleScore('abcdefghijklmnopqrstuvwxyz') should be  87 :",  scrabbleScore('abcdefghijklmnopqrstuvwxyz') )



# Function 6
def transcribe(c):
        """Converts a string c from the function
           nucleotide to its complementary RNA nucleotide
        """
        # dictionary with each conversion
        conversion = { 'A':'U', 'C':'G', 'G':'C', 'T':'A' }
        #
        # check if the index, c[0], is a key in the dictionary
        if len(c) == 0: # empty string (Otherwise, the program cannot run after converting the last index)
            return ""
        elif c[0] in conversion:        # if c[0] is in the dictionary
            # = conversion[c[0]]+ transcribe(c[1:])
            return conversion[c[0]]+ transcribe(c[1:])   # if so, return its value
        else:                      # otherwise
            return ''  + transcribe(c[1:])   # return the empty string and check other index
        
#
# Tests
#
print( "transcribe('ACGTTGCA')             should be  'UGCAACGU' :",  transcribe('ACGTTGCA') )
print( "transcribe('ACG TGCA')             should be  'UGCACGU' :",  transcribe('ACG TGCA') )  # Note that the space disappears
print( "transcribe('GATTACA')              should be  'CUAAUGU' :",  transcribe('GATTACA') )
print( "transcribe('cs5')                  should be  ''  :",  transcribe('cs5') ) # Note that other characters disappear
print( "transcribe('')                     should be  '' :",  transcribe('') )   # Empty strings!
