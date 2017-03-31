from projectFunction import *
import turtle

bob=turtle.Turtle()
hole=turtle.Turtle()
hole.speed(0)
bob.speed(0)
#//This changes the speed in which the graphic is being created.//


#                        ---MAIN PROGRAM---

turtle.bgcolor('black')
#//Changes the background's color to black.//
turtle.colormode(255)
#//This enables the shape to change color.//

hole.goto(-500,-150)
#//Places the center of the hole to the middle of the screen.//
for times in range (255):
    c=(255-times,255-times,255-times)
    hole.color(c)
    polygon(hole,1,1000)
    hole.left(145)
    hole.forward(times)
#//Makes the hole's color turn from white to black,//
#//how many lines are made, and the angle in which it turns.//

circles(bob)
#//This imports the colored circles into the program.//
