"""A program that uses Turtle and functions to create a peaceful ocean scene."""

__author__ = "730668363"

from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    ertle: Turtle = Turtle()
    # Draws a sand colored rectangle as the beach and
    # Draws a light blue colored rectngle as the ocean
    ertle.color(194, 178, 128)
    ertle.begin_fill( )
    draw_rectangle(ertle, -320, 0, 320)
    ertle.end_fill()
    ertle.color(173, 216, 230)
    ertle.begin_fill( )
    draw_rectangle(ertle, -320, 320, 320)
    ertle.end_fill()
    # Draws a yellow square as the sun
    ertle.color(253, 184, 19)
    ertle.begin_fill()
    draw_square(ertle, 230, 300, 80)
    ertle.end_fill()
    # Declare your Turtle variables here
    # Call the procedures you define and pass your Turtles as an argument
    done()

# Define the procedures for other components
def draw_rectangle(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a rectangle of the given width whose top left corner is located at x, y."""
    a_turtle.speed(100)
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0
    while i < 2:
        width = width*2
        a_turtle.forward(width)
        a_turtle.right(90)
        width = width/2
        a_turtle.forward(width)
        a_turtle.right(90)
        i = i + 1


def draw_square(b_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square of the given width whose top left corner is located at x, y."""
    b_turtle.speed(100)
    b_turtle.penup()
    b_turtle.goto(x, y)
    b_turtle.setheading(0.0)
    b_turtle.pendown()
    i: int = 0
    while i < 4:
        b_turtle.forward(width)
        b_turtle.right(90)
        i += 1


# Use the __name__ is "__main__" idiom shown in class
if __name__ == "__main__":
    main()