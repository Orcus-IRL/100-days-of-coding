from turtle import Screen
import random
import turtle as t

tim = t.Turtle()
tim.speed(0)
tim.penup()
tim.hideturtle()
t.colormode(255)
rgb_colors = [(249, 246, 240), (240, 250, 246), (251, 243, 249), (241, 245, 250), (35, 19, 15), (197, 144, 123),
              (30, 106, 155), (142, 85, 55), (9, 21, 45), (236, 213, 85), (196, 135, 155), (156, 62, 90), (221, 85, 66),
              (153, 17, 37), (202, 79, 104), (14, 54, 30), (162, 163, 35), (118, 172, 196), (41, 125, 79), (77, 12, 22),
              (120, 188, 160), (18, 92, 53), (11, 58, 137), (23, 201, 179), (23, 174, 206), (139, 222, 208),
              (149, 23, 16), (223, 172, 191), (233, 172, 162), (238, 206, 8)]

tim.setheading(220)

tim.forward(300)
tim.setheading(0)
number_of_dots =100
for dot_count in range(1,number_of_dots+1):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)

    if dot_count%10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
my_screen = Screen()
my_screen.exitonclick()
