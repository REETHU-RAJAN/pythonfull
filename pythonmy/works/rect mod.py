import turtle
t=turtle.Turtle()
t.fillcolor("red")
t.begin_fill()
for i in range(2):

    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)
t.end_fill()
turtle.done()