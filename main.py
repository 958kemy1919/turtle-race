from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(800,600)
user_color = screen.textinput("Make a guess", "Which turtle will win the race? Enter the color: ")

colors = ["blue", "green", "red", "yellow", "orange", "pink"]
y_positions = [-260,-160,-60, 40, 140, 240]

my_turtles = []

for i in range(0,6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(-380, y_positions[i])
    my_turtles.append(new_turtle)

is_race_on = True

while is_race_on:

    for turtle in my_turtles:
        random_distance = random.randint(0,20)
        turtle.forward(random_distance)
        if turtle.xcor() > 370:
            is_race_on = False
            if user_color == turtle.pencolor():
                print(f"You've won!! Your {user_color} turtle is the winner of the race.")
            else:
                print(f"You've lost!! {turtle.pencolor()} turtle is the winner of the race.")

screen.exitonclick()
