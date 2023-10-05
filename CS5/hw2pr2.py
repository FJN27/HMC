# CS5 Gold, hw2pr2
# Filename: hw2pr2.py
# Name:
# Problem description: Sleepwalking student

import random
import sys
sys.setrecursionlimit(50000)

def rs():
    """rs chooses a random step and returns it.
       Note that a call to rs() requires parentheses.
       Arguments: none at all!
    """
    return random.choice([-1, 1])

import time

def rwpos(start, nsteps):
    """rwpos models a random walker that
        starts: starting position of the walker
        nsteps: the number of random steps the walker takes from his/her starting position
    """

    time.sleep(0.1)  

    print('location is', start) # print the walker's current position

    if nsteps == 0:
        return start
    else:
        newpos = start + rs()  # take one step

        return rwpos(newpos, nsteps - 1)   # minus one step from the random step



import time
import sys

def rwsteps(start, low, hi):
    """ rwsteps: number of steps to reach lower or upper bound
        Argument lowe: the lowest value the walker is allowed to walk to
        Argument hi: the highest value the walker is allowed to walk to
        * is currently at start 
        * is in a walkway from low (usually 0) to hi (max location) 
    """
    # rwsteps(2,0,5)
    walkway = "_"*(hi-low)    # create a walkway of underscores (This is a string) "_____". If hi-low = 5, it prints five underscores
    S = (start-low)           # this is our sleepwalker's location, start-low "__S___". This is done by slicing

    walkway = walkway[:S] + "S" + walkway[S:]  # put our sleepwalker, "S", there
    
    walkway = "|" + walkway + "|"        # surround with spaces, for now...

    print(walkway, " " , start, low, hi)     # print everything to keep track...
    
    # sys.stdout.flush()   # forces Python to print everything now - may not be needed
    # time.sleep(0.1)      # and then sleep for 0.1 seconds

    if start <= low or start >= hi:            # base case: no steps if we're at an endpt
        return 0
    
    else:
        newstart = start + rs()                # takes one step (a new position)
        return 1 + rwsteps(newstart, low, hi)  # counts one step, recurses! (total steps)


def poptart_race(sA, sB, PT):
    """the total number of steps sA/sB takes to win the competition
       sA (startA): the location of the first student
       sB: the location of the second student
       PT: the location of the poptart
       Rules for the game:
          --Whoever reaches the poptart first wins the game
          --If sA or sB touches the lower/upper bonds, the game ends.
          --Total steps taken by the winner is recorded and returned
    """
    low = 0
    upper = 20

    walkway = (upper - low)* "_"
   
   

    walkway = walkway[:sA] + "sA（😀）" + walkway[sA:PT] + "#" + walkway[PT:sB] + "sB（😍）" + walkway[sB:] 
    
    walkway = "|" + walkway + "|"        # surround with borders

    print(walkway, " " , sA, sB, PT)     # print everything to keep track...
    
    # sys.stdout.flush()   # forces Python to print everything now - may not be needed
    # time.sleep(0.1)      # and then sleep for 0.1 seconds

    if sA == low or sB == upper:            # base case: no steps if we're at an endpt
        print("end")
        return 0
    elif sA == PT or sB == PT:
        return 0
    
    else:
        newstart_A = sA + rs()                # takes one step (a new position for sA)
        newstart_B = sB + rs()                # takes one step (a new position for sB)
        return 1 + poptart_race(newstart_A, newstart_B, PT)   # counts one step, recurses! (total steps)

"""
In [65]: poptart_race(5,15,10)
|_____sA_____#_____sB_____|   5 15 10
|______sA____#______sB____|   6 16 10
|_____sA_____#_______sB___|   5 17 10
|______sA____#______sB____|   6 16 10
|_______sA___#_____sB_____|   7 15 10
|______sA____#______sB____|   6 16 10
|_____sA_____#_______sB___|   5 17 10
|____sA______#________sB__|   4 18 10
|___sA_______#_______sB___|   3 17 10
|____sA______#______sB____|   4 16 10
|___sA_______#_____sB_____|   3 15 10
|____sA______#____sB______|   4 14 10
|_____sA_____#_____sB_____|   5 15 10
|____sA______#______sB____|   4 16 10
|_____sA_____#_____sB_____|   5 15 10
|______sA____#______sB____|   6 16 10
|_______sA___#_______sB___|   7 17 10
|________sA__#________sB__|   8 18 10
|_________sA_#_______sB___|   9 17 10
|__________sA#______sB____|   10 16 10
Out[65]: 19

#############################################

In [67]: poptart_race(5,15,10)
|_____sA_____#_____sB_____|   5 15 10
|____sA______#____sB______|   4 14 10
|_____sA_____#_____sB_____|   5 15 10
|____sA______#______sB____|   4 16 10
|___sA_______#_______sB___|   3 17 10
|____sA______#________sB__|   4 18 10
|_____sA_____#_________sB_|   5 19 10
|______sA____#__________sB|   6 20 10
end
Out[67]: 7


"""