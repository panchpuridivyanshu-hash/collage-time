import turtle
import math
t=turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.color("red")

for i in range(0,360):
    t.penup()
    angle=math.radians(i+20)
    x=20*math.sin(angle)**3
    y=13*math.cos(angle)-3*math.cos(2*angle)\
        -2*math.cos(3*angle)-math.cos(4*angle)
    t.goto(x*20,y*20)
    t.pendown()
    t.goto(0,0)
