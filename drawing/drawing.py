from turtle import Screen, Turtle

canvas = Screen()

def dragging(x, y):
    global size
    size = 10
    alex.ondrag(None) # https://docs.python.org/3/library/turtle.html#turtle.ondrag
    alex.setheading(alex.towards(x, y))
    alex.goto(x, y)
    alex.ondrag(dragging)

alex = Turtle()
alex.shape("turtle")
alex.speed(1)

canvas.listen()
alex.ondrag(dragging)

size = 10
for x in range(100):
    alex.forward(size)
    alex.left(89)
    size += 2


canvas.mainloop()

