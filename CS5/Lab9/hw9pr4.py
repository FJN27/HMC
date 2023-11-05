def next(term):
    """Argument term: a string
       Return the next element 
    """

    # number of time the first element consecutively appear in the string
    # [numb..appear, the element]
    # recursion/loop for the next element
    # at the same time, add each sub-strings
    # len(s) == 0: return "" to halt the function
    
    term = str(term)   # convert int term to a string

    if len(term) == 0:  # empty: return ""
        return ""
    length = len(term)

    LC = []
    while length > 0:
        num = firtletter(term) # call the helper function to count the number of times the first element consecutively appear
        LC = LC + [str(num), term[num - 1]] # put it into a list
        term = term[num:]  # slice the function
        length = length - num  # length is subtracted
       
    element = ''
    for i in LC:
        element = element + i  # add up each sub string

    return int(element)   # return the element in int
    

def firtletter(S):
    """Argument S: a string
       Return an int: the number of time the first element consecutively appear
    """
    if len(S) == 0:
        return 0
    if len(S) == 1:
        return 1
    
    elif S[0] == S[1]:
        return 1 + firtletter(S[1:])
    else: 
        return 1

assert next(21) == 1211
assert next(2222) == 42
assert next(312211) == 13112221



def readit(n):
    """Argument n: an int
    """
    if n <=0:
        return ""
    else:
        print(1)
        num = 1
        for i in range(n-1):
            print(next(num), end='\n')
            num = next(num)
            # print("num", num)

