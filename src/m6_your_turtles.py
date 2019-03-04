"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Maddie Sorensen.
"""
########################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window=rg.TurtleWindow()
redturtle=rg.SimpleTurtle('turtle')
redturtle.pen=rg.Pen('red',5)
redturtle.speed=20
greenturtle=rg.SimpleTurtle('turtle')
greenturtle.pen=rg.Pen('green',5)
greenturtle.speed=30
size=100
size2=170
for k in range(7):
    redturtle.draw_circle(size)
    redturtle.pen_up()
    redturtle.left(60)
    redturtle.forward(45)
    redturtle.pen_down()
    size=size-10

for k in range(20):
    greenturtle.draw_circle(size2)
    greenturtle.pen_up()
    greenturtle.right(15)
    greenturtle.forward(20)
    greenturtle.pen_down()
    size2 = size2 - 8

window.close_on_mouse_click()

