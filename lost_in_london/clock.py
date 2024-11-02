import turtle

background_color = "#090c1f"
pen_color = "#BFEDFF"
fill_color = "#6490CE"

canvas = turtle.Screen()

canvas.bgcolor(background_color)

n_hour_marks = 12
hour_mark_angle = 360 / n_hour_marks
hour_hand_size = 200
hour_mark_heading = 90
hour_marks = []


for mark in range(n_hour_marks):
    a_turtle = turtle.Turtle()
    a_turtle.speed(6)
    a_turtle.shape('circle')
    a_turtle.setheading(hour_mark_heading)
    a_turtle.shapesize(1)
    a_turtle.color(pen_color, background_color)
    a_turtle.penup()
    a_turtle.forward(hour_hand_size)
    hour_mark_heading -= hour_mark_angle
    hour_marks.append(a_turtle)

canvas.mainloop()

    

