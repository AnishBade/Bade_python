import turtle
win=turtle.Screen()
babe=turtle.Turtle()
babe.color("purple")
distance=50
for i in range(14):
    babe.forward(distance)
    babe.left(90)
    distance+=10
babe.color("green")
for i in range(14):
    babe.forward(distance)
    babe.left(90)
    distance+=10
babe.color("red")
for i in range(14):
    babe.forward(distance)
    babe.left(90)
    distance+=10
babe.color("blue")
for i in range(14):
    babe.forward(distance)
    babe.left(90)
    distance+=10

win.exitonclick()