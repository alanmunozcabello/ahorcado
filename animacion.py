import turtle
#from codigo_fuente import *
#from codigo_fuente import p_adv
"defs"

lapiz = turtle.Turtle()
lapiz.hideturtle()
fuego= turtle.Turtle()
fuego.hideturtle()
piedra=turtle.Turtle()
piedra.hideturtle()
piedra.shape("circle")
piedra.width(10)
gui=turtle.Turtle()
gui.hideturtle()
letras_correctas=turtle.Turtle()
letras_correctas.hideturtle()
letras_incorrectas=turtle.Turtle()
letras_incorrectas.hideturtle()
letras_correctas.shape()
letras_incorrectas.speed(0)
letras_correctas.speed(0)
letras_incorrectas.shape()
gui.speed(0)
lapiz.speed(5)
fuego.speed(0)
turtle.bgcolor("lightblue") #sin el turtle no cambia el background color de la ventana, no se por que tira error. no debería... pero funciona :D

def landscape(): #dibujo del landscape
    turtle.setup(width=1920, height=1080, startx=0, starty=0)
    lapiz.speed(0)
    lapiz.setheading(0)
    lapiz.penup()
    lapiz.color("green")
    lapiz.goto(-1000,0)
    lapiz.width(1)
    lapiz.pendown()
    lapiz.begin_fill()
    lapiz.forward(1450)
    lapiz.right(110)
    lapiz.forward(350)
    lapiz.right(-20)
    lapiz.forward(150)
    lapiz.right(30)
    lapiz.forward(250)
    lapiz.setheading(180)
    lapiz.forward(2000)
    lapiz.end_fill()

    pila_troncos()

    #dibujar fogata
    fuego.setheading(0)
    fuego.penup()
    fuego.goto(60,0)
    fuego.color("red")
    fuego.width(2)
    fuego.pendown()
    fuego.begin_fill()
    fuego.forward(35)
    fuego.left(90)
    fuego.forward(50)
    fuego.left(135)
    fuego.forward(20)
    fuego.right(90)
    fuego.forward(20)
    fuego.left(90)
    fuego.forward(20)
    fuego.left(45)
    fuego.forward(36)
    fuego.end_fill()

    #dibujar arbol
    lapiz.penup()
    lapiz.goto(200,0)
    lapiz.setheading(0)
    lapiz.color("brown")
    lapiz.pendown()
    lapiz.begin_fill()
    lapiz.left(90)
    lapiz.forward(600)
    lapiz.right(90)
    lapiz.forward(20)
    lapiz.right(90)
    lapiz.forward(600)
    lapiz.right(90)
    lapiz.end_fill()
    lapiz.penup()
    lapiz.right(90)
    lapiz.forward(270)
    lapiz.left(90)
    lapiz.pendown()
    lapiz.forward(150)

    #escrituras de la ciudad
    lapiz.setheading(0)
    lapiz.color("yellow")
    lapiz.left(-90)
    lapiz.forward(20)
    lapiz.begin_fill()
    lapiz.left(90)
    lapiz.forward(20)
    lapiz.left(90)
    lapiz.forward(10)
    lapiz.left(90)
    lapiz.forward(40)
    lapiz.left(90)
    lapiz.forward(10)
    lapiz.left(90)
    lapiz.forward(10)
    lapiz.end_fill()

    tronco0() #dibujar leño inicial del feugo

    #dibuja el corazon que indica las vidas (codigo de tiktok)
    lapiz.penup()
    lapiz.goto(540,450) #al vajar las vidas se cambia el numero del corazon
    lapiz.speed(0)
    lapiz.pendown()
    lapiz.begin_fill()
    lapiz.pensize(3)
    lapiz.color("red")
    lapiz.left(50)
    lapiz.forward(53)
    lapiz.circle(20,200)
    lapiz.right(140)
    lapiz.circle(20,200)
    lapiz.forward(53)
    lapiz.end_fill()

