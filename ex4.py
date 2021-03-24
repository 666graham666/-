
import turtle

g = turtle.Turtle()

turtle.shape('turtle')
t = 10
k = 5
while t <= 100:
    g.forward(t)
    g.right(90)
    g.forward(t)
    g.right(90)
    g.forward(t)
    g.right(90)
    g.forward(t)
    g.right(90)
    g.penup()
    g.goto(-k,k)
    g.pendown()
    t += 10
    k += 5

input()