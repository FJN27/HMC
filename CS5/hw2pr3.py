# CS 5 Gold, hw2pr3
# filename: hw2pr3.py
# Name:
# problem description: List comprehensions



# this gives us functions like sin and cos...
from math import *

# two more functions (not in the math library above)

def dbl(x):
    """Doubler!  argument: x, a number"""
    return 2*x

def sq(x):
    """Squarer!  argument: x, a number"""
    return x**2

# examples for getting used to list comprehensions...

def lc_mult(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each multiplied by 2**
    """
    return [2*x for x in range(N)]

def lc_idiv(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each divided by 2**
       WARNING: this is INTEGER division...!
    """
    return [x//2 for x in range(N)]

def lc_fdiv(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each divided by 2**
       NOTE: this is floating-point division...!
    """
    return [x/2 for x in range(N)]


# printing tests
print( "lc_mult(4)   should be [0, 2, 4, 6] :", lc_mult(4) )   
print( "lc_idiv(4)   should be [0, 0, 1, 1] :", lc_idiv(4) ) 
print( "lc_fdiv(4)   should be [0.0, 0.5, 1.0, 1.5] :", lc_fdiv(4) ) 

# assertion tests
assert lc_mult(4) == [0, 2, 4, 6]
assert lc_idiv(4) == [0, 0, 1, 1]
assert lc_fdiv(4) == [0.0, 0.5, 1.0, 1.5]




#------------------------------------------------------------------------------------------------------------

# Here is where your functions start for the lab:
# Step 1, part 1

def unitfracs(N):
    """Returns a list of evenly-spaced fractions in the unit interval [0, 1).
    """
    list = [x/N for x in range(N)] 
    return list   # output is a list, so it should use[] instead of ()



def scaledfracs(low, high, N):
    """eturns a list of evenly-spaced fractions in the interval [low, high).
    """
    list = [low + x * (high - low) for x in unitfracs(N)] # 20/5=(1/5)*(20)
    return list     

print("scaledfracs(10,30,5) is:", scaledfracs(10,30,5))




def sqfracs(low, high, N): 
    """  returns a list of squared values of N fractionsin the interval [low, hi) 
    low: lowest value of the interval in scaledfracs() 
    hi: highest value of the interval in scaledfracs() 
    N: a number N (integer or float) 
    Return Value: a list of squared values of scaledfracs(low, hi, N) """ 
    return [ x*x for x in scaledfracs(low, high, N)]
    

def f_of_fracs(f, low, high, N):
    """Takes the function of its first argument
        Argument f: the function
        Argument low: an integer
    """
    
    list = [f(x) for x in (scaledfracs(low, high, N))]

    return list

# import math

def sum(i):
    """return the sum of index
        Argument i: a list consist of numbers (can be float or integer)
    """
    if len(i) == 0:
        return 0
    else:
        return i[0] + sum(i[1:])
    
def integrate(f, low, high, N):
    """Retures the integral of f from the lower bound to the upper bound using N steps
       Argument low: an number representing the lower bound
       Argument high: an number representing the upper bound
       Argument N: an integer representing step number (number of interval used for integration
    """
    diff = (high - low)/N
    print("difference is: ", diff)

    x_list = [(high - low) * x for x in unitfracs(N)] # A list of x-values: difference divided by N --> function unitfracs(N)
    print("x_values are: ", x_list)

    y_list = f(x_list) # list of y-values --> function f_of_fracs
    print("y_values are: ", y_list)

    area_ind = [diff*y for y in y_list]
    totalArea = sum(area_ind) #compute the total area by adding individual areas

    return totalArea

# print( "integrate(dbl, 0, 10, 4) should be 75 :", integrate(dbl, 0, 10, 4) )
# print( "integrate(sq, 0, 10, 4) should be 218.75 :", integrate(sq, 0, 10, 4) )


"It is always underestimating the area if we use the left-sum to calculate the shape's total area."
"Area under curve is calculated by approximating the sum of N rectangles"


def c(x):
    """c is a semicircular function of radius two"""
    return (4 - x**2)**0.5