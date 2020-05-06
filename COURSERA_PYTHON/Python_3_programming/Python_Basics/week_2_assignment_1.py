import turtle
win=turtle.Screen()
my_tur=turtle.Turtle()
my_tur.speed(0)
distance=20
for i in range(20):
    my_tur.forward(distance)
    my_tur.left(90)
    distance+=5
win.exitonclick()