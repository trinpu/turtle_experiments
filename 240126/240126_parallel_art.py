from multiprocessing import Process
import turtle

def draw_square(a_turtle, direction): # purely designed to control behaviour
    """Draws a square, by default turns left"""
    for x in range(4):
        a_turtle.forward(200)
        a_turtle.left(direction)


wn = turtle.Screen()
wn.bgcolor("black")

alex = turtle.Turtle()
alex.color('pink')
alex.speed(2)

tess = turtle.Turtle()
tess.color('red')
tess.speed(5)

alex_behaviour = Process(target=draw_square, args=(alex, 90))
tess_behaviour = Process(target=draw_square, args=(tess, -90))

alex_behaviour.start()
tess_behaviour.start()

alex_behaviour.join()
tess_behaviour.join()

# https://stackoverflow.com/questions/70318766/tkinter-and-multiprocessing-cannot-pickle-tkinter-tkapp-object


