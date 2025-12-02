from turtle import *
import time

from snake import *
from food import Food

import sys


screen=Screen()
screen.title("My Snake Game")
screen.bgcolor("black")
screen.setup(width=800,height=800)

screen.tracer(0)

snake=Snake()
# snake class is being called

snake.create_snake()
# snake is being displayed

food=Food()
# food module is being called

# this is the code that make the keys functionable
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
screen.onkey(snake.down,"Down")

game_on=True
while game_on:
    screen.update()
    time.sleep(0.18)
    snake.move()
    snake.exit()
    snake.self_harm()
    # now for detection and collision of food
    if snake.segments[0].distance(food)<15:
        print("good")
        food.refresh()

screen.exitonclick()
