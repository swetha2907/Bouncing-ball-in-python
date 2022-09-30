from tkinter import *
a=Tk()
a.title('Bouncing ball')
a.resizable(False,False)
WIDTH,HEIGHT=500,500
b=Canvas(a,width=WIDTH,height=HEIGHT)
b.pack()
Ball=b.create_oval(10,10,40,40,fill='darkred')
xspeed=yspeed=3
def moveBall():
    global xspeed,yspeed
    b.move(Ball,xspeed,yspeed)
    (leftPos,topPos,rightPos,bottomPos)=b.coords(Ball)
    if leftPos <= 0 or rightPos >= WIDTH:
        xspeed = -xspeed
    if topPos <= 0 or bottomPos>=HEIGHT:
        yspeed = -yspeed
    b.after(30,moveBall)
b.after(30,moveBall)
a.mainloop()
