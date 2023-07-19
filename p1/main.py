from turtle import Turtle, Screen
from  snake import Snake
from FOOD import Food
from score  import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

snake = Snake()
food  = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_running = True
while game_is_running:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # detection of food
    if snake.seg[0].distance(food) < 15:
        food.refresh()
        snake.get_long()
        score.incerease_score()
       
       # head collision with tail 
    for segment in snake.seg:
        if segment == snake.seg[0]:
            pass
        elif snake.seg[0].distance(segment) < 10 :
            game_is_running = False
            score.end()
                    
    #when it setect a wall
    if snake.seg[0].xcor() < -290:
        posi  = snake.seg[0].position()
        x= -posi[0]
        y = posi[1]
        snake.seg[0].goto(x,y)
        
    elif snake.seg[0].xcor() > 290:
        posi  = snake.seg[0].position()
        x= -posi[0]
        y = posi[1]
        snake.seg[0].goto(x,y)
    
    
        
    if snake.seg[0].ycor() <  -290:
        posi  = snake.seg[0].position()
        x = posi[0]
        y = -posi[1]
        snake.seg[0].goto(x,y)
    elif snake.seg[0].ycor() > 290:
        posi  = snake.seg[0].position()
        x = posi[0]
        y = -posi[1]
        snake.seg[0].goto(x,y)
            
        
    # elif snake.seg[0].xcor() < -290:
    #     p = snake.seg[0].pos()
    #     snake.seg[0].setheading(180)
    #     snake.seg[0].goto(p[0], p[1])


screen.exitonclick()