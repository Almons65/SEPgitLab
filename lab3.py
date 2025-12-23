import turtle

class Disk(object):
    def __init__(self, name="", xpos=0, ypos=0, height=20, width=40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width

    def showdisk(self):
        turtle.penup()
        turtle.goto(self.dxpos - self.dwidth/2, self.dypos)
        turtle.setheading(0) 
        turtle.pendown()

        turtle.fillcolor("lightgray")
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(self.dwidth)
            turtle.left(90)
            turtle.forward(self.dheight)
            turtle.left(90)
            turtle.end_fill()


        turtle.penup()
        turtle.goto(self.dxpos, self.dypos + 5)
        turtle.write(self.dname, align="center", font=("Arial", 10, "normal"))
        turtle.setheading(0)    

    def newpos(self, xpos, ypos):
        self.dxpos = xpos
        self.dypos = ypos

    def cleardisk(self):

        turtle.penup()
        turtle.goto(self.dxpos - self.dwidth/2, self.dypos)
        turtle.setheading(0)
        turtle.pendown()

        turtle.pencolor("white") 
        turtle.fillcolor("white")
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(self.dwidth)
            turtle.left(90)
            turtle.forward(self.dheight)
            turtle.left(90)
            turtle.end_fill()

        
        turtle.pencolor("black")