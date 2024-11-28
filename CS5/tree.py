'''
import turtle
hr = turtle.Turtle()
hr.left(90)
hr.speed(150)

def tree(i):
    if(i>=20):
      hr.forward(i)
      hr.left(30)
      tree(3*i/4)
      hr.right(30)
      tree(3*i/4)
      hr.right(30)
      tree(3*i/4)
      hr.left(30)
      hr.backward(i)

tree(100)
turtle.done()

# recurisive tree 
import ColabTurtlePlus.Turtle as t

t.clearscreen()      # it's good to start every cell with this
t.setup(500,500)     # setup the drawing area to be 500 pixels x 500 pixels
t.showborder()       # show the border of the drawing area

t.bgcolor("AliceBlue")   # adjust to your preferences!
t.shape("turtle2")
t.speed(1)
t.width(2)
# t.left(90)
'''
# import ColabTurtlePlus.Turtle as t
import turtle as t
def svtree(trunklength, levels, angle):
    """svtree: draws a side-view tree
       trunklength = the length of the first line drawn ("the trunk")
       levels = the depth of recursion to which it continues branching
    """
    if levels == 0:
        return
    else:
      t.forward(trunklength) # draw the branch
      t.right(angle) # turn right
      svtree(trunklength*0.8, levels-1, angle) # recursion to turn left

      t.left(2*angle) # the head turns left

      svtree(trunklength*0.8, levels-1, angle) # recurison to move right

      t.right(angle) # the head goes back to the middle


      t.backward(trunklength) # draw back the branch

      pass # delete this empty statement later

#
# setup - move the turtle backward a bit:
#
t.penup()
t.backward(150)
t.pendown()

# Go!  One example:
svtree(100, 6, 30)

# try svtree(100,5)



################################################################################
################################################################################
################################################################################


t.clearscreen()      # it's good to start every cell with this
t.setup(500,500)     # setup the drawing area to be 500 pixels x 500 pixels
t.showborder()       # show the border of the drawing area

t.bgcolor("AliceBlue")   # adjust to your preferences!
t.shape("turtle2")
t.speed(10)
t.width(2)

def flakeside(sidelength, levels):
    """ flakeside draws _one side_ of the fractal Koch snowflake
    """

    # see hints below! This function is _deeply_ recursive!
    if levels == 0:
      t.forward(sidelength/3)
      return
    else:
      flakeside(sidelength/3, levels - 1)
      t.right(60)

      flakeside(sidelength/3, levels - 1)
      t.left(120)

      flakeside(sidelength/3, levels -1)

      t.right(60)
      flakeside(sidelength/3, levels - 1)

      pass

def snowflake(sidelength, levels):
  """
  """
  if levels == 0:
    t.forward(sidelength)
    return
  else:
    flakeside(sidelength, levels)

    t.left(120)
    flakeside(sidelength, levels)

    t.left(120)
    flakeside(sidelength, levels)

    pass # remove this empty statement later

# try it!
#
t.penup()
t.goto(-200,0)  # move the pen to a "southwest" corner...
t.pendown()

snowflake(500,2)

################################################################################
################################################################################
################################################################################
