from turtle import *

def filled_circle(circle_size,circle_color):
    pencolor(circle_color)
    pensize(0)
    fillcolor(circle_color)
    begin_fill()
    circle(circle_size)
    end_fill()
