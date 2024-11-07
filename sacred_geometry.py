from turtle import Screen, Turtle

canvas = Screen()

alex = Turtle()
alex.speed(8)
josh = Turtle()
josh.speed(8)
josh.color("#b3b3b3")
josh.setheading(90)
edge_size = 10
angle_change = 89

for edge in range(180):
    alex.forward(edge_size)
    josh.forward(edge_size)
    alex.left(angle_change)
    josh.right(angle_change)
    edge_size += 2

canvas.mainloop()
