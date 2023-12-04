#
# hw9pr2.py
#
# Name:
#

# Here is a function for printing 2D arrays
#  (lists-of-lists) of data

def print2d(A):
    """print2d prints a 2D array, A,
       as rows and columns.
       Argument: A, a 2D list of lists.
       Result: None (no return value)
    """
    num_rows = len(A)
    num_cols = len(A[0])

    for r in range(num_rows):
        for c in range(num_cols):
            print(A[r][c], end = ' ')
        print()

    print()

    return None  # This is implied anyway
                 # when no return statement is present

# some tests for print2d
A = [['X', ' ', 'O'], ['O', 'X', 'O']]
print("2-row, 3-column A is")
print2d(A)

A = [['X', 'O'], [' ', 'X'], ['O', 'O'], ['O', 'X']]
print("4-row, 2-column A is")
print2d(A)


# Create a 2D array from a 1D string
def createA(num_rows, num_cols, s):
    """Returns a 2D array with
           num_rows rows and
           num_cols columns
       using the data from s: across the
       first row, then across the second, etc.
       We'll only test it with enough data!
    """
    A = []
    for r in range(num_rows):
        newrow = []
        for c in range(num_cols):
            newrow += [s[0]] # Add that char
            s = s[1:]        # Get rid of that first char
        A += [newrow]
    return A

# A couple of tests for createA:
A = [['X', ' ', 'O'], ['O', 'X', 'O']]
newA = createA(2, 3, 'X OOXO')
assert newA == A
print("Is newA == A? Should be True:", newA == A)

A = [['X', 'O'], [' ', 'X'], ['O', 'O'], ['O', 'X']]
newA = createA(4, 2, 'XO XOOOX')
assert newA == A

def inarow_3east(ch, r_start, c_start, A):
    """Argument ch: a string 
       Argument r_start: a int for row position
       Argument c_start: an int for col position
       Argument A: a 2D array list
       return True is three characters (same character) in a row
    """

    col_upper_bound =  len(A[0]) - 3
    
    """
    X X X X
    X X X X
    X X X X
    X X X X X
    """

    if c_start <0 or c_start > col_upper_bound:
        return False
    
    count = 3 - c_start

    while (3 - c_start) > 0:
        if ch != A[r_start][c_start]:
            return False
        else:
            count -= 1
            c_start +=1
    return True

# tests of inarow_3east
A = createA(3, 4, 'XXOXXXOOOOOO')
print("\n3east :")
print2d(A)
assert inarow_3east('X', 0, 0, A) == False
assert inarow_3east('O', 2, 1, A) == True
assert inarow_3east('X', 2, 1, A) == False
assert inarow_3east('O', 2, 2, A) == False
print("All 3east tests worked!")


def inarow_3south(ch, r_start, c_start, A):
    """Argument ch: a string 
       Argument r_start: a int for row position
       Argument c_start: an int for col position
       Argument A: a 2D array list
       return True is three characters (same character) in a col
    """
    
    """
    X X X X
    X X X X
    X X X X
    X X X X 
    """

    row_upper_bond = len(A) - 3

    if c_start < 0 or c_start > row_upper_bond:
        return False
    
    count = 3 - r_start

    while count > 0:
        if ch != A[r_start][c_start]:
            return False
        count -=1
        r_start +=1
    return True

# tests of inarow_3south
A = createA(4, 4, 'XXOXXXOXXOO OOOX')
print("\n3south :")
print2d(A)
assert inarow_3south('X', 0, 0, A) == True
assert inarow_3south('O', 2, 2, A) == False
assert inarow_3south('X', 1, 3, A) == False
assert inarow_3south('O', 42, 42, A) == False
print("All 3south tests worked!")


def inarow_3southeast(ch, r_start, c_start, A):
    """Argument ch: a string 
       Argument r_start: a int for row position
       Argument c_start: an int for col position
       Argument A: a 2D array list
       return True is three characters (same character) in a col
    """

    row_upper_bond = len(A) - 3
    col_upper_bound = len(A[0]) - 3
    
    if c_start < 0 or c_start > row_upper_bond or c_start < 0 or c_start > col_upper_bound:
        return False
    
    count = 3 - r_start

    while count > 0:
        if ch != A[r_start][c_start]:
            return False
        count -=1
        r_start +=1
        c_start +=1
    return True

    
A = createA(4, 4, 'XOOXXXOXX XOOOOX')
print("\n3southeast :")
print2d(A)
assert inarow_3southeast('X', 1, 1, A) == True
assert inarow_3southeast('X', 1, 0, A) == False
assert inarow_3southeast('O', 0, 1, A) == True
assert inarow_3southeast('X', 2, 2, A) == False
print("All 3southeast tests worked!")


def inarow_3northeast(ch, r_start, c_start, A):
    """Argument ch: a string for character
       Argument r_start: an int for row position
       Argument c_start: a int for col position
       Argument A: a 2D array 
       return True if 3 same characters consecutively arranged in the north direction
       return False otherwise
    """

    col_upper_bound = len(A[0]) - 3
    row_upper_bound = len(A) - 3


    if c_start > col_upper_bound or c_start > row_upper_bound:
        return False
    count = 3 - c_start

    while count > 0:
        while ch != A[r_start][c_start]:
            return False
        count -=1
        c_start +=1
        r_start -=1
    
    return True
    

