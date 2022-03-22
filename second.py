import turtle

c=turtle.Turtle()
c.getscreen().bgcolor("black")
c.color("red","yellow")
c.speed(10)

dist = 250

while dist > 0:
    c.forward(dist)
    c.left(-90)
    c.forward(dist)
    c.right(90)
    dist -= 6
    c.forward(dist)
    c.left(-90)
    c.forward(dist)
    dist -= 6
    c.left(-90)

turtle.done()