# From 24-01-25, Edited on 24-11-02
# Two non-related elements can co-exist in the same universe without intering with eachother

import turtle
import random

def draw_square(a_turtle, size):
    """A turtle will draw half a square"""
    edge_colors = ["#EBD615", "#EBA215"]
    for edge_number in range(1,5):
        a_turtle.color(edge_colors[edge_number % 2])
        a_turtle.forward(size)
        a_turtle.left(90)

def random_clock():
    n_hour_marks = 30
    hour_mark_size = 360 / n_hour_marks # degrees
    random_hour_mark = hour_mark_size * random.randint(1, n_hour_marks)
    return random_hour_mark

def draw_stars(a_turtle):
    """Pick a color, draw a star in random position with random pensize"""
    star_colors = ["#8499C1", "#EBD6D4"]
    star_color = star_colors[random.randint(0, len(star_colors)-1)]
    a_turtle.color(star_color)

    radius_size = random.randint(100, 400)
    angle_change = random_clock()
    a_turtle.shapesize(random.uniform(0.1, 0.8))

    a_turtle.penup()
    a_turtle.right(angle_change)
    a_turtle.forward(radius_size)
    a_turtle.stamp()
    a_turtle.forward(-radius_size)


def art_piece_behaviour(square_turtle, stars_turtle):
    square_turtle.shape('turtle')
    square_edge_size = 30
    square_turtle.speed(4)

    stars_turtle.shape('circle')

    for x in range(50):
        draw_square(square_turtle, square_edge_size)
        draw_stars(stars_turtle)
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