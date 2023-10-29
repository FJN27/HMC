#
# hw8pr3.py
#

# Name:

import random
import time
import math


def dart():
    """ Throws one dart between (-1,-1) and (1,1).
        Returns True if it lands in the unit circle; otherwise, False otherwise
    """
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    if x**2 + y**2 < 1:
        return True        # HIT (within the unit circle)
    else:
        return False       # miss (landed in one of the corners)
    

def forpi(n):
    """Argument n: an int for the number of throws
       Return the estimate of value of pi
    """
    hits = 0
    for i in range(n):
        if dart() == True:
            hits +=1
            throws = n
            esti_pi = 4*hits/throws
            print("hits is:",  hits, "throws is:", throws, "and estimate is:", esti_pi)
    return esti_pi


def whilepi(err0r):
    """The number of darts thrown so far.
       The number of darts thrown so far that have hit the circle.
       The resulting estimate of 𝝅.
    """
    condition = True
    hits = 0
    throws = 0

    while condition == True:
        throws +=1
        if dart() == True:
            hits +=1
            esti_pi = 4*hits/throws
            error = abs(esti_pi - math.pi)
            print("hits is:",  hits, "throws is:", throws, "and estimate is:", esti_pi)
            if error < err0r:
                condition = False
            else:
                condition = True
    return throws


def forpi_np(N):
    """Return the number of hits in a list
       Argument N: an int
    """
    hits = 0
    for i in range(N):
        if dart() == True:
            hits +=1
            throws = N
            esti_pi = 4*hits/throws
            print("hits is:",  hits, "throws is:", throws, "and estimate is:", esti_pi)
    
    return esti_pi


def whilepi_np(err):
    """Return the estimation error in a list
       Argument err: an int, float
    """
    condition = True
    hits = 0
    throws = 0
    LC = [] # LC is a list

    while condition == True:
        throws +=1
        if dart() == True:
            hits +=1
            esti_pi = 4*hits/throws
            error = abs(esti_pi - math.pi)
            LC = [error] + LC  # error in a list
            print("hits is:",  hits, "throws is:", throws, "and estimated value is:", esti_pi)
            
            if error < err:
                condition = False
            else:
                condition = True
    return LC



def whilepi_np_2(err):
    """Return the estimation error in a list
       Argument err: an int, float
    """
    condition = True
    hits = 0
    throws = 0
    LC = [] # LC is a list

    while condition == True:
        throws +=1
        if dart() == True:
            hits +=1
            esti_pi = 4*hits/throws
            error = abs(esti_pi - math.pi)
            LC = [error] + LC  # error in a list
            # print("hits is:",  hits, "throws is:", throws, "and estimated value is:", esti_pi)
            
            if error < err:
                condition = False
            else:
                condition = True
    return hits

def avg(e):
    LC = [whilepi_np_2(e) for x in range(100)]
    print(LC)

    return sum(LC)/len(LC)



"""

I create a LC with 100 an error of 0.1 using the line
      LC = [whilepi_np_2(0.1) for x in range(100)]

Out of those 100 trials, the average number of throws
(sum(LC) / len(LC)) needed to reach the an error below 0.1 was:

++++++++++++
+ 27.41  +
++++++++++++


NOTE: Table for error of 0.1
In [36]: avg(0.1)
[7, 8, 4, 7, 10, 24, 7, 4, 7, 13, 13, 13, 10, 4, 7, 4, 7, 8, 17, 4, 4, 4, 4, 26, 4, 106, 160, 12, 7, 4, 7, 13, 26, 7, 13, 8, 16, 29, 242, 10, 7, 4, 32, 13, 4, 12, 51, 7, 8, 149, 7, 7, 4, 7, 4, 12, 21, 7, 237, 7, 316, 7, 7, 4, 4, 4, 4, 89, 48, 17, 191, 7, 29, 4, 4, 7, 7, 4, 42, 29, 4, 12, 26, 7, 7, 10, 4, 18, 4, 7, 16, 4, 7, 38, 4, 20, 4, 34, 4, 207]

Out[36]: 27.41

"""

"""
NOTE: an error below 0.01
Out of those 100 trials, the average number of throws
(sum(LC) / len(LC)) needed to reach the an error below 0.01 was:

++++++++++++
+ 1541.46  +
++++++++++++


In [38]: avg(0.01)
[11, 22, 1504, 228, 120, 22, 62, 65, 11, 127, 33, 29, 89, 11, 26, 51, 11, 26, 33, 44, 33, 26, 135, 26, 11, 6430, ...]

Out[38]: 1541.46

"""

"""
NOTE: an error below 1

Out of those 100 trials, the average number of throws
(sum(LC) / len(LC)) needed to reach the an error below 1 was:

++++++++++++
+ 1.34  +
++++++++++++


In [37]: avg(1)
[1, 2, 1, 1, 1, 1, 1, 3, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 4, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 3, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 2, 1, 1, 1, 1, 6, 2, 1, 2, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 4, 1, 1]

Out[37]: 1.34

"""


