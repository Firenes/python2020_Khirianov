import turtle

turtle.shape('turtle')

def square_spiral(n: int, height: int):
    squares = n * 4

    for square in range(squares):
        side = height * ((square + 1) / 2)

        turtle.forward(side)
        turtle.left(90)

square_spiral(10, 7)
