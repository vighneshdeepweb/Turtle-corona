import turtle

#create a screen
screen = turtle.Screen()

#create a drawer for drawing
drawer = turtle.Turtle()

#Set the background color of the screen
screen.bgcolor("black")

#For set a Background,color,speed,pensize and color of the drawer
drawer.pencolor("darkgreen")
drawer.pensize(3)
drawer1 = 0
drawer2 = 0
drawer.speed(0)
drawer.goto(0, 200)
drawer.pendown()

#Create while loop for drawing Corona Virus Shape.
while True:
    drawer.forward(drawer1)
    drawer.right(drawer2)
    drawer1 += 3
    drawer2 += 1
    if drawer2 == 210:
        break
    drawer.ht()

# For Holding the main Screen
screen.mainloop()
        






