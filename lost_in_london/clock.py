import turtle
import time

def create_clock(n_hour_marks, hour_hand_size, hour_mark_heading, turtle_shape_size):
    """Creates a clock of hour marks, return a list with clock wise turtles positioned as the hour marks"""

    hour_mark_angle = 360 / n_hour_marks
    hour_marks = []

    for mark in range(n_hour_marks):
        a_turtle = turtle.Turtle()
        a_turtle.speed(6)
        a_turtle.shape('circle')
        a_turtle.setheading(hour_mark_heading)
        a_turtle.shapesize(turtle_shape_size)
        a_turtle.color(pen_color, background_color)
        a_turtle.penup()
        a_turtle.forward(hour_hand_size)
        hour_mark_heading -= hour_mark_angle
        hour_marks.append(a_turtle)

    return hour_marks

background_color = "#090c1f"
pen_color = "#BFEDFF"
fill_color = "#6490CE"

canvas = turtle.Screen()
canvas.bgcolor(background_color)

n_hour_marks = 12
hour_hand_size = 200
hour_mark_heading = 90
turtle_shape_size = 1

clock = create_clock(n_hour_marks, hour_hand_size, hour_mark_heading, turtle_shape_size)

colored_mark = 12
for second in range(12):
    uncolored_mark = (colored_mark - 1) % n_hour_marks
    clock[uncolored_mark].color(pen_color, background_color)
    clock[colored_mark % n_hour_marks].color(pen_color, fill_color)
    colored_mark += 1
    time.sleep(1)
    

canvas.mainloop()

    

