import turtle

wn = turtle.Screen()
wn.title("pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # speed of animation, not the speed of the paddle
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # default is 20px by 20px
paddle_a.penup()  # don't draw a line when moving
paddle_a.goto(-350, 0)  # start position

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # default is 20px by 20px
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)  # animation speed
pen.color("white")
pen.penup()
pen.hideturtle()  # hide the pen
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Function
def paddle_a_up():
    y = paddle_a.ycor()  # returns y coordinate
    y += 20  # add 20 pixels to y
    paddle_a.sety(y)  # set y to new y


def paddle_a_down():
    y = paddle_a.ycor()  # returns y coordinate
    y -= 20  # sub 20 pixels to y
    paddle_a.sety(y)  # set y to new y


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()  # listen for keyboard input
wn.onkeypress(paddle_a_up, "w")  # when user presses w, call paddle_a_up function
wn.onkeypress(paddle_a_down, "s")  # when user presses s, call paddle_a_down function
wn.onkeypress(
    paddle_b_up, "Up"
)  # when user presses up arrow, call paddle_b_up function
wn.onkeypress(
    paddle_b_down, "Down"
)  # when user presses down arrow, call paddle_b_down function

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)  # setx() changes x coordinate
    ball.sety(ball.ycor() + ball.dy)  # sety() changes y coordinate

    # Border check
    if ball.ycor() > 290:  # top border
        ball.sety(290)
        ball.dy *= -1  # reverse direction

    if ball.ycor() < -290:  # bottom border
        ball.sety(-290)
        ball.dy *= -1  # reverse direction

    if ball.xcor() > 390:  # right border
        ball.goto(0, 0)
        ball.dx *= -1  # reverse direction
        score_a += 1

    if ball.xcor() < -390:  # left border
        ball.goto(0, 0)
        ball.dx *= -1  # reverse direction
        score_b += 1

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
        ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50
    ):
        ball.setx(340)
        ball.dx *= -1
        score_b += 1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
        ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50
    ):
        ball.setx(-340)
        ball.dx *= -1
