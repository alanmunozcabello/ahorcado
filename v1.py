import random
from animacion import *
#palabras=open("ahorcado/palabras.txt","r",encoding="utf-8") #archivo ya abrierto

def selector_palabra():
    p1="hola"
    p2="que tal"
    p3="como estas"
    numero=random.randint(1,3)
    
    #palabras.readline()

    if(numero==1):
        p_adv=p1
    elif(numero==2):
        p_adv=p2
    elif(numero==3):
        p_adv=p3

    return p_adv

def adivinador(p_adv):
    print(p_adv)
    # global malas  #en algun momento de mi codigo era necesario el global para la variable malas
    if(p_adv=="hola"): #en caso de ser hola
        l1=""   #l1= letra 1... l4= letra 4
        l2=""
        l3=""
        l4=""

        malas=0
        vida=6 #al parecer la variable intento está de decoración
        p_aux="" #p_aux=palabra auxiliar

        while(malas<6 and p_aux!=p_adv):
            letra=entradas()
            if(letra=="h" and l1==""): #primero intente con !="" pero no funciono ya que simpre empizan siendo "" oseea que es False, pero con == 
                #imprimir letra usada en pantalla
                l1=letra               #se chequea que sea igual a "" o lo que nos interesa que sea distinto de ""
            
            elif(letra=="o" and l2==""):
                #imprimir letra usada en pantalla
                l2=letra
                
            elif(letra=="l" and l3==""):
                #imprimir letra usada en pantalla
                l3=letra
                
            elif(letra=="a" and l4==""):
                #imprimir letra usada en pantalla
                l4=letra

            else:
                #imprimir letra usada en pantalla
                malas+=1
                vida-=1
                vidas(vida)
                animacion_fuego(malas)
            
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
        vida=0
        p_aux="" #p_aux=palabra auxiliar

        while(malas<6 and p_aux!=p_adv):
            letra=entradas()
            if(letra=="q" and l1==""):
                #imprimir letra usada en pantalla
                l1=letra
                
            elif(letra=="u" and l2==""):
                #imprimir letra usada en pantalla
                l2=letra
                
            elif(letra=="e" and l3==""):
                #imprimir letra usada en pantalla
                l3=letra
                

            #no es necesario para l4
            
            elif(letra=="t" and l5==""):
                #imprimir letra usada en pantalla
                l5=letra
                
            elif(letra=="a" and l6==""):
                #imprimir letra usada en pantalla
                l6=letra
                
            elif(letra=="l" and l7==""):
                #imprimir letra usada en pantalla
                l7=letra
                
            else:
                #imprimir letra usada en pantalla
                malas+=1
                vida=vida-1
                vidas(vida)
                animacion_fuego(malas)
            
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
        vida=6
        p_aux="" #p_aux=palabra auxiliar

        while(malas<6 and p_aux!=p_adv):
            letra=entradas()
            if(letra=="c" and l1==""):
                #imprimir letra usada en pantalla
                l1=letra
                
            elif(letra=="o" and l2==""):
                #imprimir letra usada en pantalla
                l2=letra
                l4=letra #l2 y l4 son la misma letra
                
            elif(letra=="m" and l3==""):
                #imprimir letra usada en pantalla
                l3=letra
                

            #no es necesario para l5

            elif(letra=="e" and l6==""):
                #imprimir letra usada en pantalla
                l6=letra
                
            elif(letra=="s" and l7==""):
                #imprimir letra usada en pantalla
                l7=letra
                
            elif(letra=="t" and l8==""):
                #imprimir letra usada en pantalla
                l8=letra
                
            elif(letra=="a" and l9==""):
                #imprimir letra usada en pantalla
                l9=letra
                
            elif(letra=="s" and l10==""):
                #imprimir letra usada en pantalla
                l10=letra
                
            else:
                #imprimir letra usada en pantalla
                malas+=1
                vida=vida-1
                vidas(vida)
                animacion_fuego(malas)

            p_aux=l1+l2+l3+l4+l5+l6+l7+l8+l9+l10 #se forma palabra auxiliar

        if(p_aux==p_adv):
            return True
        else:
            return False

#main
def main():
    intro_anim()
    p_adv=selector_palabra() #variable p_adv es palabra a adivinar
    print(adivinador(p_adv))

main()

#palabras.close()