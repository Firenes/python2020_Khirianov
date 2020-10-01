import turtle

turtle.shape('turtle')

def draw_spider(legs: int):
    angle = 360 / legs
    full = angle

    while full <= 360:
        turtle.right(full)
            
        turtle.forward(100)
        turtle.stamp()
        turtle.right(180)
        turtle.forward(100)

        turtle.right(180 - full)

        full += angle

draw_spider(12)
