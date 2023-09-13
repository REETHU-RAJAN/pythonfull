# Python program to draw hexagon
# using Turtle Programming
import turtle

polygon = turtle.Turtle()

num_sides = 6
side_length = 70
angle = 360.0 / num_sides
polygon.fillcolor("red")
polygon.begin_fill()
for i in range(num_sides):


    polygon.forward(side_length)

    polygon.right(angle)

polygon.end_fill()

turtle.done()
