import turtle
import math
g = turtle.Turtle()
g.shape('turtle')
R = 30
x = 1
n = 3
g.up()
g.goto(R, 0)
g.down()
def polygon(x):
    while x <= n:
        g.left((180 - 360 / n) / 2)
        g.left(360 / n)
        g.forward(2 * R * math.sin(math.pi/n))
        x += 1
        g.right((180 - 360 / n) / 2)
while n <= 11:
    polygon(x)
    n += 1
    R += 18
    g.up()
    g.goto(R, 0)
    g.down()


input()