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

# use a keyboard binding to call the paddle_a_up function,
window.listen()
# below will call the method paddle_a_up when the w character is pressed - :)
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")






# main game loop

while True:
# below use spaces to move 4 character spaces - can use tabs but must keep it consistant
    window.update()
    