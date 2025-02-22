import math

def calculate_dt(ticks, previous_time):
    current_time = ticks
    dt = (current_time - previous_time) / 1000
    previous_time = current_time

    return dt, previous_time