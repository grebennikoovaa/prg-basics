###
# Draw a square
#
import turtle
def draw_square(side_length):
    pen = turtle.Turtle()
    for i in range(4):
        pen.forward(side_length)
        pen.right(90)
    pen.hideturtle()

def draw_triangle(side_length):
    pen = turtle.Turtle()
    for _ in range(3):
        pen.forward(side_length)
        pen.left(120) 
    pen.hideturtle()

def draw_rectangle(side_length_a, side_length_b):
    pen = turtle.Turtle()
    for _ in range(2):
        pen.forward(side_length_a)
        pen.right(90)
        pen.forward(side_length_b)
        pen.right(90)
    pen.hideturtle()