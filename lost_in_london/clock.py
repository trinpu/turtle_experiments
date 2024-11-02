import turtle


canvas = turtle.Screen()
canvas.bgcolor("#090c1f")

n_hour_marks = 12
hour_mark_angle = 360 / n_hour_marks
hour_hand_size = 200
hour_mark_heading = 0
hour_marks = []

for mark in range(n_hour_marks):
    a_turtle = turtle.Turtle()
    a_turtle.shape('circle')
    a_turtle.setheading(hour_mark_heading)
    a_turtle.shapesize(1)
    a_turtle.color("#EBD615", "#EBA215")
    a_turtle.penup()
    a_turtle.forward(hour_hand_size)
    hour_mark_heading += hour_mark_angle
    hour_marks.append(a_turtle)

canvas.mainloop()

    

