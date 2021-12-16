import turtle
import time

pen = turtle.Turtle()
pen.speed(1)

def curve():
    for i in range (200):
        pen.right(1)
        pen.forward(1)
def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(113)
    pen.end_fill()
    
def txt():
    pen.up()
    pen.setpos(-40,95)
    pen.down()
    pen.color('white')
    pen.write('I', font=('Verdana', 12, 'bold'))
    time.sleep(1)
    pen.setpos(-10,95)
    pen.write('L', font=('Verdana', 12, 'bold'))
    time.sleep(1)
    pen.setpos(0,95)
    pen.write('O', font=('Verdana', 12, 'bold'))
    time.sleep(1)
    pen.setpos(14,95)
    pen.write('V', font=('Verdana', 12, 'bold'))
    time.sleep(1)
    pen.setpos(26,95)
    pen.write('E', font=('Verdana', 12, 'bold'))
    time.sleep(1)
    pen.setpos(55,95)
    pen.write('Y', font=('Verdana', 12, 'bold'))
    time.sleep(1)
    pen.setpos(65,95)
    pen.write('o', font=('Verdana', 12, 'bold'))
    time.sleep(1)
    pen.setpos(75,95)
    pen.write('U', font=('Verdana', 12, 'bold'))


    
heart()
txt()
pen.ht()
time.sleep(5)