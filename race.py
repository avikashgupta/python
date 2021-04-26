from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500,height=400)

user_bet = screen.textinput(title="Make your bet",prompt="Enter a color: ")

empty = []

colours =["red","purple","black","blue"]

y_pos = 100

for i in range(0,4):
    avi = Turtle(shape="turtle")
    avi.color(colours[i])
    avi.penup()
    avi.goto(x=-230,y=-y_pos)
    y_pos = y_pos - 30
    empty.append(avi)

on = True

while on:
    for j in empty:
        if j.xcor()>230:
            on = False
            win = j.pencolor()
            if win == user_bet:
                print(f"You won! {win}")
            else:
                print(f"You lost! Winner is {win}")
        distance = random.randint(0,10)
        j.forward(distance)
    
screen.exitonclick()
