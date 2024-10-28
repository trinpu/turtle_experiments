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


def experiment_spiral(a_turtle, pen_size=1, pen_size_change=0, edge_size = 20, edge_size_change = 5):

    n_edges = 4 * 1 # 1 is for single spiral
    angle_remeinder = 89 * n_edges
    
    edge_remeinder = sum([x for x in range(n_edges)]) # must figure out the logic. [10, 15, 20, 25] == 70 == (10*4) + 30

    angle_changes = []
    edges_sum = []

    for edge in range(n_edges):
        if edge < 3:  
            angle_size = random.randint(0, 89)
            edge_size = random.randint(0, edge_size + edge_size_change)

            a_turtle.forward(edge_size)
            a_turtle.left(angle_size)

            angle_remeinder -= angle_size
            edge_remeinder -= edge_size
        else:
            angle_size = angle_remeinder
            edge_size = edge_remeinder

            a_turtle.forward(edge_size)
            a_turtle.left(angle_size)

    return 0

charlie = turtle.Turtle()
charlie.color("green")
draw_spiral(charlie)

frank = turtle.Turtle()
frank.color("yellow")
experiment_spiral(frank)

    

canvas.mainloop() 


