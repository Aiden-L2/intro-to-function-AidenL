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
    for i in range(5):
        t.forward(x)
        t.left(y)
triangle(5,144)

def doubleTriangle(iRange):
    length = 8
    for i in range(iRange):
        triangle(length, 144)
        length = length * 1.07
        t.right(5)
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

""" 
#string for characters
name = "Aiden"
print(name.lower().capitalize())
#input asks the user a question and records the answer
#what we write in input argument is what users sees
#input always outputs a string
bill = int(input("how much was the bill"))
print(bill)

if bill ==10:
    print("match")
else:
    print("no match")
#integer for whole number
amt = 100
#float uses decimal
amt = 99.99

#boolean
x = True
y = False
 """