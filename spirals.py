from turtle import Screen, Turtle

canvas = Screen()

alex = Turtle()
josh = Turtle()
josh.color("#808080")
josh.setheading(90)
edge_size = 20
angle_change = 89

for edge in range(100):
    alex.forward(edge_size)
    josh.forward(edge_size)
    alex.left(angle_change)
    josh.right(angle_change)
    edge_size += 5

canvas.mainloop()
