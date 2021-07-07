import turtle
t=turtle.Pen()
t.pensize(1)
color=["red","orange","yellow","green","blue","purple","pink","white","gray","black"]
turtle.bgcolor("black")
sides=eval(input("how many sides do u want"))
name=turtle.textinput("window title","what is your name")
t.speed(0)
for x in range(100):
    t.pencolor(color[x%4])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(name,font=("arial",int((x+4)/4),"bold"))
    t.left(90)
for x in range(100000):
    t.pencolor(color[x%sides])
    t.forward(x*3/sides+x)
    t.left(360/sides+1)
    t.width(x*sides/100)


