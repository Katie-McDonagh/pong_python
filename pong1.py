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


# main game loop

while True:
# below use spaces to move 4 character spaces - can use tabs but must keep it consistant
    window.update()
    