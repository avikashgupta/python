from turtle import Turtle, Screen

avi = Turtle()
screen = Screen()

def forward():
    avi.forward(10)

def backward():
    avi.backward(10)

def left():
    avi.left(10)

def right():
    avi.right(10)
    
def clear():
    avi.clear()
    avi.penup()
    avi.home()
    avi.pendown()

screen.listen()

screen.onkey(key="w",fun = forward)
screen.onkey(key="s",fun = backward)
screen.onkey(key="a",fun = left)
screen.onkey(key="d",fun = right)
screen.onkey(key="c",fun = clear)

screen.exitonclick()
