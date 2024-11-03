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


def start_counting_orb(clock, starting_mark, n_counts, pen_color, fill_color, delete_color, jump_forward_count, delete_backward_count, time_lag, clockwise=True):
    colored_mark_index = starting_mark
    for second in range(n_counts):
        # delete logic
        if clockwise:
            deleted_mark_index = (colored_mark_index - delete_backward_count) % n_hour_marks
        else:
            deleted_mark_index = (colored_mark_index + delete_backward_count) % n_hour_marks

        clock[deleted_mark_index].color(pen_color, delete_color)

        # color logic
        clock[colored_mark_index % n_hour_marks].color(pen_color, fill_color)
        if clockwise:
            colored_mark_index += jump_forward_count
        else:   
            colored_mark_index -= jump_forward_count

        time.sleep(time_lag)
    
    if clockwise:
        return colored_mark_index - 1
    else:
        return colored_mark_index + 1

## core behaviours
def bouncing_clock():
    """A colored hour mark counting forward and backwards"""
    colored_mark = start_counting_orb(clock, starting_mark, 12, pen_color, fill_color, delete_color, 1, 1, 0.3)
    colored_mark = start_counting_orb(clock, colored_mark, 12, pen_color, fill_color, delete_color, 1, 1, 0.3, False)
    colored_mark = start_counting_orb(clock, colored_mark, 12, pen_color, fill_color, delete_color, 1, 1, 0.3)



background_color = "#090c1f"
delete_color = background_color
pen_color = "#BFEDFF"
fill_color = "#6490CE"

canvas = turtle.Screen()
canvas.bgcolor(background_color)

n_hour_marks = 12
hour_hand_size = 200
hour_mark_heading = 90
turtle_shape_size = 1

starting_mark = 12

clock = create_clock(n_hour_marks, turtle_shape_size, pen_color, background_color, hour_hand_size, hour_mark_heading)


# ----------------- train orbs

### Less hacky solution

# PROBLEMS:
# 1. Sequential vs. Simultaneous paining
# 2. Transparency of fillcolor - train_colors = [(100, 144, 206, 1),(100, 144, 206, 0.75),(100, 144, 206, 0.5)]

train_colors = ["red","white","green"]
delete_backward_count = len(train_colors) + 1
moving_flag_index = [0, 11, 10] # will find a more elegant solution

for count in range(20):
    if count == 0:
        start_counting_orb(clock, moving_flag_index[0], 1, pen_color, train_colors[0], delete_color, 1, delete_backward_count, 0.1)
        clock[moving_flag_index[0 % 12]].fillcolor(delete_color)
    elif count == 1:
        start_counting_orb(clock, moving_flag_index[0], 1, pen_color, train_colors[0], delete_color, 1, delete_backward_count, 0.1)
        start_counting_orb(clock, moving_flag_index[1], 1, pen_color, train_colors[1], delete_color, 1, delete_backward_count, 0.1)
        clock[moving_flag_index[1] % 12].fillcolor(delete_color)
        clock[moving_flag_index[0] % 12].fillcolor(delete_color)
    else:
        start_counting_orb(clock, moving_flag_index[0], 1, pen_color, train_colors[0], delete_color, 1, delete_backward_count, 0.1)
        start_counting_orb(clock, moving_flag_index[1], 1, pen_color, train_colors[1], delete_color, 1, delete_backward_count, 0.1)
        start_counting_orb(clock, moving_flag_index[2], 1, pen_color, train_colors[2], delete_color, 1, delete_backward_count, 0.1)

        # this delete behavour is so fast that it seems simultaneous!
        # same logic could be applied to coloring behvavour
        clock[moving_flag_index[2] % 12].fillcolor(delete_color)
        clock[moving_flag_index[1] % 12].fillcolor(delete_color)
        clock[moving_flag_index[0] % 12].fillcolor(delete_color)

    moving_flag_index[0] += 1
    moving_flag_index[1] += 1
    moving_flag_index[2] += 1
    

canvas.mainloop()

    

