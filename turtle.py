import turtle
import time

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("#00704A")
t.color("black")
t.penup()
t.goto(-100, 0)
t.pendown()

# Define a function to draw the Starbucks logo
def draw_starbucks():
    t.begin_fill()
    t.circle(50)
    t.end_fill()

    t.penup()
    t.goto(-40, 30)
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    t.penup()
    t.goto(-20, 50)
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    t.penup()
    t.goto(20, 50)
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    t.penup()
    t.goto(40, 30)
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.end_fill()

# Animate the Starbucks logo
for i in range(50):
    t.clear()
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    t.color("red")
    draw_starbucks()
    t.penup()
    t.goto(-100 + i*5, 0)
    t.pendown()
    t.color("blue")
    draw_starbucks()
    time.sleep(0.05)

turtle.done()
