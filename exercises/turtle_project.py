"""A program that uses Turtle and functions to create a peaceful ocean scene.

Attempting Above and beyond---try something fun---using the circle() function in Turtle.
"""

__author__ = "730668363"

from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    ertle: Turtle = Turtle()
    # Draws a sand colored rectangle as the beach and
    # Draws a light blue colored rectangle as the ocean
    ertle.color(194, 178, 128)
    ertle.begin_fill()
    draw_rectangle(ertle, -320, 0, 320)
    ertle.end_fill()
    ertle.color(173, 216, 230)
    ertle.begin_fill()
    draw_rectangle(ertle, -320, 320, 320)
    ertle.end_fill()
    # Draws a yellow square as the sun
    ertle.color(253, 184, 19)
    ertle.begin_fill()
    draw_square(ertle, 230, 300, 80)
    ertle.end_fill()
    # Draws triangles to represent sun rays
    i: int = 0
    x1: int = 0
    y1: int = 0
    while (i < 3):
        ertle.color(253, 184, 19)
        ertle.begin_fill()
        draw_triangle(ertle, 160 + x1, 260 + y1, 30)
        ertle.end_fill()
        x1 += 40
        y1 -= 60
        i += 1
    # Draw a sideways trapezoid with an upside down trapezoid to represent the fans of boats on the ocean
    ertle.color(173, 106, 250)
    ertle.begin_fill()
    draw_sideway_trapezoid(ertle, -300, 50, 70)
    ertle.end_fill()
    ertle.color(128, 128, 128)
    ertle.begin_fill()
    draw_updown_trapezoid(ertle, -310, 50, 60)
    ertle.end_fill()
    ertle.color(37, 203, 137)
    ertle.begin_fill()
    draw_sideway_trapezoid(ertle, -180, 150, 70)
    ertle.end_fill()
    ertle.color(128, 128, 128)
    ertle.begin_fill()
    draw_updown_trapezoid(ertle, -190, 150, 60)
    ertle.end_fill()
    ertle.color(238, 65, 12)
    ertle.begin_fill()
    draw_sideway_trapezoid(ertle, -50, 70, 70)
    ertle.end_fill()
    ertle.color(128, 128, 128)
    ertle.begin_fill()
    draw_updown_trapezoid(ertle, -60, 70, 60)
    ertle.end_fill()
    # Trapezoid to represent curve of ocean
    ii: int = 0
    x2: int = 0
    while (ii < 6):
        ertle.pencolor(173, 106, 250)
        ertle.color(173, 216, 230)
        ertle.begin_fill()
        draw_updown_trapezoid(ertle, -320 + x2, 0, 128)
        ertle.end_fill()
        x2 += 128
        ii += 1
    # Draw circle with smaller circles to represent a polka-dotted beachball
    ertle.color(161, 246, 104)
    ertle.begin_fill()
    draw_circle(ertle, 50, 160, -230)
    ertle.end_fill()
    iii: int = 0
    x3: int = 0
    y3: int = 0
    while (iii < 7):
        ertle.color(246, 104, 222)
        ertle.begin_fill()
        draw_circle(ertle, 5, 130 + x3, -215 + y3)
        ertle.end_fill() 
        x3 += 10
        y3 += 10
        iii += 1
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
        width = width * 2
        a_turtle.forward(width)
        a_turtle.right(90)
        width = width / 2
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


def draw_triangle(c_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a wave shape of the given width whose top left corner is located at x, y."""
    c_turtle.speed(100)
    c_turtle.penup()
    c_turtle.goto(x, y)
    c_turtle.setheading(0.0)
    c_turtle.pendown()
    i: int = 0
    while (i < 3):
        c_turtle.forward(width)
        c_turtle.left(120)
        i = i + 1
    

def draw_sideway_trapezoid(d_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a trapezoid of the given width whose one acute angle is located at x, y."""
    d_turtle.speed(100)
    d_turtle.penup()
    d_turtle.goto(x, y)
    d_turtle.setheading(0.0)
    d_turtle.pendown()
    width = width / 2
    d_turtle.forward(width)
    d_turtle.left(60)
    d_turtle.forward(width)
    d_turtle.left(60)
    d_turtle.forward(width)
    width = width * 2
    d_turtle.left(120)
    d_turtle.forward(width)


def draw_updown_trapezoid(e_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a trapezoid of the given width whose one acute angle is located at x, y."""
    e_turtle.speed(100)
    e_turtle.penup()
    e_turtle.goto(x, y)
    e_turtle.setheading(0.0)
    e_turtle.pendown()
    e_turtle.forward(width)
    e_turtle.right(120)
    width = width / 2
    e_turtle.forward(width)
    e_turtle.right(60)
    e_turtle.forward(width)
    e_turtle.right(60)
    e_turtle.forward(width)


def draw_circle(g_turtle: Turtle, radius: float, x: float, y: float) -> None:
    """Draw circle whoes center is at x, y."""
    g_turtle.speed(100)
    g_turtle.penup()
    g_turtle.goto(x, y)
    g_turtle.setheading(0.0)
    g_turtle.pendown()
    g_turtle.circle(radius)


# Use the __name__ is "__main__" idiom shown in class
if __name__ == "__main__":
    main()