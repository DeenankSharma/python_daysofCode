from turtle import Turtle,Screen
import random

screen = Screen()

race_is_on = False


screen.setup(height=400,width=500)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
colors = ["red",'blue','purple','orange','green','yellow']
turtles=[]
n=0

if user_bet:
    race_is_on=True

for i in range(0,len(colors)):
        t = Turtle(shape="turtle")
        t.color(colors[i])
        t.penup()
        t.goto(x=-240,y=-100 + n)
        n = n+40
        turtles.append(t)


while(race_is_on):

    for turtle in turtles:
        if turtle.xcor()>220:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner!")
            race_is_on=False
        if(race_is_on==True):
            turtle.forward(random.randint(0,10))


screen.exitonclick()