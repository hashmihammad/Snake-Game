import time
from turtle import Screen

from food import Food
from snake import Snake
from scoreboard import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or \
       snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()

    for segment in snake.segment:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()