def dibujar_ladron():
    lapiz.speed(0)
    lapiz.width(5)
    lapiz.hideturtle()
    lapiz.penup()
    lapiz.goto(400,100)
    lapiz.setheading(0) #setea donde mira el lapiz a default
    lapiz.pendown()
    lapiz.color("black")
    lapiz.circle(25)
    lapiz.left(-70)
    lapiz.forward(30)
    lapiz.left(-10)
    lapiz.forward(40)
    lapiz.left(270)
    lapiz.forward(50)
    lapiz.left(90)
    lapiz.forward(50)
    lapiz.backward(50)
    lapiz.right(90)
    lapiz.backward(50)
    lapiz.left(10)
    lapiz.forward(50)
    lapiz.left(50)
    lapiz.forward(50)
    lapiz.backward(50)
    lapiz.left(-50)
    lapiz.backward(50)
    lapiz.left(80)
    lapiz.backward(40)
    lapiz.right(120)
    lapiz.forward(60)
    lapiz.width(1)

def intro_sherif(): #animacion sherif parte 1

    #dibujar sheriff
    lapiz.penup()
    lapiz.setheading(0)
    lapiz.goto(-300,100)
    lapiz.speed(0)  
    lapiz.color("orange") #setea color a naranjo
    lapiz.pendown()
    lapiz.width(10)
    lapiz.circle(30) #cabeza
    lapiz.right(90) #     |
    lapiz.forward(80) #   v cuerpo
    lapiz.left(10)
    lapiz.forward(80)
    lapiz.right(180)
    lapiz.forward(80)
    lapiz.left(160)
    lapiz.forward(80)   
    lapiz.penup()   
    lapiz.setheading(0)
    lapiz.goto(-300,75)   
    lapiz.pendown() 
    lapiz.left(250)
    lapiz.forward(50)
    lapiz.left(180)
    lapiz.forward(50)
    lapiz.right(140)
    lapiz.forward(50)    
    lapiz.penup() #dejar de dibujar
    lapiz.color("black") #color de letras
    lapiz.goto(-250,150)
    lapiz.speed(1)
    lapiz.width(1)
    lapiz.pendown()
    lapiz.write("NOOOO LADRÓN QUE HACES!!!", True, font=("arial", 10)) #frase que escribe, True para hacer un pequeño delay, font para fuente y tamaño
    lapiz.speed(0)
    lapiz.clear()
    #parte 2 de animacion

    landscape() #redibujar landscape
    
    lapiz.setheading(0)
    lapiz.penup()
    lapiz.goto(-300,100) 
    lapiz.speed(0)
    lapiz.pendown() 
    lapiz.color("orange")
    lapiz.width(10)
    lapiz.circle(30)
    lapiz.right(90)
    lapiz.forward(80)
    lapiz.left(45)
    lapiz.forward(70)
    lapiz.right(180)
    lapiz.forward(70)
    lapiz.left(110)
    lapiz.forward(60)   
    lapiz.penup()   
    lapiz.goto(-300,75)   
    lapiz.pendown() 
    lapiz.forward(50)
    lapiz.left(180)
    lapiz.forward(50)
    lapiz.right(45)
    lapiz.forward(20)
    lapiz.left(90)
    lapiz.forward(20)   

def sherif_acepto_reto():
    lapiz.setheading(0)
    lapiz.penup()
    lapiz.speed(0)
    lapiz.color("black")
    lapiz.goto(-250,150)
    lapiz.speed(1)
    lapiz.width(1)
    lapiz.pendown()
    lapiz.write("Hmmm...", True, font=("arial",10))
    lapiz.undo()
    lapiz.write("No queda de otra", True, font=("arial", 10))
    lapiz.undo()
    lapiz.write("Comencemos...", True, font=("arial", 10))
    lapiz.undo()

