import random
import turtle
from turtle import Turtle, Screen
s = Screen()
s.setup(width=500, height=400)
user_input = s.textinput(title="Make your Bet", prompt="Which Turtle will win the race? Enter a color: ")
print(f"You placed your bets on {user_input} turtle")
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
d = 0
x = -230
y = -120
turtle_lst = []
for i in range(6):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colors[i])
    t. goto(x, y)
    y += 50
    turtle_lst.append(t)
f = True
if user_input:
    f = True
while f:
    for turtle in turtle_lst:
        if turtle.xcor() > 230:
            f = False
            win = turtle.pencolor()
            if win == user_input:
                print(f"You Won!, The {win} turtle is the winner!")
            else:
                print(f"You lose!, The {win} turtle is the winner!")
        r = random.randint(1,10)
        turtle.forward(r)








s.exitonclick()







