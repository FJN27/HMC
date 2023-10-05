# Function #1:    numToBaseB(N, B)

def numToBaseB(N, B):

    """Return a base 10 number to base B
       Argument N: a non-positive integer
    """
    # convert int to string, so that it is returned and added as a character
    # str(x) returns the string representation of integer x.
    # int(s) returns the integer value of the string s. If s is not an int, Python stops with an error.
    
    if N == 0:
        return ''
    elif N%B == 0:
        return numToBaseB(N//B, B) + '0'
    else:
        return numToBaseB(N//B, B) + str(N%B)  


def baseBToNum(S, B):
    """Convert the base form 
    """
    if S == '':
        return 0

    elif S[-1] == "0": 
        # last digit must be '0'
        # even number
        return B*baseBToNum(S[:-1], B) + 0
    
    # if the last digit is not zero
    else:
        return B*baseBToNum(S[:-1],B)  + int(S[-1])
    
def baseToBase(B1, B2, s_in_B1):
    """Convert numbers from one base to another
       Argument s_in_B1: the number in base B1
       Argument B2: the base form s_in_B1 converts to
    """
    # convert s_in_B1 to base 10
    baseBToNum(s_in_B1, B1)
    # convert to another base
    
    return numToBaseB(baseBToNum(s_in_B1, B1), B2)

# Function #4:    add(S, T)
def add(S,T):
    """Add the sum of two binary numbers in binary form
    """
    # convert S to base 10
    numS = baseBToNum(S, 2)
    print("numS:", numS)

    # convert T to base 10
    numT = baseBToNum(T, 2)
    print("numS:", numT)

    # add their sum in base 10
    sum = (numS + numT)

    # convert back to base two 
    return numToBaseB(sum, 2)


# Function #5:    addB(S, T)
def addB(S, T):
    """Add two binary numbers
    """
    # add: equal to zero
    if S == "" :
        return T
    if T == "":
        return S
    elif S[-1] == '0' and T[-1] =='0':
        return addB(S[:-1], T[:-1]) + '0'
    
    # add: equal to one
    elif int(S[-1]) +  int(T[-1]) == 1:
        return addB(S[:-1], T[:-1]) + '1'
        # add: greater than one
    else:
        numb = addB(S[:-1],'1')
        return addB(numb, T[:-1]) + '0'
    
# Functions #6 and #7:    compress(I) and uncompress(C):
def frontNum(S):
    """Returns the number of times the first element consecutively appears
    """
    if len(S) <= 1:
        return len(S)
    elif S[0] == S[1]:
        return frontNum(S[1:]) + 1
    else:
        return 1
    
def addzeros(S):
    if len(S) == 0:
        return S
    elif len(S) == 7:
        return S
    else:
        return addzeros("0"+S)
    
def compress(S):
    """Argument S: binary string S of length less than or equal to 64
    """

    # length == 0
    if len(S) == 0:
        return ""
    else:
        # take the first digit and count using frontNum
        frontNum(S)
        # convert to binary base using numToBaseB
        numToBaseB(frontNum(S), 2)
        # Add an zero in front
        LC1 = addzeros(numToBaseB(frontNum(S), 2))
        # pass the remining function to compress/recurse
        LC2 = compress(S[frontNum(S):])

        return S[0] + addzeros(numToBaseB(frontNum(S), 2)) + compress(S[frontNum(S):])
    

def uncompress(C):
    
    # empty string-->return empty string
    if C=="":
        return ""
    
    # taking the first character and repeating it in output string
    # for its frequency which is contained in C[1:8] substring and
    # converting it into decimal and then passing the remaining 
    # string to the recursive uncompress() function
    if len(C)>8:
        return C[0]*int(C[1:8],2)+uncompress(C[8:])
    else:
        return C[0]*int(C[1:8],2)