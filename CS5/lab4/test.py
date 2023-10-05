# Python Program

# Given helper function in question
def frontNum(S):
    if len(S) <= 1:
        return len(S)
    elif S[0] == S[1]:
        return 1 + frontNum(S[1:])
    else:
        return 1

# Given helper function in question
def numToBaseB(N, B):
    """returns a string representing the number N in base B.
    Argument N: a non-negative integer N
    Argument B: a base B (between 2 and 10 inclusive)
    """
    if N == 0:
        return ''
    else:
        return numToBaseB(N//B, B) + str(N % B)

# function to make strings of length 7 by adding zeroes
def addzeros(S):
    if(len(S) == 7):
        return S
    else:
        return addzeros("0"+S)

# required function compress
def compress(S):
    # if length of String is 0 return ""
    if len(S) == 0:
        return ""
    else:
        # extracting the first digit and counting using frontNum function and converting
        # it into base 2 using numToBaseB function and then making it length 7 string
        # by using addzeros function and passing the remaining string to compress function
        return S[0]+addzeros(numToBaseB(frontNum(S), 2))+compress(S[frontNum(S):])


print(compress('11111'))
print(compress('101010'))
print(compress(42*'0'))