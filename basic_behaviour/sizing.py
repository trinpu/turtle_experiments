# ref https://docs.python.org/3/library/turtle.html

import turtle
import random

canvas = turtle.Screen()
canvas.bgcolor("black")

def draw_spiral(a_turtle, pen_size=1, pen_size_change=0, edge_size = 20, edge_size_change = 5):
    for edge in range(20):
        angle_change = random.randint(89,89) # 89 is the normal constant
        a_turtle.pensize(pen_size)
        a_turtle.forward(edge_size)
        a_turtle.left(angle_change)
        pen_size += pen_size_change
        edge_size += edge_size_change

    return 0

charlie = turtle.Turtle()
charlie.color("green")
draw_spiral(charlie)

canvas.mainloop() 


