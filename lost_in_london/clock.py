import turtle
import time

def create_clock(n_hour_marks, turtle_shape_size, pen_color, fill_color, hour_hand_size, hour_mark_heading):
    """Creates a clock of hour marks, return a list with clock wise turtles positioned as the hour marks"""

    hour_mark_angle = 360 / n_hour_marks
    hour_marks = []

    for mark in range(n_hour_marks):
        a_turtle = turtle.Turtle()
        a_turtle.speed(6)
        a_turtle.shape('circle')
        a_turtle.setheading(hour_mark_heading)
        a_turtle.shapesize(turtle_shape_size)
        a_turtle.color(pen_color, fill_color)
        a_turtle.penup()
        a_turtle.forward(hour_hand_size)
        hour_mark_heading -= hour_mark_angle
        hour_marks.append(a_turtle)

    return hour_marks


def start_counting_orb(clock, starting_mark, n_counts, pen_color, fill_color, delete_color, jump_forward_count, delete_backward_count, cloclwise=True):
    colored_mark_index = starting_mark
    for second in range(n_counts):
        # delete logic
        if cloclwise:
            deleted_mark_index = (colored_mark_index - delete_backward_count) % n_hour_marks
        else:
            deleted_mark_index = (colored_mark_index + delete_backward_count) % n_hour_marks

        clock[deleted_mark_index].color(pen_color, delete_color)

        # color logic
        clock[colored_mark_index % n_hour_marks].color(pen_color, fill_color)
        if cloclwise:
            colored_mark_index += jump_forward_count
        else:   
            colored_mark_index -= jump_forward_count

        time.sleep(0.5)
    
    return deleted_mark_index 


background_color = "#090c1f"
delete_color = background_color
pen_color = "#BFEDFF"
fill_color = "#6490CE"
fill_colors = []

canvas = turtle.Screen()
canvas.bgcolor(background_color)

n_hour_marks = 12
hour_hand_size = 200
hour_mark_heading = 90
turtle_shape_size = 1

clock = create_clock(n_hour_marks, turtle_shape_size, pen_color, background_color, hour_hand_size, hour_mark_heading)

# clock = create_clock(n_hour_marks, hour_hand_size, pen_color, fill_color, hour_mark_heading, turtle_shape_size)
# colored_mark = start_counting_orb(clock, n_hour_marks, pen_color, fill_color, delete_color, 12, 1,1)


# colored_mark = 12
# for second in range(12):
#     uncolored_mark = (colored_mark + 1) % n_hour_marks
#     clock[uncolored_mark].color(pen_color, background_color)
#     clock[colored_mark % n_hour_marks].color(pen_color, fill_color)
#     colored_mark -= 1
#     time.sleep(0.5)



    

canvas.mainloop()

    

