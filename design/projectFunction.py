#//This function can create any polygon.//
def polygon(t, sides, distance):
    angle = 360 / sides
    #t.begin_fill()
    for times in range(sides):
        t.forward(distance)
        t.left(angle)
    #t.end_fill()

#//This function tells turtle to jump to a certain coordinate without
#//making a line.//
def jump(t, x, y):
    t.pu()
    t.goto(x, y)
    t.pd()


#//This function draws the colored circles in the image.//
def circles(t):
    t.goto(650,-50)
    for times in range (75):
        c=(255,140,times)
        t.color(c)
        polygon(t,15,30)
        t.left(35)
        t.forward(times)
    jump(t,455,280)
    for times in range (75):
        c=(0,255-times,255)
        t.color(c)
        polygon(t,15,30)
        t.left(35)
        t.forward(times)   
    jump(t,-500,-200)
    for times in range (75):
        c=(255,0,255-times)
        t.color(c)
        polygon(t,15,30)
        t.left(35)
        t.forward(times)
    jump(t,-620,250)
    for times in range (75):
        c=(255,140,times)
        t.color(c)
        polygon(t,15,30)
        t.left(35)
        t.forward(times)

