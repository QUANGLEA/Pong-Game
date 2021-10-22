import turtle
import os 

# Making Pong Game in Python
# By: Quang Le
 
window = turtle.Screen()
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer()

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=4, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B 
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=4, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.speedx = 5 
ball.speedy = 5

#Score
score_a = 0
score_b = 0

#Result
result = turtle.Turtle()
result.speed(0)
result.color("blue")
result.penup()
result.goto(0, 250)
result.hideturtle()
result.write("Player A: {}              Player B: {}".format(score_a, score_b), align="center", font=("Courier", 26, "normal"))

#Game Over
over = turtle.Turtle()
over.speed(0)
over.penup()
over.hideturtle()
over.color("white")
over.goto(0, 60)

# Function 
def up_paddle_a():
    y = paddle_a.ycor()
    y += 15
    paddle_a.sety(y)

def down_paddle_a():
    y = paddle_a.ycor()
    y -= 15
    paddle_a.sety(y)

def up_paddle_b():
    y = paddle_b.ycor()
    y += 15
    paddle_b.sety(y)

def down_paddle_b():
    y = paddle_b.ycor()
    y -= 15
    paddle_b.sety(y)

# Keyboard binding
window.listen()
window.onkeypress(up_paddle_a, 'w')
window.onkeypress(down_paddle_a, 's')
window.onkeypress(up_paddle_b, 'Up')
window.onkeypress(down_paddle_b, 'Down')

# Main Game 
while True:
    window.update()

    # Ball Movement
    ball.setx(ball.xcor() + ball.speedx)
    ball.sety(ball.ycor() + ball.speedy)

    # Hit Border 
    if ball.ycor() < -288:
        ball.sety(-288)
        ball.speedy *= -1
        os.system("afplay Border.wav&")

    if ball.ycor() > 288:
        ball.sety(288)
        ball.speedy *= -1
        os.system("afplay Border.wav&")

    if ball.xcor() < -388:
        ball.goto(0, 0)
        ball.speedx *= -1
        score_b += 1
        result.clear()
        result.write("Player A: {}              Player B: {}".format(score_a, score_b), align="center", font=("Courier", 26, "normal"))

    if ball.xcor() > 388:
        ball.goto(0, 0)
        ball.speedx *= -1
        score_a += 1
        result.clear()
        result.write("Player A: {}              Player B: {}".format(score_a, score_b), align="center", font=("Courier", 26, "normal"))

    # Hit Paddle
    if ball.xcor() < -340 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.speedx *= -1
        os.system("afplay Paddle.wav&")

    if ball.xcor() > 340 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.speedx *= -1
        os.system("afplay Paddle.wav&")

    #Check Game Over
    if score_a == 2:
        result.clear()
        os.system("afplay Score.wav&")
        over.write("Player A Wins!", align="center", font=("Courier", 26, "normal"))
        window.exitonclick()
        
    if score_b == 2:
        result.clear()
        os.system("afplay Score.wav&")
        over.write("Player B Wins!", align="center", font=("Courier", 26, "normal"))
        window.exitonclick()
    
    
    

    
    

    

     



