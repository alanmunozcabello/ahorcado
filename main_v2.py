import random
from animacion import *
"defs"

def selector_palabra(): #segun un numero random se elige la frase o palabra
    p1="mandarina"
    p2="macetero"
    p3="perro sentado"
    p4="escrituras falsas"
    p5="pompella"
    numero=random.randint(1,5)

    if(numero==1):
        p_adv=p1
    elif(numero==2):
        p_adv=p2
    elif(numero==3):
        p_adv=p3
    elif(numero==4):
        p_adv=p4
    elif(numero==5):
        p_adv=p5
    return p_adv

def adivinador(p_adv):
    print(p_adv)
    vida=6 #cantidad base de vidas
    malas=0
    buenas=0 #variable cantidad de letras buenas
    l_usadas=""
    k=0
    while(k<len(p_adv)): #chequea por espacios, si se encuentran se da una buena por cada espacio
        if(p_adv[k]==" "):
            buenas+=1
            k+=1
        else:
            k+=1
    
    while(malas<6 and buenas<len(p_adv)):#ciclo para ingresar letras hasta que pierda o gane
        #letra=str(input("ingrese una letra: ")) #ingresar letra
        letra=entradas()
        usada=0 #variable check si se usó la letra
        k=0
        while(k<len(l_usadas) and usada!=1): #revisar si la letra fue usada
            if(letra==l_usadas[k]):
                usada=1
                k+=1
            else:
                k+=1

        if(usada==0): #si usada == 0 significa que no se a utilizado
            l_usadas+=letra
            l_buena=0 #variable check si la letra ingresada es correcta o no
            i=0
            while(i<len(p_adv)): #chequea si la letra se encuentra en la palabra a adivinar
                if(letra==p_adv[i]): #si es que se encuentra en p_adv
                    l_buena+=1
                    buenas+=1
                    print(letra) #cambiar po dibujar letra en index i
                    #dibujar letra en espacio de letras buenas
                    i+=1

                else: #sino se pasa al siguiente index
                    i+=1
            if(l_buena==0):
                vida-=1
                vidas(vida)
                malas+=1
                animacion_fuego(malas)

                print("letra mala", malas) #cambiar por escribir en posicion letras usadas
        else:
            print("letra usada")

    if(malas==6):
        return 0
    else:
        return 1

def gana_o_pierde(g_o_p):
    if(g_o_p==0):
        animacion_pierde()
        print("perdiste")
    else:
        animacion_gana()
        print("ganaste")

def main():
    intro_anim()
    p_adv=selector_palabra() #variable p_adv es palabra a adivinar
    g_o_p=adivinador(p_adv)
    gana_o_pierde(g_o_p)

"main"

main()