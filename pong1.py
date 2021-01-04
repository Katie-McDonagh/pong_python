#turtle is an inbuilt module that lets you do some basic graphics, oppose to pygame which move advanced

import turtle

# window is a variable which is importing a game screen from the turtle module
window = turtle.Screen()
# set a title for my window (I don't have to import the turtle module again, as I have already above)
window.title("Pong by Katie")
# putting styling directly into the window in the same file
window.bgcolor("black")
window.setup(width=800, height=600)
# tracer stops the window from updating, we have to manually update it, which means we can speed up the game alot
window.tracer

#Score
score_a = 0
score_b = 0

# paddle A 

# paddle_a is a turtle object (small t for the module turtle, and uppercase T for the class Turtle within the turtle module)
paddle_a = turtle.Turtle()
# paddle speed is the speed of animation, not how fast a paddle can move, 0 sets it to the maximum speed
paddle_a.speed(0)
# styling the paddle: there are a few built in shapes within turtle, we can use them by calling them in a string like below
paddle_a.shape("square")
paddle_a.color("white")
# by default the paddle will be 20px by 20px, it can be stretched by calling its height/width and by how much to be 
# stretched by so width=5 would be making it 5 times bigger
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
# to prevent the default of turtle drawing a line after an object moves we call the .penup method
paddle_a.penup()
# set the co-ordinates of where the paddle should start on the screen paddle.goto(x co-ordinates, y co-ordinates), the program 
# uses the center of the board is an default starting point, to the x and y co-ordinates are relative to center of board instead
# of the top left corner with JS
paddle_a.goto(-350,0)

# Paddle B 

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
# split the movement of the ball into vertical and horizonal, .dx means delta so its 'change x) which will be horizontal
# assigning it 2 means that everytime our ball moves it will move 2 pixels, in the below case it will move up and right by 2
# to go down and left we would use -2, to make it move at all you need to go to the main game loop.
ball.dx = 5
ball.dy = -5


# scoring 
# Pen
#pen is an turtle object, call small t for the turtle module and uppercase T for the class
pen = turtle.Turtle()
#annimation speed
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 24, "normal"))


# functions to move the paddles

def paddle_a_up():
    # set the y co-ordinate for the paddle before moving it, using the .ycor method from the turtle module
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# use a keyboard binding to call the paddle_a_up function,
window.listen()
# below will call the method paddle_a_up when the w character is pressed - :)
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "i")
window.onkeypress(paddle_b_down, "k")






# main game loop

while True:
# below use spaces to move 4 character spaces - can use tabs but must keep it consistant
    window.update()

    # move the ball

    # the first time a while loop is called the value of ball will be 2 (as ball.xcor starts at 0, and ball.dx == 2)
    # next iteration will be 4, 6, you get the idea.
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #set a border

    # when the ball's y co-ordinates gets to a certain point we want it to bounce back 
    # top of board is 300 and bottom is -300 as the height of the board is 600 altogether
    # however the ball is 20 pixels and takes up space so we set the y cords to 290 and -290
    if ball.ycor() > 290:
        ball.sety(290)
        # below reverses the direction of the ball to go down, but still travels across to the right.
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
      ball.goto(0,0)
      ball.dx *= -1
      score_a += 1
      pen.clear()
      pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    if ball.xcor() < -390:
      ball.goto(0,0)
      ball.dx *= -1
      score_b += 1
      pen.clear()
      pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))



    # paddle and ball colisions

    # right paddle 

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    # left paddle 

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1

    