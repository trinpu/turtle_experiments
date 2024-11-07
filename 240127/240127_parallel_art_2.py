from multiprocessing import Process
import turtle
import tkinter

def draw_square(a_turtle, direction): # purely designed to control behaviour
    """Draws a square, by default turns left"""
    for x in range(4):
        a_turtle.forward(200)
        a_turtle.left(direction)


main = tkinter.Tk()
canv = tkinter.Canvas(master=main)

alex = turtle.RawTurtle(canv)
alex.color('pink')
alex.speed(2) # speed basically is the number of updates to the canvas each second??

tess = turtle.RawTurtle(canv)
tess.color('red')
tess.speed(5)

alex_behaviour = Process(target=draw_square, args=(alex, 90))
tess_behaviour = Process(target=draw_square, args=(tess, -90))

alex_behaviour.start()
tess_behaviour.start()

alex_behaviour.join()
tess_behaviour.join()

# --REFERECES
# https://stackoverflow.com/questions/71941523/is-it-possible-to-use-turtle-without-the-graphics-window
# TypeError: cannot pickle '_tkinter.tkapp' object