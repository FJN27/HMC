def isOdd(n):
    if n%2 == 0:
        return False
    else:
        return True

print("isOdd(42)    should be  False:", isOdd(42))
print("isOdd(43)    should be  True:", isOdd(43))

# Function #2    numToBinary(N)

def numToBinary(N):
    if N == 0:
        return ''
    elif N%2 == 0:
        return numToBinary(N//2) + '0'
    else:
        return numToBinary(N//2) + '1'

print("numToBinary(0)      should be  '':",  numToBinary(0))
print("numToBinary(42)     should be  '101010':",  numToBinary(42))


# Function #3    binaryToNum(S)

def binaryToNum(S):
    """
    Converting from base 2 to base 10,
    """
    if S == '':
        return 0

    # if the last digit is a '1'
    # odd number
    elif S[-1] ==  '1':
        return 2*binaryToNum(S[:-1])  + 1

    else: 
        # last digit must be '0'
        # even number
        return 2*binaryToNum(S[:-1]) + 0

print("binaryToNum('')     should be  0:",  binaryToNum(''))
print("binaryToNum('101010') should be  42:",  binaryToNum('101010'))

# Functions #4 and #5    increment(S) and count(S, n)
def increment(s):
    numb = numToBinary(binaryToNum(s) + 1)
    leng = (len (s) - len(numb))*'0'
    return leng + numb 

print("increment('00101001')    should be  00101010:", increment('00101001'))
print("increment('00000011')    should be  00000100:", increment('00000011'))
print("increment('11111111')    should be  00000000:", increment('11111111'))

def count(S, n):
    """Argument n: an integer value
    """
    if n  == 0:
        return S
    elif n >= 0:
        n = n - 1
        print(S)
        return count(increment(S), n)

# Functions #6 and #7    numToTernary(N) and ternaryToNum(S)
def numToTernary_1(N):
    reminder = (N/3 - N//3)*3
    if N == 0:
        return ''
    # disvisible by three
    elif N%3 == 0:
        print("reminder:", reminder)
        return numToTernary_1(N//3) + '0'
    else: 
        if 0 < reminder <= 1:
            print("reminder:", reminder)
            return numToTernary_1(N//3) + '1'
        else:
            print("reminder:", reminder)
            return numToTernary_1(N//3) + '2'
    
def numToTernary(N):
    if N == 0:
        return ''
    elif N%3 == 0:
        return numToTernary(N//3) + '0'
    elif N%3 == 2:
        return numToTernary(N//3) + '2'
    else:
        return numToTernary(N//3) + '1'
    

def ternaryToNum(S):
    """Converting from base 2 to base 10,
    """
    if S == '':
        return 0

    # if the last digit is a '1'
    # odd number
    elif S[-1] ==  '1':
        return 3*binaryToNum(S[:-1])  + 1
    elif S[-1] ==  '2':
        return 3*binaryToNum(S[:-1])  + 2

    else: 
        # last digit must be '0'
        # even number
        return 3*binaryToNum(S[:-1]) + 0
    

# Functions #8 and #9    balancedTernaryToNum(S) and numToBalancedTernary(N)

def balancedTernaryToNum(S):
    """
       return the decimal value equivalent to the balanced ternary string S
       + (the plus sign) represents +1
       0 represents zero, as usual
       - (the minus sign) represents -1
    """
    numb = len(S) - 1
    if len(S) == 0:
        return 0
    elif S[0] == "0":
            return balancedTernaryToNum(S[1:]) + 0
    elif S[0] == "-":
            numb = (-1) * 3**(len(S) - 1)
            return balancedTernaryToNum(S[1:]) + numb
    elif S[0] == "+":
            numb = (1) * 3**(len(S) - 1)
            return  balancedTernaryToNum(S[1:]) + numb


def numToBalancedTernary(N):
    """Return a balanced ternary string representing the value of the argument N
    0-->0
    remainder 2 --> "-", and N+1
    else (reminder of 1)--> "+"

    """
    if N == 0:
        return ""
    # disvisible by 3
    elif N%3 == 0:
        return numToBalancedTernary(N//3) + "0"
    # 14//3 = 2
    elif N%3 == 2:
        return numToBalancedTernary((N + 1)//3) + "-"
    else:
        return numToBalancedTernary((N )//3) + "+"
"""
     if N == 0:
        return ''
    elif N%3 == 0:
        return numToTernary(N//3) + '0'
    elif N%3 == 2:
        return numToTernary(N//3) + '2'
    else:
        return numToTernary(N//3) + '1'
"""