import turtle


g = turtle.Turtle()


g.shape("turtle")
g.speed(0)
x = 1
while True:
    g.forward(2)
    g.left(1)
    if (x % 360) == 1:
        g.clear()
    x += 1

input()