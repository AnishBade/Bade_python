import turtle
win=turtle.Screen()
babe=turtle.Turtle()
babe.speed(0)
babe.color("purple")
distance=0.1
angle=8
range1=20
for j in range(5):
    for i in range(range1):
        babe.forward(distance)
        babe.left(angle)
        distance+=0.1
    babe.color("green")
    for i in range(range1):
        babe.forward(distance)
        babe.left(angle)
        distance+=0.1
    babe.color("red")
    for i in range(range1):
        babe.forward(distance)
        babe.left(angle)
        distance+=0.1
    babe.color("blue")
    for i in range(range1):
        babe.forward(distance)
        babe.left(angle)
        distance+=0.1

win.exitonclick()