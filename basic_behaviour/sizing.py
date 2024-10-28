# ref https://docs.python.org/3/library/turtle.html

import turtle
import random

canvas = turtle.Screen()
canvas.bgcolor("black")

the_turtle = turtle.Turtle()
the_turtle.color("green")

def draw_spiral(pen_size=1, pen_size_change=0, edge_size = 20, edge_size_change = 10):
    for edge in range(20):
        angle_change = random.randint(89,105) # 89 is the usual constant
        the_turtle.pensize(pen_size)
        the_turtle.forward(edge_size)
        the_turtle.left(angle_change)
        pen_size += pen_size_change
        edge_size += edge_size_change

    return 0

draw_spiral()


    

canvas.mainloop() 


