import turtle as t
def rectangle(h,v,c):
    t.pendown()
    t.pensize()
    t.color(c)
    t.begin_fill()
    for counter in range(1,3):
        t.forward(h)
        t.right()
        t.forward(v)
        t.right(90)
    t.end_fill()
    t.penup()
t.speed(1)
t.goto(-100,-150)
rectangle(50,20,'blue')
t.goto(-30,-150)
rectangle(50,20,'blue')
