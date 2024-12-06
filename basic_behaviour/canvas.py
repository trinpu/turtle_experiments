import turtle

canvas = turtle.Screen()
canvas.setup(width=0.5, height=0.75)
canvas.bgcolor("black")

# only this last instance will be displayed
window = turtle.Screen()
window.setup(width=0.75, height=0.5)
window.bgcolor("blue")

canvas.mainloop()