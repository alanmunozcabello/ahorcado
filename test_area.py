import turtle

piedra = turtle.Turtle()
piedra.speed(0)
piedra.color("gray")
piedra.shape("circle")

def x_y(x,y,i):
    if(i<6):
        y+=20
        x+=80
    else:
        y-=20
        x+=100
    return x,y

def lanzar_piedra():
    x=-600
    y=75
    piedra.penup()
    piedra.goto(x,y)
    piedra.speed(1)
    i=0
    while(i<13):
        x,y=x_y(x,y,i)
        piedra.goto(x,y)
        i+=1

lanzar_piedra()