def animacion_ladron(): #animacion ladron
    lapiz.width(5)
    lapiz.hideturtle()
    lapiz.penup()
    lapiz.goto(400,100)
    lapiz.setheading(0) #setea donde mira el lapiz a default
    lapiz.pendown()
    lapiz.color("black")
    lapiz.circle(25)
    lapiz.left(-70)
    lapiz.forward(30)
    lapiz.left(-10)
    lapiz.forward(40)
    lapiz.left(270)
    lapiz.forward(50)
    lapiz.left(90)
    lapiz.forward(50)
    lapiz.backward(50)
    lapiz.right(90)
    lapiz.backward(50)
    lapiz.left(10)
    lapiz.forward(50)
    lapiz.left(50)
    lapiz.forward(50)
    lapiz.backward(50)
    lapiz.left(-50)
    lapiz.backward(50)
    lapiz.left(80)
    lapiz.backward(40)
    lapiz.right(120)
    lapiz.forward(60)
    lapiz.width(1)
    # lapiz.color("pink") #escrituras de la ciudad
    # lapiz.setheading(-90)
    # lapiz.forward(20)
    # lapiz.begin_fill()
    # lapiz.left(90)
    # lapiz.forward(20)
    # lapiz.left(90)
    # lapiz.forward(10)
    # lapiz.left(90)
    # lapiz.forward(40)
    # lapiz.left(90)
    # lapiz.forward(10)
    # lapiz.left(90)
    # lapiz.forward(10)
    # lapiz.end_fill()

    lapiz.penup()
    lapiz.goto(250,160)
    lapiz.speed(2)
    lapiz.color("black")

    #dialogo
    lapiz.pendown()
    lapiz.write("Quieres esto?. . .", True, font=("arial", 10))
    lapiz.undo()
    #cuadro blanco para borrar
    # lapiz.penup()
    # lapiz.goto(250,60)
    # lapiz.pendown()
    # lapiz.color("white")
    # lapiz.speed(0)
    # lapiz.write("█████████████████████████████████", True, font=("arial", 10))

    lapiz.penup()
    lapiz.speed(3)
    lapiz.color("black")
    lapiz.goto(250,160)
    lapiz.pendown()
    lapiz.speed(1)
    lapiz.write("SOLVE MY READLE!!!", True, font=("arial", 10))
    lapiz.undo()
    # lapiz.penup()
    # lapiz.goto(250,60)
    # lapiz.pendown()
    # lapiz.color("white")
    # lapiz.speed(0)
    # lapiz.write("█████████████████████████████████", True, font=("arial", 10))

    lapiz.penup()
    lapiz.color("black")
    lapiz.goto(170,160)
    lapiz.pendown()
    lapiz.speed(1)
    lapiz.write("Tienes que adivinar la frace que estoy pensando...", True, font=("arial", 10))
    lapiz.undo()

    # lapiz.penup()
    # lapiz.goto(170,60)
    # lapiz.pendown()
    # lapiz.color("white")
    # lapiz.speed(0)
    # lapiz.write("█████████████████████████████████", True, font=("arial", 10))

    lapiz.penup()
    lapiz.color("black")
    lapiz.goto(250,160)
    lapiz.pendown()
    lapiz.speed(1)
    lapiz.write("Tienes 6 intentos", True, font=("arial", 10))
    lapiz.undo()

    # lapiz.penup()
    # lapiz.goto(250,60)
    # lapiz.pendown()
    # lapiz.color("white")
    # lapiz.speed(0)
    # lapiz.write("█████████████████████████████████", True, font=("arial", 10))

    lapiz.penup()
    lapiz.color("black")
    lapiz.goto(250,160)
    lapiz.pendown()
    lapiz.speed(1)
    lapiz.write("Sinó... pues", True, font=("arial", 10))
    lapiz.undo()

    # lapiz.penup()
    # lapiz.goto(250,60)
    # lapiz.pendown()
    # lapiz.color("white")
    # lapiz.speed(0)
    # lapiz.write("█████████████████████████████████", True, font=("arial", 10))

    lapiz.penup()
    lapiz.color("black")
    lapiz.goto(250,160)
    lapiz.pendown()
    lapiz.speed(1)
    lapiz.write("You y tu town say bye bye ", True, font=("arial", 10))
    lapiz.undo()

    # lapiz.penup()
    # lapiz.goto(250,60)
    # lapiz.pendown()
    # lapiz.color("white")
    # lapiz.speed(0)
    # lapiz.write("█████████████████████████████████", True, font=("arial", 10))

    lapiz.penup()
    lapiz.color("black")
    lapiz.goto(250,160)
    lapiz.pendown()
    lapiz.speed(1)
    lapiz.write("MUAJAJAJAJAJA!!!!", True, font=("arial", 10))
    lapiz.undo()

    # lapiz.penup()
    # lapiz.goto(250,60)
    # lapiz.pendown()
    # lapiz.color("white")
    # lapiz.speed(0)
    # lapiz.write("█████████████████████████████████", True, font=("arial", 10))

    sherif_acepto_reto()

