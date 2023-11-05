#
# hw9pr1.py - Game of Life lab (Conway)
#
# Name:
#

import random

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You might use this in your createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """Argument width: an int for column number
       Argument height: an int for height number
       Return a list of height rows and width columns
    """

    # call the createOneRow() function for "height" times
    LC = []
    for i in range(height):
        LC  +=[createOneRow(width)]
    return LC

def printBoard(A):
    """This function prints the 2D list-of-lists A."""

    # A = createBoard(5, 3)      # A is a list of list [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]] for createBoard(3,5)
    for row in A:                # number of lements in A = number of row
        for col in row:          # number of column = number of elements in sub-lists in A
            print(col, end = '') # print elements in the sub-list
        print()


def diagonalize(width, height):
    """Creates an empty board and then modifies it
       so that it has a diagonal strip of "on" cells.
       But it does that only in the *interior* of the 2D array.
    """
    A = createBoard(width, height)  #creat a list (height = row #)

    for row in range(1, height - 1):        # the first and last rows are not included 
        for col in range(1, width - 1):     # the first and last columns are not included
            if row == col:                  
                A[row][col] = 1  
            else:
                A[row][col] = 0

    return A

"""
[[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0]]

[[0, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 1, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0],
 [0, 0, 0, 0, 0, 0, 0]]
 """


def innerCells(w, h):
    """returns a 2D array that has all live cells—with a value of 1—except 
    for a one-cell-wide border of empty cells (with a value of 0) around 
    the edge of the 2D array.
    """

    A = createBoard(w, h)

    for row in range(1, h - 1):
        for col in range(1, w - 1):
            A[row][col] = 1
    return A

def randomCells(w, h):
    """
    """
    A = createBoard(w, h)

    for row in range(1, w-1):   # rows: not including the first and last rows
        for col in range(1, h-1): # rows: not including the first and last cols
            A[row][col] = random.choice([0,1 ])
    return A


def copy(A):
    """Return a deep copy of the 2D array A
    """
    height = len(A)    # number of elements in A
    width  = len(A[0])  # number of elements in the first sub-list in A
    newA = createBoard(width, height)  # create a 2D array 

    for row in range(1, height - 1):
        for col in range(1, width-1):
            newA[row][col] = A[row][col]   #copy each elements in A into newA (a new list) to create a deep copy
    return newA

def innerReverse(A):
    """Argument A: a 2D array list
       Return a new array newA of the same shape but in the reverse order
    """
    height = len(A)    # number of elements in A
    width  = len(A[0])  # number of elements in the first sub-list in A
    newA = createBoard(width, height)  # create a 2D array, a shallow copy

    for row in range(1, height - 1):
        for col in range(1, width-1):
            newA[row][col] = A[row][col]   #copy each elements in A into newA (a new list) to create a deep copy
            if A[row][col] == 0:
                A[row][col] == 1
            else:
                A[row][col] == 0
    return newA


def countNeighbors(row, col, A):
    """Argument row: an int for the row number
       Argument col: an int for the column number
       Argument A
       Return the number of live neighbors for a cell in the board A at a particular row and col
    """
    count = 0 # count the number of "1"
    
    for r in range(row-1, row+2):
        for n in range(col-1, col+2):
            if A[r][n] == 1:
                count +=1
    if A[row][col] == 1:
        count = count -1
    return count 

def next_life_generation(A):
    """Makes a copy of A and then advances one generation of Conway's Game of Life within
       the *inner cells* of that copy.
       The outer edge always stays at 0.
    """
    height = len(A)    # number of elements in A
    width = len(A[0])  # number of elements in the first sub-list in A
    newA = createBoard(height, width) 

    for row in range(1, height - 1):
        for col in range(1, width- 1):
            live_cell  = countNeighbors(row,col, A)
            if A[row][col] == 1:
                if live_cell == 2:
                    newA[row][col] = 1
                else:
                    newA[row][col] = 0
            else:
                if live_cell == 3:
                    newA[row][col] = 1
                else:
                    newA[row][col] = 0
    return newA



#
# +++ Helper functions for when Life has been completed! +++
#

"""
These allow for "terminal-graphics animation"

Once next_life_generation is complete, run

   lifedemo()

You may need to adjust your terminal's shape/size to 
    create a smooth animation.

"""



import sys

def printBoard_with_d( A, d = None ):
    """ this function prints the 2d list-of-lists A
        using the dictionary d 
    """
    if (d == None) or (0 not in d) or (1 not in d): # can we use d?
        for row in A:
            for col in row:
                sys.stdout.write( str(col) )     # use raw contents
            sys.stdout.write( '\n' )
    else:
        for row in A:
            for col in row:
                sys.stdout.write( str(d[col]) )  # lookup each value
            sys.stdout.write( '\n' )

def placeGlider(row,col,A):
    """ creates a glider with a bounding box
        whose upper-left corner is at row row and col col
    """
    H = len(A); W = len(A[0])
    OFFSETS = [ [+0,+1], [+1,+2], [+2,+0], [+2,+1], [+2,+2] ]
    for row_offset, col_offset in OFFSETS:
        r = row + row_offset
        c = col + col_offset
        if 0 < r < H-1 and 0 < c < W-1:
            A[r][c] = 1
    # no need to return A, A is changed in place!

def placeAirDancer(row,col,A):
    """ creates an up-down air dancer with top location
        (upper-left corner) is at row row and col col
    """
    H = len(A); W = len(A[0])
    OFFSETS = [ [+0,+0], [+1,+0], [+2,+0] ]
    for row_offset, col_offset in OFFSETS:
        r = row + row_offset
        c = col + col_offset
        if 0 < r < H-1 and 0 < c < W-1:
            A[r][c] = 1
    # no need to return A, A is changed in place!

import time

def lifedemo():
    """ ASCII demo! 
    """
    W = 42; H = 21          # alter to suit!
    
    A = createBoard(W,H)    # empty grid
    placeGlider(2,2,A)
    placeAirDancer(2,20,A)
    placeAirDancer(3,36,A)

    # A = randomCells(W,H)   # random grid
    
    # dictionaries to indicate what to print
    # d = { 0: 0,    1: 1 }
    d = { 0: 0,    1: " " }
    # d = { 0: " ",  1: "0" }
    # d = { 0: " ",  1: "#" }
    # d = { 0: "▯", 1: "▮" }
    # d = { 0: " ",  1: "🙂" } 


    while True:
        print("\n")

        
        printBoard_with_d(A, d)
        print("\n")
        A = next_life_generation(A)
        time.sleep(0.42)


# the terminal colors don't seem as successful
# d = { 0: "\033[6;36;47m0\033[0m", 1: "\033[6;37;40m1\033[0m" }
# www.cs.hmc.edu/twiki/bin/view/CS5/TerminalColorsInPython


#
# +++ end of helper functions +++
#