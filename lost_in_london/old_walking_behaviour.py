def walking_orbs(orbs_colors, n_steps):
    """Create three obs one by one. Orbs walk forward by 1 step lasting n seconds (pulse duration)"""
    delete_backward_count = len(orbs_colors) + 1

    starting_index = n_hour_marks % n_hour_marks # staring from 0
    moving_flag_index = [starting_index, n_hour_marks - 1, n_hour_marks - 2]
    time_lag = 0 # rename to coloring_lag
    pulse_duration = 1 # rename to pulse_duration

    for count in range(n_steps):
        if count == 0:
            start_counting_orb(clock, moving_flag_index[0], 1, pen_color, orbs_colors[0], delete_color, 1, delete_backward_count, time_lag)
            time.sleep(pulse_duration)
            clock[moving_flag_index[0 % n_hour_marks]].fillcolor(delete_color) # remove the 12 to support more hour hands
        elif count == 1:
            start_counting_orb(clock, moving_flag_index[1], 1, pen_color, orbs_colors[1], delete_color, 1, delete_backward_count, time_lag)
            start_counting_orb(clock, moving_flag_index[0], 1, pen_color, orbs_colors[0], delete_color, 1, delete_backward_count, time_lag)
            time.sleep(pulse_duration)
            clock[moving_flag_index[0] % n_hour_marks].fillcolor(delete_color)
            clock[moving_flag_index[1] % n_hour_marks].fillcolor(delete_color)
        else:
            start_counting_orb(clock, moving_flag_index[0], 1, pen_color, orbs_colors[0], delete_color, 1, delete_backward_count, time_lag)
            start_counting_orb(clock, moving_flag_index[1], 1, pen_color, orbs_colors[1], delete_color, 1, delete_backward_count, time_lag)
            start_counting_orb(clock, moving_flag_index[2], 1, pen_color, orbs_colors[2], delete_color, 1, delete_backward_count, time_lag)

            time.sleep(pulse_duration)

            clock[moving_flag_index[2] % n_hour_marks].fillcolor(delete_color)
            clock[moving_flag_index[1] % n_hour_marks].fillcolor(delete_color)
            clock[moving_flag_index[0] % n_hour_marks].fillcolor(delete_color)

        moving_flag_index[0] += 1
        moving_flag_index[1] += 1
        moving_flag_index[2] += 1