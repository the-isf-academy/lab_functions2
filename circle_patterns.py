from turtle import *
import random

def filled_circle(circle_size,circle_color):
    fillcolor(circle_color)
    begin_fill()
    circle(circle_size)
    end_fill()

def alternating_pattern(num_circles, circle_size):
    for i in range (num_circles):
        if i%2 == 0:
            filled_circle(circle_size, "blue")
        else:
            filled_circle(circle_size, "cyan")
        penup()
        forward(circle_size*2)
        pendown()

def bullseye_pattern(num_circles, starting_circle_size):
    unit = starting_circle_size/num_circles
    for i in range (num_circles):
        if i%2 == 0:
            filled_circle(unit*(5-i), "orange")
        else:
            filled_circle(unit*(5-i), "cyan")
        penup()
        left(90)
        forward(unit)
        right(90)

def size_pattern(num_columns, num_rows, color):
    penup()
    goto(-300,300)
    for j in range (num_rows):
        for i in range (num_columns):
            pendown()
            filled_circle(10*(j+1),color)
            penup()
            forward(600/num_columns)
        penup()
        goto(-300,300-(j+1)*600/num_rows)
        pendown()

def halftone_pattern(num_columns, num_rows, color1, color2):
    penup()
    goto(-300,300)
    for j in range (num_rows):
        for i in range (num_columns):
            pendown()
            filled_circle(30,color1)
            penup()
            forward(15)
            right(90)
            forward(15)
            left(90)
            filled_circle(30,color2)
            left(90)
            forward(15)
            right(90)
            forward(600/num_columns)
        penup()
        goto(-300,300-(j+1)*600/num_rows)
        pendown()

def thick_circle(circle_size, circle_color, thickness):
    pensize(thickness)
    pencolor(circle_color)
    circle(circle_size)

def random_pattern(num_circles, background_color):
    bgcolor(background_color)

    for i in range (num_circles):
        goto(random.randint(-300,300),random.randint(-300,300))
        num = random.randint(50,200)
        pendown()
        colormode(255)
        if num%2 == 0:
            filled_circle(num, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        else:
            thick_circle(num, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), random.randint(10,20))
        penup()
    
speed(0)
# alternating_pattern(5,50)
# bullseye_pattern(5,200)
# size_pattern(6,5,'coral')
# halftone_pattern(6,5,'dark blue','light blue')
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
random_pattern(5, "black")

input()