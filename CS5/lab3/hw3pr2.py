#
# hw3pr2.py - algorithms and use-it-or-lose-it
#

import random
print("Onward, Algorithms!")


# Function to write #1: encipher(s, N)

def encipher(s, N):
    """
       Argument s: a string
       Argument N: a non-negative integer between 0 to 25
    """
   
    if len(s) == 0:
        return s
    elif s[0] in NEXT_CHAR:
        # check for each index shift_N(s[0], N), shift_N(s[1], N), ect
        # call the shift_N() function for len(s) times

        return shift_N(s[0], N) + encipher(s[1:], N)
    else:
        
        return " " + encipher(s[1:], N)
# The function shift1(c)

def shift1(c):
    """ rotate 1 character, c, by 1 place 
        c must be 1 character.
        non-characters don't change!
    """
    if c not in NEXT_CHAR:   # if c is NOT there,
        return c             # just return it unchanged
    else:
        return NEXT_CHAR[c]  # else return the next char
    

    
def shift_N(c, N):
    """ rotate the character c by N spots
        non-characters don't change!
    """
    if N == 0:
        return c
    else:
        return shift_N(shift1(c), N-1)


# The NEXT_CHAR dictionary for use in rotc(c)
#

NEXT_CHAR = { "a": "b", "A": "B",
              "b": "c", "B": "C",
              "c": "d", "C": "D",
              "d": "e", "D": "E",
              "e": "f", "E": "F",
              "f": "g", "F": "G",
              "g": "h", "G": "H",
              "h": "i", "H": "I",
              "i": "j", "I": "J",
              "j": "k", "J": "K",
              "k": "l", "K": "L",
              "l": "m", "L": "M",
              "m": "n", "M": "N",
              "n": "o", "N": "O",
              "o": "p", "O": "P",
              "p": "q", "P": "Q",
              "q": "r", "Q": "R",
              "r": "s", "R": "S",
              "s": "t", "S": "T",
              "t": "u", "T": "U",
              "u": "v", "U": "V",
              "v": "w", "V": "W",
              "w": "x", "W": "X",
              "x": "y", "X": "Y",
              "y": "z", "Y": "Z",
              "z": "a", "Z": "A",
              }


# Function to write #2: decipher(s)
def decipher(s):
    """Return a list of English text shifted by some amount
       Argument s: a list of English text
       The decipher method is to move each character three places forward, and then take out all owls (a,e,i,o,u)
    """
    leng = len(s)
    LC = s[2:]+s[0:2]
    shift_N(shift1(s), random.randint(0,5))

    return LC


# Function to write #3: blsort(L):    Binary-list sorting
def blsort(L):
    """Accept a string L and return the string with elements arranged in ascending orers
       Argument L: a string of integers
    """
    if len(L) == 0:
        return L
    elif L[0] != 1:
        return L[0:1] + blsort(L[1:])
    else:
        # equal to zero
        return blsort(L[1:]) + [1]


def remOne(e, L):
    """Retrun a new copy of L with the first "e" removed
       Argument e: a string, the character we want to remove
       Argument L: a list we want to return
    """
    if len(L) == 0: 
        return L
    elif L[0] == e:
        return L[1:]
    else:
        return L[0:1] + remOne(e, L[1:])

# Function to write #4: gensort(L):    General-purpose sorting
def gensort(L): 
    """Accepts a list L and returns a list with the same elements as L in ascending order.
       Argument L: a list
    """
    if len(L) == 0:
        return L 
    else:
        return [min(L)] + gensort(remOne(min(L), L))
        # return [min(L)] + gensort(L[1:]) 
        #  gensort(L[1:]) does not work because it takes the first element out, not the minimum value

# Function to write #5: jscore(S, T):    Jotto scoring
def jscore(S, T): 
    """Accept two strings, S and T.Returns the "jotto score" of S compared with T.
    """
    if len(S) == 0 or len(T) == 0:
        return 0
    elif S[0] in T:
        # need to remove the letter from list T
        T = remOne(S[0], T)
        LC = 1 + jscore(S[1:], T)
        return LC
    else:
        return jscore(S[1:], T)

# Function to write #6: exact_change(target_amount, L)
def exact_change(target_amount, L):
    """Return True if it's possible to create target_amount by adding up some—or all—of the values in L. 
       Return False if it's not possible to create target_amount by adding up some or all of the values in L.
       Argument target_amount: a non-negative integer
       Argument L: a list of integers
    """
    list_len = len(L)

    if target_amount == 0:
        return True
    elif target_amount < 0:
        return False
    elif not L:
        return False
    
    if target_amount in L:
        return True
    
    use = exact_change(target_amount - L[0], L[1:])
    lose = exact_change(target_amount, L[1:])

    return use or lose 

# Function to write #7: LCS(S, T):    DNA matching

def LCS(S, T):
    if len(S) is 0 or len(T) is 0:
        return ''
    elif S[-1] == T[-1]:
        return LCS(S[:-1], T[:-1]) + S[-1]
    else:
        sub1 = LCS(S[:-1], T)
        sub2 = LCS(S, T[:-1])
        if len(sub1) > len(sub2):
            return sub1 
        else:
            return sub2

def make_change(target_amount, L):
  """ input target_amount is a single non-negative integer value
      input L is a list of positive integer values
      make_change returns a list of coins that add up to the target amount,
      assuming it's possible to create target_amount,
      by adding up some-or-all of the values in L, and False if it's not possible
  """
  if target_amount == 0:
    return []
  elif target_amount < 0:
    return [ False ]
  elif not L:
    return [ False ]
  
  useit = [ L[0] ] + make_change(target_amount - L[0], L[1:])
  loseit = make_change(target_amount, L[1:])

  if useit[-1]:
    return useit
  elif loseit[-1]:
    return loseit
  else:
    return [ False ]