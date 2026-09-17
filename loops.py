import turtle
from turtle import *
t = Turtle()
t.speed(1000)


""" def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
square(7,90)

def doubleSquares(iRange):
    length = 5
    for i in range(iRange):
        square(length, 90)
        length = length * 1.07
        t.right(5)
doubleSquares(60) """

def triangle(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
triangle(7,120)

def doubleTriangle(iRange):
    length = 5
    for i in range(iRange):
        triangle(length, 120)
        length = length * 1.07
        t.left(75)
doubleTriangle(60)




""" for i in range(100):
    def square(x,y):
            t.forward(x)
            t.left(y)
            t.forward(x)
            t.left(y)
            t.forward(x)
            t.left(y)
            t.forward(x)
            t.left(y)
            t.left(5)
    square(200,90)


 """
""" for i in range(100):
    def triangle(x):
        t.forward(x)
        t.left(120)
        t.forward(x)
        t.left(120)
        t.forward(x)
        t.left(5)
    triangle(200) """


turtle.done()