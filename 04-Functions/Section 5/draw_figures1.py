import turtle
import figures

window = turtle.Screen()
window.bgcolor("lightblue")

pen = turtle.Turtle()
pen.speed(5)

side_length = 100
side_length_a = 200
side_length_b = 100
side_length = 100

pen.penup()
pen.goto(100,100)
pen.pendown()

figures.draw_triangle(side_length)

pen.penup()
pen.goto(-100, -200)
pen.pendown()

figures.draw_triangle(side_length)

pen.penup()
pen.goto(100, 100)
pen.pendown()
figures.draw_rectangle(side_length_a, side_length_b)

pen.penup()
pen.goto(-100, -200)
pen.pendown()
figures.draw_rectangle(side_length_a, side_length_b)

pen.penup()
pen.goto(-100, 100)
pen.pendown()
figures.draw_square(side_length)


pen.penup()
pen.goto(200, -100)  # Move to a new location
pen.pendown()
figures.draw_square(side_length)

pen.hideturtle()
window.mainloop()




