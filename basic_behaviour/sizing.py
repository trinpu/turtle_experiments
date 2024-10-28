# ref https://docs.python.org/3/library/turtle.html

import turtle

canvas = turtle.Screen()
canvas.bgcolor("black")

the_turtle = turtle.Turtle()
the_turtle.color("green")

pen_size = 1
pen_size_change = 1
edge_size = 50
edge_size_change = 10

for edge in range(50):
    the_turtle.pensize(pen_size)
    the_turtle.forward(edge_size)
    the_turtle.left(89)
    pen_size += pen_size_change
    edge_size += edge_size_change

    

canvas.mainloop() 


