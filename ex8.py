import turtle as t

t.shape('turtle')
x = 20


for i in range(1, x, 1):
    t.forward(20+30*i/x)
    t.left(90)

    
input()