def animacion_fuego(malas):
    fuego.shape()
    if(malas==1):
        fuego.speed(0)
        fuego.penup()
        fuego.goto(60,0)
        fuego.color("red")
        fuego.width(2)
        fuego.setheading(0)
        fuego.pendown()
        fuego.begin_fill()
        fuego.forward(35)
        fuego.left(90)
        fuego.forward(70)#cambiante segun malas
        fuego.left(135)
        fuego.forward(20)
        fuego.right(90)
        fuego.forward(20)
        fuego.left(90)
        fuego.forward(20)
        fuego.left(45)
        fuego.forward(56)#cambiante segun malas
        fuego.end_fill()
        tronco0()
        tronco1()
    if(malas==2):
        fuego.speed(0)
        fuego.penup()
        fuego.goto(60,0)
        fuego.color("red")
        fuego.width(2)
        fuego.setheading(0)
        fuego.pendown()
        fuego.begin_fill()
        fuego.forward(35)
        fuego.left(90)
        fuego.forward(110)#cambiante segun malas
        fuego.left(135)
        fuego.forward(20)
        fuego.right(90)
        fuego.forward(20)
        fuego.left(90)
        fuego.forward(20)
        fuego.left(45)
        fuego.forward(86)#cambiante segun malas
        fuego.end_fill()
        tronco0()
        tronco1()
        tronco2()
    if(malas==3):
        fuego.speed(0)
        fuego.penup()
        fuego.goto(60,0)
        fuego.color("red")
        fuego.width(2)
        fuego.setheading(0)
        fuego.pendown()
        fuego.begin_fill()
        fuego.forward(35)
        fuego.left(90)
        fuego.forward(150)#cambiante segun malas
        fuego.left(135)
        fuego.forward(20)
        fuego.right(90)
        fuego.forward(20)
        fuego.left(90)
        fuego.forward(20)
        fuego.left(45)
        fuego.forward(136)#cambiante segun malas
        fuego.end_fill()
        tronco0()
        tronco1()
        tronco2()
        tronco3()
    if(malas==4):
        fuego.speed(0)
        fuego.penup()
        fuego.goto(60,0)
        fuego.color("red")
        fuego.width(2)
        fuego.setheading(0)
        fuego.pendown()
        fuego.begin_fill()
        fuego.forward(35)
        fuego.left(90)
        fuego.forward(200)#cambiante segun malas
        fuego.left(135)
        fuego.forward(20)
        fuego.right(90)
        fuego.forward(20)
        fuego.left(90)
        fuego.forward(20)
        fuego.left(45)
        fuego.forward(186)#cambiante segun malas
        fuego.end_fill()
        tronco0()
        tronco1()
        tronco2()
        tronco3()
        tronco4()
    if(malas==5):
        fuego.speed(0)
        fuego.penup()
        fuego.goto(60,0)
        fuego.color("red")
        fuego.width(2)
        fuego.setheading(0)
        fuego.pendown()
        fuego.begin_fill()
        fuego.forward(35)
        fuego.left(90)
        fuego.forward(240)#cambiante segun malas
        fuego.left(135)
        fuego.forward(20)
        fuego.right(90)
        fuego.forward(20)
        fuego.left(90)
        fuego.forward(20)
        fuego.left(45)
        fuego.forward(226)#cambiante segun malas
        fuego.end_fill()
        tronco0()
        tronco1()
        tronco2()
        tronco3()
        tronco4()
        tronco5()
    if(malas==6):
        fuego.speed(0)
        fuego.penup()
        fuego.goto(60,0)
        fuego.color("red")
        fuego.width(2)
        fuego.setheading(0)
        fuego.pendown()
        fuego.begin_fill()
        fuego.forward(35)
        fuego.left(90)
        fuego.forward(270)#cambiante segun malas
        fuego.left(135)
        fuego.forward(20)
        fuego.right(90)
        fuego.forward(20)
        fuego.left(90)
        fuego.forward(20)
        fuego.left(45)
        fuego.forward(256)#cambiante segun malas
        fuego.end_fill()
        tronco0()
        tronco1()
        tronco2()
        tronco3()
        tronco4()
        tronco5()
        tronco6()
        #llamar animacion de final (loss)

