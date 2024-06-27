from turtle import Turtle,Screen

timmy = Turtle()
screen = Screen()

def move_forward():
    timmy.forward(10)

def move_backwards():
    timmy.backward(10)

def rotate_c():
    timmy.right(10)

def rotate_ac():
    timmy.left(10)

screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backwards)
screen.onkey(key="a",fun=rotate_ac)
screen.onkey(key="d",fun=rotate_c)

screen.exitonclick()