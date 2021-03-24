import turtle as t

t.speed(0)


def duga(R):
    for i in range(90):
        t.forward(R * 0.0349)


t.right(2)


def crug(R):
    t.penup()

    t.forward(R)
    t.right(90)
    t.pendown()
    duga(R)
    duga(R)
    t.penup()
    t.left(90)
    t.backward(R)
    t.pendown()

    t.begin_fill()
    duga(100)
    duga(100)
    t.color("yellow")
    t.end_fill()
    t.color("black")

    t.begin_fill()
    t.right(60)
    t.penup()
    t.forward(60)
    t.pendown()
    crug(15)
    t.penup()
    t.backward(60)
    t.color("blue")
    t.end_fill()
    t.color("black")

    t.begin_fill()
    t.right(60)
    t.forward(60)
    t.pendown()
    crug(15)
    t.penup()
    t.backward(60)
    t.color("blue")
    t.end_fill()
    t.color("black")

    t.width(8)
    t.left(30)
    t.forward(80)
    t.pendown()
    t.forward(30)

    t.color("red")
    t.penup()
    t.forward(10)
    t.left(90)
    t.forward(70)
    t.right(90)
    t.pendown()
    duga(70)


input()
