import turtle
import random

def penGo(pen, x, y):
    pen.up()
    pen.ht()
    pen.goto(x, y)
    pen.st()
    pen.down()


def penGoDraw(pen, x, y):
    pen.goto(x, y)


def penDotDraw(pen, x, y):
    penGo(pen, x, y)
    pen.dot(3, "white")


# Coordinate properties
turtle.setworldcoordinates(-1000, -1000, 1000, 1000)

# Window
window = turtle.Screen()
window.bgcolor("black")  # Background color of window
window.title("Drawing Triangles")  # Title of window

# Pen
pen = turtle.Pen()
pen.speed(0)  # Speed of pen
pen.color("white")  # Color of pen

# Nodes (x, y)
A = [0, 600]
B = [550, -300]
C = [-550, -300]
nodeList = [A, B, C]

# Drawing main Triangle
pen.width(3)
penGo(pen, A[0], A[1])
penGoDraw(pen, B[0], B[1])
penGoDraw(pen, C[0], C[1])
penGoDraw(pen, A[0], A[1])
pen.width(1)

# Select random dot position for start
penDotDraw(pen, 100, 200)

# Selecting random one of the nodes
for i in range(10000):
    Node = random.choice(nodeList)
    penPos = pen.pos()
    nextDotPos = [(Node[0] + penPos[0]) / 2, (Node[1] + penPos[1]) / 2]
    penDotDraw(pen, nextDotPos[0], nextDotPos[1])

turtle.done()
