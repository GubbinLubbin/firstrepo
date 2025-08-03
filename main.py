import time
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from boundry import Boundry

game_is_on=True
screen=Screen()
screen.setup(600,600)
screen.title("The Snake Game")
screen.bgcolor("black")

screen.tracer(0)
boundry=Boundry()



snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.right,"d")
screen.onkey(snake.left,"a")
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if(snake.head.distance(food)<15):
        if((scoreboard.score+1)%5==0 and scoreboard.score!=0):
            food.bigfood()
        else:
            food.newlocation()
        scoreboard.refresh()
        snake.increase_size()
    if(snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280):
        scoreboard.gameover()
        game_is_on=False
    for segments in snake.all_segments[1:]:
            if(snake.head.distance(segments)<10):
                scoreboard.gameover()
                game_is_on=False
            
screen.exitonclick()