def intro_anim(): #llama a las otras animaciones para la introduccion
    landscape()
    dibujar_ladron()
    intro_sherif()
    animacion_ladron()
    vida=6 #vidas iniciales
    vidas(vida)

def entradas(): #muestra ventana para ingresar letras
    letra=turtle.textinput("", "ingrese una letra minuscula (solo una a la vez): ") 
    if(len(letra)==0):
        letra=turtle.textinput("entrada no valida", "ingrese UNA letra minuscula: ") #en caso de que ingresen algo diferente se recalca UNA letra
        return letra #haga o no haga caso el jugador se returna lo que haya ingresado
    elif(len(letra)>1):
        letra=turtle.textinput("entrada no valida", "ingrese UNA letra minuscula: ") #en caso de que ingresen algo diferente se recalca UNA letra
        return letra #haga o no haga caso el jugador se returna lo que haya ingresado
    else:
        return letra

def vidas(vida):
    lapiz.speed(0)
    lapiz.penup()
    lapiz.goto(532,475)
    lapiz.pendown()
    lapiz.setheading(0)
    lapiz.color("red")
    lapiz.begin_fill()
    lapiz.forward(30)
    lapiz.left(90)
    lapiz.forward(40)
    lapiz.left(90)
    lapiz.forward(30)
    lapiz.left(90)
    lapiz.forward(40)
    lapiz.left(90)
    lapiz.end_fill()
    lapiz.color("white")
    lapiz.write(vida,False, font=("jellee",25))

def mostrar_frase(p_adv,l_corr,frase_actual,frase_nueva):
    frase_nueva=""
    j=0
    while(j<len(frase_actual)):
        i=0
        while(i<len(l_corr)and j<len(frase_actual)):
            if(l_corr[i]==p_adv[j]):
                frase_nueva+=l_corr[i]
                j+=1
                i=0
            
            else:
                i+=1
        if(i==len(l_corr)):
            frase_nueva+=frase_actual[j]
        j+=1

    gui.clear()
    gui.penup()
    gui.goto(-100,-200)
    gui.write(frase_nueva, font=("arial",50))

    return frase_nueva

def animacion_gana():
    fuego.clear()
    tronco0()
    lapiz.penup()
    lapiz.goto(250,160)
    lapiz.color("black")
    lapiz.pendown()
    lapiz.speed(1)
    lapiz.write("Ganó esta vez, sheriff...", True, font=("arial",10))
    lapiz.undo()

def animacion_pierde():
    lapiz.penup()
    lapiz.goto(250,160)
    lapiz.color("black")
    lapiz.pendown()
    lapiz.speed(1)
    lapiz.write("Perdió, sheriff, y el pueblo con usted", True, font=("arial",10))
    lapiz.undo()

def mostrar_letras_correctas(l_corr_nr):
    letras_correctas.clear()
    letras_correctas.speed(0)
    letras_correctas.penup()
    letras_correctas.goto(-700,-250)
    letras_correctas.pendown()
    letras_correctas.width(10)
    letras_correctas.color("lavender blush")
    letras_correctas.write(f"letras correctas usadas: {l_corr_nr}",font=("arial",20))

def mostrar_letras_incorrectas(l_incorr):
    letras_incorrectas.clear()
    letras_incorrectas.speed(0)
    letras_incorrectas.penup()
    letras_incorrectas.goto(-700,-400)
    letras_incorrectas.pendown()
    letras_incorrectas.width(10)
    letras_incorrectas.color("tomato")
    letras_incorrectas.write(f"letras incorrectas usadas: {l_incorr}",font=("arial",20))

