import turtle

turtle.shape('turtle')
    
def draw_nested_squares(n: int, height: int):
    old_square = new_square = 0

    for square in range(n):
        old_square = new_square
        new_square = height * (((square + 1) / 2))
    
        for i in range(4):
            turtle.forward(new_square)
            turtle.left(90)

        curr_pos = turtle.position()
        new_pos = (new_square - old_square) / 2
        turtle.penup()
        turtle.goto(curr_pos - (new_pos, new_pos))
        turtle.pendown()

draw_nested_squares(15, 50)
