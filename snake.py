from turtle import Turtle, Screen
import random
import time

starting_pos = [(0,0),(-20,0),(-40,0)]
move_dis = 20
up = 90
down = 270
left = 180
right = 0


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        
    def create_snake(self):
        for i in starting_pos:
            self.addseg(i)
            
    def move(self):
        for i in range(len(self.segment)-1,0,-1):
            new_x = self.segment[i-1].xcor()
            new_y = self.segment[i-1].ycor()
            self.segment[i].goto(new_x,new_y)
        self.head.forward(move_dis)
        
    def up(self):
        if self.head.setheading != down:
            self.head.setheading(up)
        
    def down(self):
        if self.head.setheading != up:
            self.head.setheading(down)
        
    def left(self):
        if self.head.setheading != right:
            self.head.setheading(left)
        
    def right(self):
        if self.head.setheading != left:
            self.head.setheading(right)
    
    def addseg(self,position):
        seg = Turtle("square")
        seg.color("white")
        seg.penup()
        seg.goto(position)
        self.segment.append(seg)
    
    def extend(self):
        self.addseg(self.segment[-1].position())

class Food(Turtle):
    def __init__(self):
        super().__init__(self)
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_width = 0.5)
        self.color("blue")
        self.speed("fatest")
        self.refresh()
        
    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.scorebo()
        self.hideturtle()
        
    def scorebo(self):
        self.write(f"Score: {self.score}",align="center",font=("Arial",20,"normal"))
        
    def increase(self):
        self.score +=1
        self.clear()
        self.scorebo()
        
    def gameover(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=("Arial",20,"normal"))
        
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


on = True

while on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #Detect collision
    
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase()
        
    #Detect collision with wall
    
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor>280 or snake.head.ycor<-280:
        on = False
        score.gameover()
        
    #Detect collision with tail
    
    for i in snake.segment:
        if i == snake.head:
            pass
        if snake.head.distance(i)<10:
            on = False
            score.gameover()
    
screen.exitonclick()