A = createA(4, 4, 'XOXXXXOXXOXOOOOX')
print("\n3northeast :")
print2d(A)
assert inarow_3northeast('X', 2, 0, A) == True
assert inarow_3northeast('O', 3, 0, A) == True
assert inarow_3northeast('O', 3, 1, A) == False
assert inarow_3northeast('X', 3, 3, A) == False
print("All 3northeast tests worked!")



def inarow_Neast(ch, r_start, c_start, A, N):
    """Argument ch: a string for character
       r_start: an int for row position
       c_start: a int for col position
       Argument A: an 2D array list
       Argument N: an int for the number of ch in a col
    """
    row_upper_bound = len(A)      # number of rows is len(A)
    col_num = len(A[0]) - N  # number of cols is len(A[0]) 

    if r_start >= row_upper_bound:
        return False # out of bounds in rows
        # other out-of-bounds checks...
    if c_start > col_num:
        return False # out of bounds in cols
        # are all of the data elements correct?
    for i in range(N):                  # loop index i as needed
        if A[r_start][c_start+i] != ch: # check for mismatches
            return False                # mismatch found--return False
    return True                         # loop found no mismatches--return True


# tests of inarow_Neast
A = createA(5, 5, 'XXOXXXOOOOOOXXXX XXXOOOOO')
print("\nNeast :")
print2d(A)
assert inarow_Neast('O', 1, 1, A, 4) == True
assert inarow_Neast('O', 1, 3, A, 2) == True
assert inarow_Neast('X', 3, 2, A, 4) == False
assert inarow_Neast('O', 4, 0, A, 5) == True
print("All Neast tests worked!")




def inarow_Nsouth(ch, r_start, c_start, A, N):
    """Argument ch: a string for character
       r_start: an int for row position
       c_start: a int for col position
       Argument A: an 2D array list
       Argument N: an int for the number of ch in a row
    """

    """len(A) - 1   # last row 
    len(A[0]) - 1   # last col 

    row_upper_bound = len(A) - N # row_upper_bound = len(A) - 1 - (N-1)
    
    # south dir, only care of row position

    if c_start > row_upper_bound:
        return False
    
    count = N - c_start

    while count > 0:
        if ch != A[r_start][c_start]:
            return False
        count -=1
        r_start +=1
    return True"""

    row_upper_bound = len(A) - N
    col_upper_bound = len(A[0]) 
    
    if r_start  > row_upper_bound or c_start > col_upper_bound:
        return False
    
    for i in range(N):                  
        if A[r_start+i][c_start] != ch: 
            return False               
    return True

# tests of inarow_Nsouth
A = createA(5, 5, 'XXOXXXOOOOOOXXXXOXXXOOOXO')
print("\nNsouth :")
print2d(A)
assert inarow_Nsouth('X', 0, 0, A, 5) == False
assert inarow_Nsouth('O', 1, 1, A, 4) == True
assert inarow_Nsouth('O', 0, 1, A, 6) == False
assert inarow_Nsouth('X', 4, 3, A, 1) == True
print("All Nsouth tests worked!")


def inarow_Nsoutheast(ch, r_start, c_start, A, N):
    """Argument ch: a string for character
       r_start: an int for row position
       c_start: a int for col position
       Argument A: an 2D array list
       Argument N: an int for the number of ch in the southeast dir
       return True if N elements are consecutively arranged in southeast dir
       return False otherwise
    """

    """col_upper_bound = len(A[0]) - N
    row_upper_bound = len(A) - N

    if c_start > col_upper_bound or r_start > row_upper_bound:
        return False
    
    count = N - (c_start)
    
    while count > 0:
        if ch != A[r_start][c_start]:
            return False
        r_start +=1
        c_start +=1
        count -=1

    return True"""
    col_upper_bound = len(A[0]) - N
    row_upper_bound = len(A) - N

    if c_start > col_upper_bound or r_start > row_upper_bound:
        return False
    
    for i in range(N):
        if ch != A[r_start + i][c_start + i]:
            return False

    return True


# tests of inarow_Nsoutheast
A = createA(5, 5, 'XOO XXXOXOOOXXXXOXXXOOOXX')
print("\nNsoutheast :")
print2d(A)
assert inarow_Nsoutheast('X', 1, 1, A, 4) == True
assert inarow_Nsoutheast('O', 0, 1, A, 3) == False
assert inarow_Nsoutheast('O', 0, 1, A, 2) == True
assert inarow_Nsoutheast('X', 3, 0, A, 2) == False
print("All Nsoutheast tests worked!")



def inarow_Nnortheast(ch, r_start, c_start, A, N):
    """Argument ch: a string for character
       r_start: an int for row position
       c_start: a int for col position
       Argument A: an 2D array list
       Argument N: an int for the number of ch in the southeast dir
       return True if N elements are consecutively arranged in southeast dir
       return False otherwise
    """

    col_upper_bound = len(A[0]) - N
    row_upper_bound = len(A) - N

    if c_start > col_upper_bound or c_start < row_upper_bound:
        return False
    
    count = N - (c_start)
    
    while count > 0:
        while ch != A[r_start][c_start]:
            return False
        c_start += 1
        r_start -= 1
        count -= 1
        
    return True

# tests of inarow_Nnortheast
A = createA(5, 5, 'XOO XXXOXOOOXOXXXOXXXOOXX')
print("\nNnortheast :")
print2d(A)
assert inarow_Nnortheast('X', 4, 0, A, 5) == True
assert inarow_Nnortheast('O', 4, 1, A, 4) == True
assert inarow_Nnortheast('O', 2, 0, A, 2) == False
assert inarow_Nnortheast('X', 0, 3, A, 1) == False
print("All Nnortheast tests worked!")