import random
palabras=open("proyecto ahorcado/ahorcado/palabras.txt","r",encoding="utf-8") #archivo ya abrierto

def selector_palabra():
    p1="hola"
    p2="que tal"
    p3="como estas"
    numero=random.randint(1,3)
    
    if(numero==1):
        p_adv=p1
    elif(numero==2):
        p_adv=p2
    elif(numero==3):
        p_adv=p3

    return p_adv

def adivinador(p_adv):
    print(p_adv)
    if(p_adv=="hola"): #en caso de ser hola
        l1=""   #l1= letra 1... l4= letra 4
        l2=""
        l3=""
        l4=""

        malas=0
        intentos=0
        p_aux="" #p_aux=palabra auxiliar

        while(malas<6 and p_aux!=p_adv):
            letra=str(input(":"))
            if(letra=="h" and l1==""): #primero intente con !="" pero no funciono ya que simpre empizan siendo "" oseea que es False, pero con == 
                #imprimir letra usada en pantalla
                l1=letra               #se chequea que sea igual a "" o lo que nos interesa que sea distinto de ""
                intentos+=1
            elif(letra=="o" and l2==""):
                #imprimir letra usada en pantalla
                l2=letra
                intentos+=1
            elif(letra=="l" and l3==""):
                #imprimir letra usada en pantalla
                l3=letra
                intentos+=1
            elif(letra=="a" and l4==""):
                #imprimir letra usada en pantalla
                l4=letra
                intentos+=1
            else:
                #imprimir letra usada en pantalla
                malas+=1
                intentos+=1
            
            p_aux=l1+l2+l3+l4 #se forma palabra auxiliar
            
        if(p_aux==p_adv):
            print("yu win")
        else:
            print("game over")

    elif(p_adv=="que tal"):
        l1=""
        l2=""
        l3=""
        l4=" "
        l5=""
        l6=""
        l7=""
        malas=0
        intentos=0
        p_aux="" #p_aux=palabra auxiliar

        while(malas<6 and p_aux!=p_adv):
            letra=str(input(":"))
            if(letra=="q" and l1==""):
                #imprimir letra usada en pantalla
                l1=letra
                intentos+=1
            elif(letra=="u" and l2==""):
                #imprimir letra usada en pantalla
                l2=letra
                intentos+=1
            elif(letra=="e" and l3==""):
                #imprimir letra usada en pantalla
                l3=letra
                intentos+=1

            #no es necesario para l4
            
            elif(letra=="t" and l5==""):
                #imprimir letra usada en pantalla
                l5=letra
                intentos+=1
            elif(letra=="a" and l6==""):
                #imprimir letra usada en pantalla
                l6=letra
                intentos+=1
            elif(letra=="l" and l7==""):
                #imprimir letra usada en pantalla
                l7=letra
                intentos+=1
            else:
                #imprimir letra usada en pantalla
                malas+=1
                intentos+=1
            
            p_aux=l1+l2+l3+l4+l5+l6+l7 #se forma palabra auxiliar
            
        if(p_aux==p_adv):
            print("yu win")
        else:
            print("game over")

    elif(p_adv=="como estas"):
        l1=""
        l2=""
        l3=""
        l4=""
        l5=" "
        l6=""
        l7=""
        l8=""
        l9=""
        l10=""
        malas=0
        intentos=0
        p_aux="" #p_aux=palabra auxiliar

        while(malas<6 and p_aux!=p_adv):
            letra=str(input(":"))
            if(letra=="c" and l1==""):
                #imprimir letra usada en pantalla
                l1=letra
                intentos+=1
            elif(letra=="o" and l2==""):
                #imprimir letra usada en pantalla
                l2=letra
                l4=letra #l2 y l4 son la misma letra
                intentos+=1
            elif(letra=="m" and l3==""):
                #imprimir letra usada en pantalla
                l3=letra
                intentos+=1

            #no es necesario para l5

            elif(letra=="e" and l6==""):
                #imprimir letra usada en pantalla
                l6=letra
                intentos+=1
            elif(letra=="s" and l7==""):
                #imprimir letra usada en pantalla
                l7=letra
                intentos+=1
            elif(letra=="t" and l8==""):
                #imprimir letra usada en pantalla
                l8=letra
                intentos+=1
            elif(letra=="a" and l9==""):
                #imprimir letra usada en pantalla
                l9=letra
                intentos+=1
            elif(letra=="s" and l10==""):
                #imprimir letra usada en pantalla
                l10=letra
                intentos+=1
            else:
                #imprimir letra usada en pantalla
                malas+=1
                intentos+=1

            p_aux=l1+l2+l3+l4+l5+l6+l7+l8+l9+l10 #se forma palabra auxiliar

        if(p_aux==p_adv):
            print("yu win")
        else:
            print("game over")


#main

p_adv=selector_palabra() #variable p_adv es palabra a adivinar
adivinador(p_adv)

palabras.close()