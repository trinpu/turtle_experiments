from turtle import Screen, Turtle

canvas = Screen()
canvas.bgcolor("#0F122A")
raffaele = Turtle()
raffaele.speed(8)
raffaele_colors = ["#50DC64", "#224E5C"]
edge_size = 10

for edge in range(80):
    if edge % 7 == 0:
        raffaele.color(raffaele_colors[1])
        edge_growth = 3
        angle_change = 90
    else:
        raffaele.color(raffaele_colors[0])
        edge_growth = 2
        angle_change = -89
    
    raffaele.forward(edge_size)
    raffaele.left(angle_change)
    edge_size += edge_growth
    

canvas.mainloop()
