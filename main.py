import random
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgpic(picname="images/space_2-transformed.png")
screen.register_shape("images/defender_2.gif")
screen.addshape("images/pngegg.gif")
screen.title("Ping Pong Avi 😉")
screen.tracer(False)

pong_ball = Ball()
pong_ball.hideturtle()
all_balls = []
turtle_color = ["red", "yellow", "green"]
x_positions = [-340, -300, -260, -220, -180, -140, -100, -60, -20]
y_positions = [160, 130, 100, 70, 40, 10]
move_direction = 10
all_tiles = []
all_beems = []
lives = 3
second = 1

# def moving(new_x, turtle):
#     turtle.goto(new_x, turtle.ycor())


def pong_move():
    global lives, second

    balls_to_remove = []
    tiles_to_remove = []

    for ball in all_balls:
        ball.move()
        if ball.ycor() > 300:
            ball.hideturtle()
            balls_to_remove.append(ball)
        for tile in all_tiles:
            if ball.distance(tile) < 20:
                tiles_to_remove.append(tile)
                balls_to_remove.append(ball)
                ball.hideturtle()
                ball.clear()
                tile.hideturtle()
                tile.clear()
                second = seconds(second)
                break

    for ball in balls_to_remove:
        all_balls.remove(ball)
    for tile in tiles_to_remove:
        all_tiles.remove(tile)

    screen.update()
    screen.ontimer(pong_move, 50)


def on_right_click():
    global pong_ball
    screen.tracer(False)
    pong_ball = Ball()
    pong_ball.goto(r_paddle.xcor(), r_paddle.ycor())
    pong_ball.showturtle()
    all_balls.append(pong_ball)




def beem_stop():
    global lives
    # print("I am here")
    for beem in all_beems:
        beem.sety(beem.ycor())
        if beem.distance(r_paddle) < 20:
            lives = 0
            update_lives()

        if beem.ycor() < -300:
            beem.hideturtle()
            all_beems.remove(beem)

def beem_move():
    global lives
    for beem in all_beems:
        beem.sety(beem.ycor() - 10)
        if beem.distance(r_paddle) < 20:
            lives -= 1
            update_lives()
            beem.hideturtle()
            all_beems.remove(beem)
        if beem.ycor() < -300:
            beem.hideturtle()
            all_beems.remove(beem)


    screen.update()
    screen.ontimer(beem_move, 500)

def beem_me():
    if all_tiles:
        rand_inv = random.randint(0, len(all_tiles) - 1)
        beem = Turtle()
        beem.penup()
        beem.shape("circle")
        beem.color("pink")
        beem.shapesize(stretch_len=0.1, stretch_wid=0.5)
        screen.tracer(False)
        beem.goto(all_tiles[rand_inv].xcor(), all_tiles[rand_inv].ycor())
        beem.showturtle()
        all_beems.append(beem)

    screen.ontimer(beem_me, 2500)




def update_lives():
    global move_direction
    global game_is_on
    lives_tur.clear()
    lives_tur.write(f"Lives: {lives}", font=("Comic Sans MS", 24, "normal"))
    if lives <= 0:
        new_tim = Turtle()
        new_tim.penup()
        new_tim.hideturtle()
        new_tim.color("white")
        new_tim.goto(-80, 0)
        new_tim.pendown()
        new_tim.write("Game Over", font=("Comic Sans MS", 24, "normal"))
        beem_stop()
        move_direction = 0
        game_is_on = False

def move_invaders():
    global move_direction
    for invader in all_tiles:
        invader.setx(invader.xcor() + move_direction)
        if invader.xcor() > 380 or invader.xcor() < -380:
            move_direction *= -1
            for invader in all_tiles:
                invader.sety(invader.ycor() - 20)
            break

    screen.update()
    screen.ontimer(move_invaders, 100)



def seconds(second):
    screen.tracer(True)
    second += 1
    # timer_tur.clear()
    # timer_tur.write(f"Timer: {second}", font=("Comic Sans MS", 24, "normal"))
    return second

# second = 1


locate = [random.randint(0, 33) for item in range(4)]

for index in range(len(y_positions)):
    for mindex in range(len(x_positions)):
        tim = Turtle()
        tim.penup()
        tim.shape("images/pngegg.gif")
        tim.shapesize(stretch_len=2, stretch_wid=1, outline=8)
        tim.goto(x=x_positions[mindex], y=y_positions[index])
        all_tiles.append(tim)

r_paddle = Paddle(0, -250, "Right", "Left")

# pong_ball = Ball()
# screen.update()


lives_tur = Turtle()
lives_tur.hideturtle()
lives_tur.penup()
lives_tur.goto(250, 250)
lives_tur.color("white")
lives_tur.pendown()
update_lives()
# lives_tur.write(f"Lives: {lives}", font=("Comic Sans MS", 24, "normal"))

timer_tur = Turtle()
timer_tur.hideturtle()
timer_tur.penup()
timer_tur.goto(-50, 250)
timer_tur.color("white")
timer_tur.pendown()
# timer_tur.write(f"Timer: {second}", font=("Comic Sans MS", 24, "normal"))
def high_scores():
    high_score = Turtle()
    high_score.hideturtle()
    high_score.penup()
    high_score.goto(-380, 250)
    high_score.color("white")
    high_score.pendown()
    with open("score.txt", "r+") as file:
        my_score = file.read()
        high_score.write(f"High Score: {my_score}", font=("Comic Sans MS", 24, "normal"))

game_is_on = True
screen.onkeypress(on_right_click, "space")
move_invaders()
pong_move()
beem_me()
beem_move()
# pong_move()

while game_is_on:
    screen.update()

    # Timer

    # screen.tracer(True)

    # Detect Win
    if not all_tiles:
        # screen.tracer(False)
        new_tim = Turtle()
        new_tim.color("white")
        new_tim.hideturtle()
        new_tim.penup()
        new_tim.goto(-80, 0)
        new_tim.write("You Won", font=("Comic Sans MS", 24, "normal"))
        timer_tur.write(f"Score: {second}", font=("Comic Sans MS", 24, "normal"))
        with open("score.txt", "r+") as file:
            my_score = file.read()
            if second > int(my_score):
                file.write(str(second))
        game_is_on = False

    # move_invaders()

    for tile in all_tiles:
        if tile.distance(r_paddle) < 30:
            new_tim = Turtle()
            new_tim.hideturtle()
            new_tim.penup()
            new_tim.goto(-80, 0)
            new_tim.color("white")
            new_tim.pendown()
            new_tim.write("Game Over", font=('Comic Sans MS', 24, 'normal'))
            move_direction = 0
            game_is_on = False





screen.exitonclick()
