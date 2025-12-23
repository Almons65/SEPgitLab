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

class Pole(object):
    def __init__(self, name="", xpos=0, ypos=0, thick=10, length=100):
        self.pname = name
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length
        self.stack = [] 
        self.toppos = 0 

    def showpole(self):
        """Display the pole."""
        turtle.penup()
        turtle.goto(self.pxpos - self.pthick/2, self.pypos)
        turtle.setheading(0)
        turtle.pendown()

        turtle.fillcolor("black")
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(self.pthick)
            turtle.left(90)
            turtle.forward(self.plength)
            turtle.left(90)
            turtle.end_fill()

        turtle.penup()
        turtle.goto(self.pxpos, self.pypos - 20)
        turtle.write(self.pname, align="center", font=("Arial", 12, "bold"))

    def pushdisk(self, disk):
        """Place a disk onto this pole."""
        
        new_y = self.pypos + self.toppos

        
        disk.newpos(self.pxpos, new_y)

        
        disk.showdisk()

        
        self.stack.append(disk)
        self.toppos += disk.dheight

    def popdisk(self):
        """Remove the top disk from this pole."""
        if not self.stack:
            return None

       
        disk = self.stack.pop()

        
        disk.cleardisk()

        
        self.toppos -= disk.dheight

        
        disk.newpos(self.pxpos, self.pypos + self.plength + 20)
        disk.showdisk()

        return disk

class Hanoi(object):
    def __init__(self, n=3, start="A", workspace="B", destination="C"):
        self.startp = Pole(start, -200, 0)
        self.workspacep = Pole(workspace, 0, 0)
        self.destinationp = Pole(destination, 200, 0)
        
        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()
        
        for i in range(n):
            width = 120 - (i * 30) 
            d = Disk("d" + str(i), 0, 0, 20, width)
            self.startp.pushdisk(d)

    def move_disk(self, start, destination):
        disk = start.popdisk()
      
        disk.cleardisk() 
        destination.pushdisk(disk)

    def move_tower(self, n, s, d, w):
        if n == 1:
            self.move_disk(s, d)
        else:
            self.move_tower(n-1, s, w, d)
            self.move_disk(s, d)
            self.move_tower(n-1, w, d, s)

    def solve(self):
        self.move_tower(3, self.startp, self.destinationp, self.workspacep)

if __name__ == "__main__":
    turtle.setup(800, 600)
    turtle.speed(3) 
    turtle.hideturtle()
    
    h = Hanoi()
    h.solve()
    
    turtle.done()