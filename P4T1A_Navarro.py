# The turtle will ask you how many squares do you want to draw. Enter a number and
# the turtle will draw the the square depending the number you put in. 
# 10-14-2019
# CTI-110 P4T2 - Bug Collector
# Alexis Navarro
#

import turtle

num_squares = 3
t = turtle.Turtle()
t.pendown()
side = side_unit = 30

while True:
    try:
        num_squares = int(input('How many squares do you want?'))
    except ValueError:
        print("How many squares do you want?") # The user will be asked for number of squares.
    
    if num_squares > 3:
        break

for sq in range(1, num_squares + 1):
    t.left(90)
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.left(90)
    side = side_unit + 3 * sq  

    t.goto(0,0)                

turtle.done()
