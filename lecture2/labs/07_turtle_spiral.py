import turtle
import numpy

turtle.shape('turtle')

def spiral(stop, step):
    for i in numpy.arange(0, stop, step):
        turtle.forward(i / 2 * numpy.pi)
        turtle.left(2 * numpy.pi)

spiral(5, 0.01)
