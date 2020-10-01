import turtle

turtle.shape('turtle')

turtle.penup()
turtle.forward(50)
turtle.left(90)
turtle.pendown()

draw_circle()


def draw_circle():
    for i in range(360):
        turtle.forward(1)
        turtle.left(1)
