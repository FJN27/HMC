# hw8pr1.py
# Lab 8
#
# Name:
#

# keep this import line...
from cs5png3 import *

"""

If you get an error that there is "no PIL" or "no object/library PIL," it's the Pillow library you need.
Try


!pip install Pillow       or
!pip3 install Pillow       or
%pip install Pillow       or
%pip3 install Pillow      

"""
#
# A test function...
#
def test_fun():
    """Algorithmic image creation, one pixel at a time.
       This is a test function: it should create
       an image named test.png in the current directory.
    """
    im = PNGImage(300, 200)  # Creates an image of width 300, height 200

    # Nested loops!
    for r in range(200):     # loops over the rows with runner variable r
        for c in range(300): # loops over the columns with c
            if  c == r:   
                im.plotPoint(c, r, (255, 0, 0))
            #else:
            #    im.plotPoint(c, r, (255, 0, 0))
                
    im.saveFile()

#
# start your Lab 8 functions here:
#
def mult(c, n):
    """multiply c n times without using multiplying
    """
    result = 0
    for i in range(n):
        result = result + c
        n = n -1
    return result

def update(c, n):
    """Update starts with z = 0 and runs z = z**2 + c
       for a total of n times. It returns the final z.
    """
    z = 0
    for i in range(n):
        z = z**2 + c
    return z


def inMSet(c, n):
    """inMSet accepts
            c for the update step of z = z**2+c
            n, the maximum number of times to run that step.
       Then, it returns
            False as soon as abs(z) gets larger than 2.
            True if abs(z) never gets larger than 2 (for n iterations).
    """
    z = 0
    for i in range(n):
        z = z**2 + c
        if abs(z) > 2:
            return False
    else:
        return True
    

from cs5png3 import *   # You might already have this line at the top...

def weWantThisPixel(col, row):
    """This function returns True if we want to show
       the pixel at col, row and False otherwise.
    """
    if col % 10 == 0  and  row % 10 == 0:
        return True
    else:
        return False

def test():
    """This function demonstrates how
       to create and save a PNG image.
    """
    width = 300
    height = 200
    image = PNGImage(width, height)

    # Create a loop that will draw some pixels.

    for col in range(width):
        for row in range(height):
            if weWantThisPixel(col, row):
                image.plotPoint(col, row)

    # We looped through every image pixel; we now write the file.

    image.saveFile()

def scale(pix, pixMax, floatMin, floatMax):
    """The first argument, pix, is the current pixel value: we are at column 150 (or perhaps row 150; scale doesn't care).
    The second argument, pixMax, is the maximum possible pixel value: pixels run from 0 to 200 in this case.
    The third argument, floatMin, is the minimum floating-point value. This is what the function will return when the first argument is 0.
    The fourth argument, floatMax, is the maximum floating-point value. This is what the function will return when the first argument is pixMax.
    """
    return floatMin+ (floatMax - floatMin)*(pix/pixMax)


def mset():
    """Creates a 300x200 image of the Mandelbrot set.
    """
    # width = 300*1       # We can update the 1 later to enlarge the image...
    # height = 200*1
    # image = PNGImage(width, height)

    NUM_ITERATIONS = 100  # of updates
    XMIN = -1.2  # The smallest real coordinate value
    XMAX =  -.6  # The largest real coordinate value
    YMIN = -.5   # The smallest imaginary coordinate value
    YMAX = -.01  # The largest imaginary coordinate value
    FACTOR = 3
    width = 300*FACTOR
    height = 200*FACTOR
    image = PNGImage(width, height)  # make sure the image is the right size


    # Create a loop to draw some pixels

    for col in range(width):
        for row in range(height):
    
            # find x using the scale function
            x = scale(col, width, XMIN, XMAX)
            #  use the scale function to find y
            y = scale(row, height, YMIN, YMAX)

            c = x + y*1j
            n = 25
            if inMSet(c, n) == True:
                image.plotPoint(col, row, (255, 175, 0))
            else:
                image.plotPoint(col,row, (0, 0, 0))


    # We looped through every image pixel; we now write the file
    image.saveFile()

"""for col in range(10):
    for row in range(5):
        print("col is: ", col, "row is:" , row)
        """
            