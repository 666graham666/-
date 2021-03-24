import turtle

turtle.shape('turtle')

m = 360/12
n = 12
while n > 0:
    turtle.forward(50)
    turtle.stamp()
    turtle.backward(50)
    turtle.left(m)

    n -= 1

input()