def pila_troncos():
    lapiz.penup()
    lapiz.goto(400,0)
    lapiz.pendown()
    lapiz.color("brown")
    lapiz.begin_fill()
    i=0
    while(i<2):
        lapiz.forward(25)
        lapiz.right(90)
        lapiz.forward(25)
        lapiz.right(90)
        i+=1
    lapiz.end_fill()
    lapiz.penup()
    lapiz.goto(425,0)
    lapiz.pendown()
    lapiz.begin_fill()
    i=0
    while(i<2):
        lapiz.forward(25)
        lapiz.right(90)
        lapiz.forward(25)
        lapiz.right(90)
        i+=1
    lapiz.end_fill()
    lapiz.penup()
    lapiz.goto(413,25)
    lapiz.pendown()
    lapiz.begin_fill()
    i=0
    while(i<2):
        lapiz.forward(25)
        lapiz.right(90)
        lapiz.forward(25)
        lapiz.right(90)
        i+=1
    lapiz.end_fill()

def tronco0():
    lapiz.speed(0)
    lapiz.setheading(0)
    lapiz.penup()
    lapiz.color("brown")
    lapiz.goto(55,15)
    lapiz.pendown()
    lapiz.begin_fill()
    i=0
    while(i<2):
        lapiz.forward(15)
        lapiz.right(90)
        lapiz.forward(15)
        lapiz.right(90)
        i+=1
    lapiz.end_fill()

def tronco1():
    lapiz.speed(0)
    lapiz.setheading(0)
    lapiz.penup()
    lapiz.color("brown")
    lapiz.goto(70,15)
    lapiz.pendown()
    lapiz.begin_fill()
    i=0
    while(i<2):
        lapiz.forward(15)
        lapiz.right(90)
        lapiz.forward(15)
        lapiz.right(90)
        i+=1
    lapiz.end_fill()

def tronco2():
    lapiz.speed(0)
    lapiz.setheading(0)
    lapiz.penup()
    lapiz.color("brown")
    lapiz.goto(55,30)
    lapiz.pendown()
    lapiz.begin_fill()
    i=0
    while(i<2):
        lapiz.forward(15)
        lapiz.right(90)
        lapiz.forward(15)
        lapiz.right(90)
        i+=1
    lapiz.end_fill()

def tronco3():
    lapiz.speed(0)
    lapiz.setheading(0)
    lapiz.penup()
    lapiz.color("brown")
    lapiz.goto(70,30)
    lapiz.pendown()
    lapiz.begin_fill()
    i=0
    while(i<2):
        lapiz.forward(15)
        lapiz.right(90)
        lapiz.forward(15)
        lapiz.right(90)
        i+=1
    lapiz.end_fill()

def tronco4():
    lapiz.speed(0)
    lapiz.setheading(0)
    lapiz.penup()
    lapiz.color("brown")
    lapiz.goto(55,45)
    lapiz.pendown()
    lapiz.begin_fill()
    i=0
    while(i<2):
        lapiz.forward(15)
        lapiz.right(90)
        lapiz.forward(15)
        lapiz.right(90)
        i+=1
    lapiz.end_fill()

def tronco5():
    lapiz.speed(0)
    lapiz.setheading(0)
    lapiz.penup()
    lapiz.color("brown")
    lapiz.goto(70,45)
    lapiz.pendown()
    lapiz.begin_fill()
    i=0
    while(i<2):
        lapiz.forward(15)
        lapiz.right(90)
        lapiz.forward(15)
        lapiz.right(90)
        i+=1
    lapiz.end_fill()

def tronco6():
    lapiz.speed(0)
    lapiz.setheading(0)
    lapiz.penup()
    lapiz.color("brown")
    lapiz.goto(55,60)
    lapiz.pendown()
    lapiz.begin_fill()
    i=0
    while(i<2):
        lapiz.forward(15)
        lapiz.right(90)
        lapiz.forward(15)
        lapiz.right(90)
        i+=1
    lapiz.end_fill()

def x_y(x,y,i):
    if(i<6):
        y+=20
        x+=45
    else:
        y-=15
        x+=60
    return x,y

def lanzar_piedra():
    piedra.speed(0)
    x=-290
    y=90
    piedra.penup()
    piedra.goto(x,y)
    piedra.showturtle()
    piedra.speed(3)
    i=0
    while(i<13):
        x,y=x_y(x,y,i)
        piedra.goto(x,y)
        i+=1