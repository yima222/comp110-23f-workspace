from turtle import Turtle, colormode
colormode(255)
#leo: Turtle = Turtle()

# leo.forward(50)
# leo.left(30)
# leo.right(40)
# done()

# Exercise 1: Drawing a square
# i: int = 0
# while (i< 4):
    # leo.forward(300)
    # leo.left(90)
    # i = i + 1

# Exercise 2: Drawing a triangle
#leo.penup()
#leo.goto(-50,-20)
#leo.pendown()
# leo.color(99, 204, 250)
# leo.begin_fill()
# code for the shape to be filled
# leo.end_fill()
#leo.pencolor("pink")
#leo.fillcolor(32, 67, 93)
#leo.begin_fill()
#leo.color("green", "yellow")

#i: int = 0
#while (i< 3):
    #leo.forward(200)
    #leo.left(120)
    #i = i + 1
#leo.end_fill()

#leo.speed(50)
#leo.hideturtle()

bob: Turtle = Turtle()
bob.pencolor("black")
bob.penup()
bob.goto(45, 60)
bob.pendown()
bob.speed(60)

side_length: int = 300
i: int = 0
while (i< 3):
    bob.forward(side_length)
    bob.left(120)
    i = i + 1
side_length: side_length * 0.97
i: int = 0
while (i< 3):
    bob.forward(side_length)
    bob.left(120)
    i = i + 1