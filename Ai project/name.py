import turtle as t
t.pen()
t.bgcolor("Black")
colors=["red","green","yellow","blue","gray","aqua","purple","brown","gray"]
name=t.textinput("Enter Your name","Enter your name")
s=int(t.numinput("Number of sides","How many sides you want(1-60)",10,1,20))
for i in range(100):
    t.pencolor(colors[i%s%10])
    t.penup()
    t.forward(i*5)
    t.pendown()
    t.write(name,font=("",int((i*2+4)/4),"bold"))
    t.left(360/s+4)