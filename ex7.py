import turtle
import math

g = turtle.Turtle()
g.shape('turtle')
x = 0
while True:
    g.forward(x / 2 * math.pi)
    g.left(2 * math.pi)
    x += 0.1

input()