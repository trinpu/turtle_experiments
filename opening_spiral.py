import turtle
import random

canvas = turtle.Screen()
canvas.bgcolor("black")

alex = turtle.Turtle()
alex.color('green')
alex.pensize(5)

charlie = turtle.Turtle()
charlie.color('yellow')

edge_size = 20
angle = 105
n_edges = 4 * 10

def draw_shape(a_turtle, edge_size, angle,n_edges, is_rose=True):
    """Draws a random shape, similar to a star"""
    for edge in range(4 * 10):
        a_turtle.forward(edge_size)
        a_turtle.left(angle)

        if is_rose:
            angle -= 1
        else:
            angle += 1

        edge_size += 10
    
    return 0

draw_shape(alex, edge_size, angle, n_edges)
draw_shape(charlie, edge_size, angle, n_edges, False)

canvas.mainloop()