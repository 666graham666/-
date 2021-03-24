import turtle

g = turtle.Turtle()

n = 1000000
sA = (n-2)*180
angle = sA//n

for i in range(n):
    g.forward(1)
    g.pendown()
    g.right(180-angle)

input()


