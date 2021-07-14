import time
from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard

# initialing screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.listen()
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

# main loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.update()

    # collision with border
    if snake.head.pos()[0] < -280 or snake.head.pos()[0] > 280 or \
            snake.head.pos()[1] < -280 or snake.head.pos()[1] > 280:
        scoreboard.reset()
        snake.reset()

    # collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset()

    # eating
    if snake.head.distance(food) < 15:
        food.change_position()
        scoreboard.increase_score()
        snake.get_tail()

screen.exitonclick()

snake.right()
snake.left()
snake.down()
snake.up()
