# DSE 2020 ICT Paper 2D Q1
# Written by Ha sir 😁
import turtle
import time

car = turtle.Turtle()
car.setheading(90)
car.color('blue')
car.pensize(5)
# shapes: “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”.
car.shape('turtle')
car.shapesize(1)
time.sleep(1)
steps = 20


def P(N):
    while N > 0:
        for i in range(1, N+1):
            car.forward(N*steps)
        car.right(90)
        for i in range(1, N+1):
            car.forward(N*steps)
        car.right(90)
        N = N - 1

# Actually, passing parameters in the following functions will be much better. However, since we are
# going to simulate the public exam question as much as possible, we use global for the variable dir 😅


def TE():
    global dir
    for i in range(1, (5 - dir + 1) % 4):
        car.right(90)
    dir = 1


def TW():
    global dir
    for i in range(1, 3 - dir + 1):
        car.right(90)
    dir = 3


def TN():
    global dir
    for i in range(1, 4 - dir + 1):
        car.right(90)
    dir = 0


def TS():
    global dir
    for i in range(1, (6 - dir + 1) % 4):
        car.right(90)
    dir = 2


def MOVE(X, Y, NX, NY):
    if NX > X:
        TE()
    else:
        TW()
    for i in range(1, NX - X + 1):
        car.forward(steps)
    if NY > Y:
        TN()
    else:
        TS()
    for i in range(1, NY - Y + 1):
        car.forward(steps)


# P(5)
dir = 0
# dir = TS(dir)
# print(dir)
MOVE(0, 0, 10, 1)
print(dir)

time.sleep(3)
