import turtle

turtle.shape('turtle')
turtle.left(90)
n = 50

def but(n):
    turtle.circle(n)
    turtle.circle(-n)


x = 1

while x <=20:
    but(n)

    n += 5
    x += 1

input()

