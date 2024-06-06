from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your Bet",
                            prompt="Which Turtle will win the race\nred, orange, yellow, green, blue, purple?\nEnter the color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []
y = -100
num = 0

for turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y)
    y += 40
    new_turtle.color(color[num])
    num += 1
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color.lower() == user_bet.lower():
                print(f"You've WON! The {winning_color} turtle is the winner")
            else:
                print(f"You've LOST! The {winning_color} turtle is the winner")
        turtle.forward(random.randint(0, 10))

screen.exitonclick()
