# From 24-01-25, Edited on 24-11-02
# Two non-related elements can co-exist in the same universe without intering with eachother

import turtle
import random

def draw_half_square(a_turtle, size):
    """A turtle will draw half a square"""
    for color in ["#EBD615", "#EBA215"]: # yello and organge
        a_turtle.color(color)
        a_turtle.forward(size)
        a_turtle.left(90)

def draw_random_radius(a_turtle):
    """A turtle will draw a random radius"""
    radius_size = random.randint(100, 400)
    change_coefficient = 360 / 30
    angle_change = change_coefficient * random.randint(1, change_coefficient)
    a_turtle.penup()
    a_turtle.color("#EBD6D4") # or 8499C1
    a_turtle.right(angle_change)
    a_turtle.forward(radius_size)
    a_turtle.stamp()
    a_turtle.forward(-radius_size)


def art_piece_behaviour(square_turtle, clock_turtle):
    square_turtle.shape('turtle')
    square_edge_size = 30
    square_turtle.speed(4)

    for x in range(50):
        draw_half_square(square_turtle, square_edge_size)
        draw_random_radius(clock_turtle)
        draw_half_square(square_turtle, square_edge_size)
        square_turtle.forward(square_edge_size / 2)
        square_turtle.left(25)
        square_edge_size += 5


wn = turtle.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgcolor("#232A6B") #dark blue
wn.title("A small universe")

alex = turtle.Turtle()
tess = turtle.Turtle()

art_piece_behaviour(alex, tess)

wn.mainloop()