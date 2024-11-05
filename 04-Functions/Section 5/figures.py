###
# Draw a square
#
import turtle
def draw_square(side_length):
    pen = turtle.Turtle()
    for i in range(4):
        pen.forward(side_length)
        pen.right(90)