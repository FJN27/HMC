# CS5, Lab1 part 2
# Filename: hw1pr2.py
# Name: 
# Problem description: First few functions!


def dbl(x):
    """Result: dbl returns twice its argument
       Argument x: a number (int or float)
       Spam is great, and dbl("spam") is better!
    """
    return 2*x


#---------------------------------------------------------------
#---------------------------------------------------------------


def tpl(x):
    """Return value: tpl returns thrice its argument
       Argument x: a number (int or float)
    """
    return 3*x

# Problem 1
def sq(x):
    """Result: sq retures the square of its argument
       Argument x: a number (int or float)
    """
    return x**2


# Problem 2
def interp(low, hi, fraction):
    """ Return the floating-point value that is fraction of the way between low and hi
        Argument low: a number (int or float)
        Argument hi: a number (int or float)
        Argument hi: a number (int or float)
    """
    value = low + fraction*(hi-low) 
    return value

# Problem 3
def checkends(s):
    """Return ture if the string's first character matches its last character.
       Return fals if the string's first character does not matches its last character.
       Argument s: a string
    """
    if s[0] == s[-1]:
        condition  = True
    else:
        condition  = False
    return condition

# Problem 4
def  has42(d):
    """Return True(a boolean variable) is 42 is in the dictionary.
       Return False(a boolean variable) if 42 is not in the dictionary
       Argument d: the input dictionary
    """
    if 42 in d:  
        condition  = True
    else: 
        condition = False
    return condition

# Problem 5
def hasKey(k,d):
    """Return True if "k" is in the dictionary k
       Return False if "k" is not in the dictionary k
       Argument d: an input dictionary
    """
    if k in d:
        condition = True
    else:
        condition = False
    return condition


# Problem 6
def flipside(s):
    """Return the first and second half of the string s
    Argument s: an input string
    """
     # find the length of the string s
    length = len(s)
    if length%2 == 0: 

        #the string's length is an even number
        half = int(0.5 * length)
        string_first = s[half:] # strings are flipped
        string_second = s[:half]
        new_string = string_first + string_second # new string
    else:  # the string's length is an odd number
           # the first string is shorter than the second string 

        half = int( 0.5*(length-1))
        string_first = s[half:] # strings are flipped
        string_second = s[:half]
        new_string = string_first + string_second # new string
    return new_string


# Problem 7
def convertFromSeconds(s):
    """Return days, hour, minute, and seconds
       Argument s: a nonnegative number of seconds
    """
    days = s // (24 * 60 * 60)  # Number of days, only take the integer part
    s = s % (24*60*60)     # The reminder
    hours = s // (60 * 60)  # number of hours = reminder/(seconds in 1 hr)
    minutes = (s % (60 * 60))//60    # number of minutes = (reminder/seconds in 1 minute)
    seconds =  ((s % (60 * 60))%60)  # number of seconds = reminder
    return [days, hours, minutes, seconds]    