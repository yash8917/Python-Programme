# Yash Gupta...
import turtle
t= turtle.Turtle()
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(-2)
print("Yash Gupta...")
while (True):
    for i in range(6):
        for colour in ["red","blue","brown","green","grey","pink"]:
            turtle.color(colour)
            turtle.circle(100)
            turtle.left(33)

turtle.hideturtle()
turtle.mainloop()
