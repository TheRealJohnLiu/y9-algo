import turtle
import random
import itertools

COLORS = ['red', 'blue', 'green', 'yellow', 'black', 'pink', 'gold', 'violet', 'orange', 'magenta', 'cyan']

def random_color(iterator=[]):  # intentional dangerous default value
    if not iterator:  # empty container
        colors = COLORS
        random.shuffle(colors)
        iterator.append(itertools.cycle(colors))

    return next(iterator[0])

def square(length, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    while length >= 10:
        color = random_color()  # change color after each square
        turtle.color(color)

        turtle.begin_fill()

        for _ in range(4):
            turtle.forward(length)
            turtle.right(90)

        turtle.end_fill()

        length -= 10

square(200, -100, 100)

turtle.done()