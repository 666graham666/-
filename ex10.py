import turtle

t = turtle.Turtle()
turtle.shape('turtle')

x = 1
n = 6

def chvetok(x):
    while x <= n:
        t.circle(50)
        t.left(360 / n)
        x += 1

chvetok (x)

input()